#!/usr/bin/env python3

import pandas as pd
import yaml

csv_file = "problems.csv"
yaml_file = "problems.yaml"

# Read the csv file
data = pd.read_csv(csv_file)

# Handle empty cells being read as 'NaN', by emptying them again
data = data.fillna("")

# Write the yaml file
with open(yaml_file, "w") as out_file:
    yaml.dump(data.to_dict(orient="records"), out_file,
              sort_keys=False)  # Prevent columns being reordered alphabetically
