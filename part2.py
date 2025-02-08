import pandas as pd

# read file
df1 = pd.read_csv("Data/t1_user_active_min.csv")
df2 = pd.read_csv("Data/t2_user_variant.csv")

# calculate total time regardless of date user is active
t1= df1.groupby("uid", as_index=False)["active_mins"].sum()

# merge user group to t1
new_t1 = t1.merge(df2[["uid", "variant_number"]], on="uid")

new_t1.to_csv("Data/new_t1.csv", index=False)
