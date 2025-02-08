import scipy.stats
import pandas as pd

# read file
df = pd.read_csv("Data/new_t1.csv")
df3 = pd.read_csv("Data/t3_user_active_min_pre.csv")

# calculate total time regardless of date user is active pre experiment
df3 = df3.groupby("uid", as_index=False)["active_mins"].sum()

# merge
df = df.merge(df3, on="uid", suffixes=("", "_pre"))

# difference
df["diff_act_mins"] = df["active_mins"] - df["active_mins_pre"]

IQR = df["diff_act_mins"].quantile(0.75) - df["diff_act_mins"].quantile(0.25)
df = df[(df["diff_act_mins"] >= df["diff_act_mins"].quantile(0.15)-1.5*IQR) & (df["diff_act_mins"] <= df["diff_act_mins"].quantile(0.75)+1.5*IQR)]

# two groups
control_group = df[df["variant_number"] == 0]["diff_act_mins"]
treatment_group = df[df["variant_number"] == 1]["diff_act_mins"]

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
}).to_csv("Data/part5.csv", index=False)
