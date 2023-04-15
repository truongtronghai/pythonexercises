import statistics

MedicalTests = {
    "Cholesterol": [4.32, 3, 2],
    "Sugar": [3.45, 5, 6],
    "Enzyms": [2, 5.67, 4],
    "Calcium": [5.63, 4.67, 6],
}

total_all = 0.0
counting_all = 0
for k, v in MedicalTests.items():
    for item in v:
        total_all += item
        counting_all += 1

print(f"Global average of all values: {'{:.4f}'.format(total_all / counting_all)}")

StatisticMedicalTests = {
    k: {
        "mean": statistics.mean(v),
        "max": max(v),
        "min": min(v),
        "standard deviation": statistics.stdev(v),
        "variance": statistics.variance(v),
    }
    for (k, v) in MedicalTests.items()
}

for k, v in StatisticMedicalTests.items():
    print(f"{k}: {str(v)}")
