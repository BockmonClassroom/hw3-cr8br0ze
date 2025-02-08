import scipy.stats
import pandas as pd

# read file
df = pd.read_csv("Data/new_t1.csv")

# two groups
control_group = df[df["variant_number"] == 0]["active_mins"]
treatment_group = df[df["variant_number"] == 1]["active_mins"]

# t-test
t_stat, p_value = scipy.stats.ttest_ind(control_group, treatment_group, equal_var=False)

# mean and medium
control_mean = control_group.mean()
control_median = control_group.median()
treatment_mean = treatment_group.mean()
treatment_median = treatment_group.median()

stats = pd.DataFrame({
    "Group": ["Control", "Treatment"],
    "Mean Active Minutes": [control_mean, treatment_mean],
    "Median Active Minutes": [control_median, treatment_median],
    "T-stats": [t_stat, t_stat],
    "P-value": [p_value, p_value]
}).to_csv("Data/part3.csv", index=False)

