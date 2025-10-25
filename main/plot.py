import matplotlib.pyplot as plt
import os
import glob
import pandas as pd
from filter import filter_angles


# the path for the csv file
CSV_file_path = os.path.join(os.getcwd(),"CSV")
CSV_file_name = "25Rods_SameDir_FlexMem-05162025160946-0000.csv"
CSV_full_path = os.path.join(CSV_file_path,CSV_file_name)

# read the csv file
df = pd.read_csv(CSV_full_path)


# the total number of robots in the video
number_of_robots = int(CSV_file_name[0:2])

# filter the angles in the dataframe
df = filter_angles(df,number_of_robots)

# making a file for the plots
plot_path = os.path.join(os.getcwd(),"figs","plots")
plot_folder_name = CSV_file_name.split(".")[0]
plot_full_path = os.path.join(plot_path,plot_folder_name)
os.makedirs(plot_full_path,exist_ok = True)

# we will make 3 plots x , y and theta against frame_id
# each plot will have data for 5 robots

# the batch size for the robots
robot_batch_size = 5

for i in range (0,number_of_robots,robot_batch_size):
    plt.figure(figsize=(15, 5))
    robot_ids = list(range(i,min(i+robot_batch_size,number_of_robots)))
    for ids in robot_ids:
        robot_data = df[df["ObjectID"] == ids]
        plt.subplot(1, 3, 1)
        plt.plot(robot_data["Frame"], robot_data["X"], label=f'Robot {ids}')
        plt.ylabel('X')
        plt.xlabel('Frame ID')
        plt.legend()
    
        plt.subplot(1, 3, 2)
        plt.plot(robot_data["Frame"], robot_data["Y"], label=f'Robot {ids}')
        plt.ylabel('Y')
        plt.xlabel('Frame ID')
        plt.legend()
    
        plt.subplot(1, 3, 3)
        plt.plot(robot_data["Frame"], robot_data["Angle"], label=f'Robot {ids}')
        plt.ylabel('Angle')
        plt.xlabel('Frame ID')
        plt.legend()
    plt.savefig(plot_full_path + f'/robots_{i}_to_{min(i+robot_batch_size,number_of_robots)-1}.png')
