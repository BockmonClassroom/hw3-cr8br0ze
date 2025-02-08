import scipy.stats
import pandas as pd

# read file
df = pd.read_csv("Data/new_t1.csv")
df3 = pd.read_csv("Data/t3_user_active_min_pre.csv")
df4 = pd.read_csv("Data/t4_user_attributes.csv")

# calculate total time regardless of date user is active pre experiment
df3 = df3.groupby("uid", as_index=False)["active_mins"].sum()

# merge
df = df.merge(df3, on="uid", suffixes=("", "_pre"))
df = df.merge(df4, on="uid")

# difference
df["diff_act_mins"] = df["active_mins"] - df["active_mins_pre"]

IQR = df["diff_act_mins"].quantile(0.75) - df["diff_act_mins"].quantile(0.25)
df = df[(df["diff_act_mins"] >= df["diff_act_mins"].quantile(0.15)-1.5*IQR) & (df["diff_act_mins"] <= df["diff_act_mins"].quantile(0.75)+1.5*IQR)]

attr1 = df[df["variant_number"] == 0].groupby("user_type")["diff_act_mins"].mean().reset_index()
gender1 = df[df["variant_number"] == 0].groupby("gender")["diff_act_mins"].mean().reset_index()
attr2 = df[df["variant_number"] == 1].groupby("user_type")["diff_act_mins"].mean().reset_index()
gender2 = df[df["variant_number"] == 1].groupby("gender")["diff_act_mins"].mean().reset_index()

attr = attr1.merge(attr2, on="user_type", suffixes=("_controled", "_treatment"))
genders = gender1.merge(gender2, on="gender", suffixes=("_controled", "_treatment"))

attr.to_csv("Data/part6_attr.csv", index=False)
genders.to_csv("Data/part6_genders.csv", index=False)