# For this code to be accessible you first need to download the GA_2020_ADI_9 Digit Zip Code_v3.2 as a csv file.
# From there add it to your explore page with the adi.testing.csv of the zip codes that you specificially want and run this code

import pandas as pd
import numpy as np


test_df = pd.read_csv("./adi_testing.csv")
adi_df = pd.read_csv("./GA_2020_ADI_9 Digit Zip Code_v3.2.csv")

test_df["ZIP_4"] = pd.to_numeric(test_df["9-digit zip"].apply(lambda x: x.replace("-", "")), errors='coerce')
new_df = pd.merge(test_df, adi_df, on="ZIP_4")
new_df = new_df.drop(columns=["ZIP_4"])
new_df.to_csv("merged.csv")
