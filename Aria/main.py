import numpy as np
import pandas as pd

df = pd.read_csv('../sbdc_data.csv')


print(df["Total Counseling Time, hrs"].mean())


# Counting Number of NonZero in each column
print(df.astype(bool).sum(axis=0))

# Counting Whether They started business or Not
df_start_bs = df[df["Impact: Started Business"]=='Yes'] #1667
#print(df_start_bs)
df_start_bs_rev_inc = df_start_bs[df_start_bs["Impact: Revenue Increase"]>0]
#print(df_start_bs_rev_inc) #446




