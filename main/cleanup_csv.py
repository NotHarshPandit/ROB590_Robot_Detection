import pandas as pd
import os
import numpy as np

# the path for the csv file
CSV_file_path = os.path.join(os.getcwd(),"CSV")
CSV_file_name = "27Rods_OppDir_RigidMem-05162025170726-0000.csv"
CSV_full_path = os.path.join(CSV_file_path,CSV_file_name)


# read the csv file
df = pd.read_csv(CSV_full_path)
# the total number of robots in the video
number_of_robots = int(CSV_file_name[0:2])
print("Total number of robots:", number_of_robots)
df = df[df["ObjectID"] != number_of_robots]
df.to_csv(CSV_full_path, index=False)
