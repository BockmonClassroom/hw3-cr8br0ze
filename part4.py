import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

# read file
df = pd.read_csv("Data/new_t1.csv")

# two groups
control_group = df[df["variant_number"] == 0]["active_mins"]
treatment_group = df[df["variant_number"] == 1]["active_mins"]

# box plot
plt.figure(figsize=(10, 10))
plt.boxplot([control_group, treatment_group], labels=["Control", "Treatment"])
plt.title("Box Plot by Group")
plt.ylabel("Active Minutes")
plt.grid(True)

plt.savefig('part4.png') 

# find outlier
IQR = df["active_mins"].quantile(0.75) - df["active_mins"].quantile(0.25)
df = df[(df["active_mins"] >= df["active_mins"].quantile(0.15)-1.5*IQR) & (df["active_mins"] <= df["active_mins"].quantile(0.75)+1.5*IQR)]
df.to_csv("Data/new_new_t1.csv", index=False)

#redo part2 part3
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
}).to_csv("Data/part4.csv", index=False)
