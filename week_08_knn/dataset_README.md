# Dataset README — Fitness Injury Risk

## Domain
Predicting whether a fitness athlete is at risk of injury based on one week
of training data.

## Features

| Column | Type | Range | Description |
|---|---|---|---|
| `training_volume_hrs` | float | 2 – 20 | Weekly training hours |
| `sleep_hours` | float | 4 – 10 | Average sleep per night (hours) |
| `protein_intake_g` | int | 40 – 200 | Daily protein intake (grams) |
| `injury_risk` | string | — | Target: `at_risk` or `safe` |

## Generation Method
Data was synthetically generated using `numpy` with `random_state=42`.
A weighted linear score with Gaussian noise (σ=0.13) was used to assign labels,
creating a realistic, non-linearly-separable boundary.

## Class Balance
Approximately 45% `at_risk`, 55% `safe` — within acceptable range.

## Scale Difference
`protein_intake_g` (range ~160) vs `sleep_hours` (range ~6) — 27× difference.
This makes `StandardScaler` essential before applying KNN.

## Records
300 total rows.
