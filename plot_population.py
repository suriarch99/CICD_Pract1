import matplotlib.pyplot as plt
import numpy as np

# Example data: population counts by age group
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
population_counts = [5000, 6000, 7000, 8000, 7500, 7200, 6300, 5000, 3000]

# Standard deviations for each age group (example data)
std_devs = [400, 500, 450, 550, 500, 480, 470, 400, 350]

# Calculate the 95% confidence intervals
# Assuming normally distributed data, use standard error = std_dev/sqrt(n)
# and that we have a large sample size, so the critical z-value for 95% confidence is approximately 1.96
sample_size = 100  # Example sample size
conf_intervals = [1.96 * (std / np.sqrt(sample_size)) for std in std_devs]

plt.figure(figsize=(10, 6))
plt.bar(age_groups, population_counts, color='skyblue', yerr=conf_intervals, capsize=5)

plt.xlabel('Age Group')
plt.ylabel('Population Count')
plt.title('Population by Age Group with 95% Confidence Intervals')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


def calculate_mean(data):
    return sum(data) / len(data)

def calculate_confidence_intervals(std_devs, sample_size):
    return [1.96 * (std / np.sqrt(sample_size)) for std in std_devs]
