import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
from matplotlib.widgets import SliderBase
from sklearn.neighbors import KNeighborsClassifier

# ==================== Load Model & Data ====================
print("Loading model and data...")
with open("model/knn_model.pkl", "rb") as f:
    saved = pickle.load(f)

knn = saved["knn"]
scaler = saved["scaler"]
le = saved["le"]
k = saved["k"]
X_train_scaled = saved["X_train_scaled"]
y_train = saved["y_train"]

df = pd.read_csv("my_dataset.csv")

# ==================== Color Scheme ====================
BG = "#0e0e14"
SURFACE = "#16161f"
C0 = "#e05c6c"  # at_risk → red
C1 = "#22d3a7"  # safe    → teal
ACCENT = "#7c5cfc"
TEXT = "#d8d6e8"
GRID = "#2a2a3d"

plt.rcParams.update(
    {
        "figure.facecolor": BG,
        "axes.facecolor": SURFACE,
        "axes.edgecolor": GRID,
        "axes.labelcolor": TEXT,
        "xtick.color": TEXT,
        "ytick.color": TEXT,
        "text.color": TEXT,
        "grid.color": GRID,
        "grid.linestyle": "--",
        "grid.alpha": 0.5,
        "font.family": "monospace",
    }
)

# ==================== Setup 2D KNN (training_volume vs sleep) ====================
feat_idx = [0, 1]
feat_names = ["Training Volume (scaled)", "Sleep Hours (scaled)"]
feat_raw_names = ["training_volume_hrs", "sleep_hours"]

X2d_train = X_train_scaled[:, feat_idx]
X2d = X_train_scaled[:, feat_idx]
y_encoded = y_train

knn_2d = KNeighborsClassifier(n_neighbors=k)
knn_2d.fit(X2d_train, y_train)

# Create decision boundary
h = 0.04
x_min, x_max = X2d_train[:, 0].min() - 1.2, X2d_train[:, 0].max() + 1.2
y_min, y_max = X2d_train[:, 1].min() - 1.2, X2d_train[:, 1].max() + 1.2
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = knn_2d.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# ==================== Interactive Plot ====================
fig, (ax_plot, ax_info) = plt.subplots(1, 2, figsize=(15, 7))
fig.patch.set_facecolor(BG)

# Left panel: Decision boundary + draggable point
ax_plot.set_facecolor(SURFACE)
for spine in ax_plot.spines.values():
    spine.set_edgecolor(GRID)

# Draw decision boundary
cmap_bg = ListedColormap([C0 + "28", C1 + "28"])
ax_plot.contourf(xx, yy, Z, cmap=cmap_bg, alpha=1.0)
ax_plot.contour(xx, yy, Z, colors=[GRID], linewidths=0.8, alpha=0.4)

# Plot training points
for cls, color, label in zip([0, 1], [C0, C1], le.classes_):
    mask = y_train == cls
    ax_plot.scatter(
        X2d_train[mask, 0],
        X2d_train[mask, 1],
        c=color,
        edgecolors="white",
        linewidths=0.3,
        s=30,
        alpha=0.6,
        label=f"Train: {label}",
        zorder=2,
    )

# Initialize draggable point at center
center = X2d_train.mean(axis=0)
(point,) = ax_plot.plot(
    [center[0]],
    [center[1]],
    "o",
    color="#ffff00",
    markersize=12,
    markeredgecolor="white",
    markeredgewidth=2,
    zorder=10,
    label="Query Point",
)
(neighbors_line,) = ax_plot.plot([], [], "w--", linewidth=0.5, alpha=0.3, zorder=1)

ax_plot.set_xlabel(feat_names[0], fontsize=11)
ax_plot.set_ylabel(feat_names[1], fontsize=11)
ax_plot.set_title(
    f"Interactive KNN Classifier (K={k})\nDrag the yellow point",
    fontsize=12,
    fontweight="bold",
    pad=14,
)
ax_plot.legend(loc="upper right", framealpha=0.2, fontsize=9)
ax_plot.grid(True, alpha=0.3)

# Right panel: Information display
ax_info.axis("off")
ax_info.set_facecolor(SURFACE)

current_state = {"point": center.copy(), "text_elements": []}


def update_info(point_scaled, is_dragging=False):
    """Update the information panel."""
    # Clear previous text
    for txt in current_state["text_elements"]:
        txt.remove()
    current_state["text_elements"] = []

    # Predict
    pred_class_encoded = knn_2d.predict([point_scaled])[0]
    pred_class = le.inverse_transform([pred_class_encoded])[0]
    proba = knn_2d.predict_proba([point_scaled])[0]

    # Find nearest neighbors
    distances, indices = knn_2d.kneighbors([point_scaled])
    distances = distances[0]
    indices = indices[0]

    # Get raw feature values (inverse scale)
    point_raw = np.array([point_scaled[0], point_scaled[1]])

    # Build text
    y_pos = 0.95
    info_text = []

    # Title
    title = ax_info.text(
        0.05,
        y_pos,
        "PREDICTION INFO",
        fontsize=12,
        fontweight="bold",
        transform=ax_info.transAxes,
        color=TEXT,
        va="top",
    )
    current_state["text_elements"].append(title)
    y_pos -= 0.08

    # Predicted class
    pred_color = C0 if pred_class == "at_risk" else C1
    pred_txt = ax_info.text(
        0.05,
        y_pos,
        f"Prediction: {pred_class.upper()}",
        fontsize=11,
        fontweight="bold",
        transform=ax_info.transAxes,
        color=pred_color,
        va="top",
    )
    current_state["text_elements"].append(pred_txt)
    y_pos -= 0.06

    # Confidence
    conf = max(proba) * 100
    conf_txt = ax_info.text(
        0.05,
        y_pos,
        f"Confidence: {conf:.1f}%",
        fontsize=10,
        transform=ax_info.transAxes,
        color=TEXT,
        va="top",
    )
    current_state["text_elements"].append(conf_txt)
    y_pos -= 0.06

    # Class probabilities
    prob_txt = ax_info.text(
        0.05,
        y_pos,
        "Class Probabilities:",
        fontsize=10,
        fontweight="bold",
        transform=ax_info.transAxes,
        color=TEXT,
        va="top",
    )
    current_state["text_elements"].append(prob_txt)
    y_pos -= 0.05

    for i, cls in enumerate(le.classes_):
        cls_color = C0 if cls == "at_risk" else C1
        p_txt = ax_info.text(
            0.10,
            y_pos,
            f"{cls}: {proba[i]:.3f}",
            fontsize=9,
            transform=ax_info.transAxes,
            color=cls_color,
            va="top",
            family="monospace",
        )
        current_state["text_elements"].append(p_txt)
        y_pos -= 0.045

    # Separator
    y_pos -= 0.02
    sep = ax_info.text(
        0.05,
        y_pos,
        "─" * 35,
        fontsize=8,
        transform=ax_info.transAxes,
        color=GRID,
        va="top",
    )
    current_state["text_elements"].append(sep)
    y_pos -= 0.05

    # K Nearest Neighbors
    nn_title = ax_info.text(
        0.05,
        y_pos,
        f"K={k} NEAREST NEIGHBORS",
        fontsize=10,
        fontweight="bold",
        transform=ax_info.transAxes,
        color=ACCENT,
        va="top",
    )
    current_state["text_elements"].append(nn_title)
    y_pos -= 0.06

    for i, (idx, dist) in enumerate(zip(indices, distances)):
        neighbor_class = le.inverse_transform([y_train[idx]])[0]
        nn_color = C0 if neighbor_class == "at_risk" else C1
        nn_txt = ax_info.text(
            0.10,
            y_pos,
            f"#{i+1}: {neighbor_class:8s} (dist={dist:.3f})",
            fontsize=8,
            transform=ax_info.transAxes,
            color=nn_color,
            va="top",
            family="monospace",
        )
        current_state["text_elements"].append(nn_txt)
        y_pos -= 0.045

        if i == 4:  # Show top 5
            break

    # Status
    status_txt = "(DRAGGING)" if is_dragging else "(Ready to drag)"
    status = ax_info.text(
        0.05,
        0.02,
        status_txt,
        fontsize=8,
        transform=ax_info.transAxes,
        color=GRID,
        va="bottom",
        style="italic",
    )
    current_state["text_elements"].append(status)


# Initial info display
update_info(center)

# ==================== Mouse Event Handlers ====================
dragging = [False]


def on_motion(event):
    """Handle mouse motion - update point and prediction."""
    if not dragging[0] or event.xdata is None or event.ydata is None:
        return

    # Constrain to plot bounds
    x = np.clip(event.xdata, x_min, x_max)
    y = np.clip(event.ydata, y_min, y_max)

    # Update point position
    new_point = np.array([x, y])
    point.set_data([x], [y])
    current_state["point"] = new_point

    # Update nearest neighbors visualization
    distances, indices = knn_2d.kneighbors([new_point])
    neighbor_points = X2d_train[indices[0]]

    # Draw lines to neighbors
    lines_x = [new_point[0]] * len(neighbor_points) + [np.nan]
    lines_y = [new_point[1]] * len(neighbor_points) + [np.nan]
    for pt in neighbor_points:
        lines_x.append(pt[0])
        lines_y.append(pt[1])
    neighbors_line.set_data(lines_x, lines_y)

    # Update info panel
    update_info(new_point, is_dragging=True)

    fig.canvas.draw_idle()


def on_press(event):
    """Handle mouse button press."""
    if event.inaxes == ax_plot:
        dragging[0] = True


def on_release(event):
    """Handle mouse button release."""
    dragging[0] = False
    # Clear neighbor lines
    neighbors_line.set_data([], [])
    update_info(current_state["point"], is_dragging=False)
    fig.canvas.draw_idle()


# Connect events
fig.canvas.mpl_connect("motion_notify_event", on_motion)
fig.canvas.mpl_connect("button_press_event", on_press)
fig.canvas.mpl_connect("button_release_event", on_release)

plt.tight_layout()
print("Interactive plot ready!")
print(f"Drag the yellow point to see real-time KNN predictions.")
print(f"K={k}, using features: {feat_raw_names}")
plt.show()
