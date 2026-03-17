import numpy as np


#generate dataset
num_students = 200

student_id = np.arange(1, num_students + 1)
age = np.random.randint(18, 26, num_students)
attendance = np.random.randint(40, 101, num_students)
study_hours = np.random.randint(0, 41, num_students)
midterm = np.random.randint(0, 101, num_students)
final = np.random.randint(0, 101, num_students)

data = np.column_stack((student_id, age, attendance, study_hours, midterm, final))

header = "StudentID,Age,AttendancePercentage,StudyHoursPerWeek,MidtermScore,FinalScore"

np.savetxt("students.csv", data, delimiter=",", header=header, comments="", fmt="%d")

print("Dataset generated and saved to students.csv")

#load the csv file

loaded_data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)

columns = ["StudentID", "Age", "Attendance", "StudyHours", "Midterm", "Final"]

stats = {}

for i, col in enumerate(columns):

    column_data = loaded_data[:, i]

    stats[col] = {
        "mean": np.mean(column_data),
        "median": np.median(column_data),
        "std": np.std(column_data),
        "min": np.min(column_data),
        "max": np.max(column_data)
    }


#correlation matrix

corr_matrix = np.corrcoef(loaded_data.T)


#linear pridictor

midtermscore = loaded_data[:, 4]
final_scores = loaded_data[:, 5]

mean_mid = np.mean(midtermscore)
mean_final = np.mean(final_scores)

std_mid = np.std(midtermscore)
std_final = np.std(final_scores)

correlation = np.corrcoef(midtermscore, final_scores)[0,1]

predicted_final = mean_final + correlation * (std_final/std_mid) * (midtermscore - mean_mid)


#abs error

meanabserror = np.mean(np.abs(predicted_final - final_scores))

#report

with open("analysis_report.txt", "w") as f:

    f.write("STUDENT DATA ANALYSIS REPORT\n")

    f.write("Dataset Size: 200 Students\n\n")

    f.write("Descriptive Statistics:\n")

    for col in columns:
        f.write(f"\n{col}\n")
        f.write(f"Mean: {stats[col]['mean']:.2f}\n")
        f.write(f"Median: {stats[col]['median']:.2f}\n")
        f.write(f"Std: {stats[col]['std']:.2f}\n")
        f.write(f"Min: {stats[col]['min']:.2f}\n")
        f.write(f"Max: {stats[col]['max']:.2f}\n")

    f.write("\nCorrelation Matrix:\n")
    f.write(str(corr_matrix))
    f.write("\n\n")

    f.write(f"Correlation between Midterm and Final: {correlation:.3f}\n")
    f.write(f"Mean Absolute Error of Prediction: {meanabserror:.3f}\n")

print("Analysis report saved to analysis_report.txt")