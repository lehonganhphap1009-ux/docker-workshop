import os
import sys

import pandas as pd

print("arguments:", sys.argv)

if len(sys.argv) < 2:
    raise ValueError("Usage: python pipeline.py <month>")

month = int(sys.argv[1])

os.makedirs("data", exist_ok=True)

df = pd.DataFrame({"day": [1, 2, 3], "num_passengers": [4, 5, 6]})
df["month"] = month

df.to_parquet(f"data/output_{month}.parquet", engine="pyarrow", index=False)

print(f"hello world, month = {month}")
print(df)


