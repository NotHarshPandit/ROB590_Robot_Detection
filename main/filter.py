import os
import pandas as pd
import glob

# the below code is for joining data for robots which were not detected in the main tracking script
# this merges the csvs for those robots into the main csv

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# original_csv_path = os.path.join(os.getcwd(),'Videos',"Tracked Videos")
# file_name = "40 rods same direction"

# video_name = "40Rods_SameDir_RigidMem-05162025141328-0000"
# new_csv_path = os.path.join(os.getcwd(),"CSV","filtered_csv",video_name + ".csv")
# os.makedirs(os.path.join(os.getcwd(),"CSV","filtered_csv"), exist_ok = True)
# df1 = pd.read_csv(os.path.join(original_csv_path, file_name,f"{video_name}.csv"))
# robot_ids = [18,19,21,23]
# for robot_id in robot_ids:
#     csv_name = robot_id
#     df = pd.read_csv(os.path.join(original_csv_path, file_name, f"{csv_name}.csv"))
#     df["ObjectID"] = robot_id
#     df1.loc[df1["ObjectID"] == robot_id, :] = df.loc[df["ObjectID"] == robot_id, :].values
# df1.to_csv(os.path.join(new_csv_path), index = False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# below script is for filtering the csvs obtained from bounding box detection
# this will change the angle from theta to (90 - theta) is difference in consecutive frames is more than 10 degress

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# define the paths
csv_file_path = os.path.join(os.getcwd(),'CSV','Unfiltered')
os.makedirs(csv_file_path, exist_ok = True)

new_csv_path = os.path.join(os.getcwd(),"CSV","filtered_csv")
os.makedirs(new_csv_path, exist_ok = True)
# iterate through all csv files in the directory
for csv_file in glob.glob(os.path.join(csv_file_path,"*.csv")):
    # get the video name without .csv extension
    video_name = os.path.basename(csv_file).split('.')[0]
    # number_of_robots = int(video_name[0:2])
    df = pd.read_csv(csv_file)
    # iterate through each robot's data
    for robot_id in df["ObjectID"].unique():
        # filter data for the current robot
        df_robot = df[df["ObjectID"] == robot_id].reset_index(drop=True)
        for i in range(1, len(df_robot)):
            # calculate the difference in angle between consecutive frames
            angle_now = df_robot.at[i, "Angle"]
            angle_prev = df_robot.at[i-1, "Angle"]
            angle_diff = abs(angle_now - angle_prev)
            # if the difference is more than 10 degrees, adjust the angle
            if angle_diff > 10:
                df_robot.at[i, "Angle"] = (90 - angle_now)
        # update the main dataframe with the filtered angles
        df.loc[df["ObjectID"] == robot_id, "Angle"] = df_robot["Angle"].values
    # save the filtered dataframe to a new csv file
    df.to_csv(os.path.join(new_csv_path, f"{video_name}.csv"), index = False)


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""