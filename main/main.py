import os
import numpy as np
import pandas as pd
import cv2
import csv
from scipy.spatial import distance_matrix
import glob
from Utils import contour_merge
from thresh import grayscale_to_thresh
from contour import filter_contours
from hungarian_matchmaking import match_robots
# from filter import filter_robots
from points_to_track import plot_points_to_track

def select_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points_to_track.append((x, y))

# path where the videos are stored
saved_video_path = os.path.join(os.getcwd(),'Videos',"Tracked Videos")
os.makedirs(saved_video_path, exist_ok = True)
video_path = os.path.join(os.getcwd(),'Videos',"Original Videos")
os.makedirs(video_path, exist_ok = True)

for video_file in glob.glob(os.path.join(video_path,"*.avi")):
    print(f"Processing {video_file}...")
    # get the video name without .avi extension
    video_name = os.path.basename(video_file).split('.')[0]
    #make a csv file in the CSV folder with the same name as the video
    csv_name = os.path.join(os.getcwd(),"CSV","Unfiltered",video_name + ".csv")

    # read the video
    cap = cv2.VideoCapture(video_file)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out_path = os.path.join(saved_video_path, f"{video_name}_processed.avi")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

    # Get the number of robots from the video name
    number_of_robots = int(video_name[0:2])
    frame_idx = 0
    # if the number >= 36 then use optical flow to track
    with open(csv_name, "w", newline="") as f:
            writer = csv.writer(f)
            if number_of_robots >= 36:
                writer.writerow(["Frame","ObjectID","X","Y","Angle"])
                # Initialize the first frame
                ret, old_frame = cap.read()
                old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
                if video_name == "36Rods_OppDir_RigidMem-05162025163948-0000":
                    lk_params = dict(winSize=(21,21),
                                    maxLevel=2,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "36Rods_SameDir_FlexMem-05162025152832-0000":
                    lk_params = dict(winSize=(21,21),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "36Rods_SameDir_RigidMem-05162025142903-0000":
                    lk_params = dict(winSize=(17,17),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "37Rods_OppDir_RigidMem-05162025163704-0000":
                    lk_params = dict(winSize=(16,16),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "37Rods_SameDir_FlexMem-05162025152535-0000":
                    lk_params = dict(winSize=(14,14),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "37Rods_SameDir_RigidMem-05162025142403-0000":
                    lk_params = dict(winSize=(17,17),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "37Rods_SameDir_RigidMem-05162025142527-0000":
                    lk_params = dict(winSize=(17,17),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "38Rods_OppDir_RigidMem-05162025163417-0000":
                    lk_params = dict(winSize=(17,17),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "38Rods_SameDir_FlexMem-05162025152234-0000":
                    lk_params = dict(winSize=(17,17),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "38Rods_SameDir_RigidMem-05162025142150-0000":
                    lk_params = dict(winSize=(17,17),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                elif video_name == "39Rods_OppDir_RigidMem-05162025163122-0000":
                    lk_params = dict(winSize=(13,13),
                                    maxLevel=2,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "39Rods_SameDir_FlexMem-05162025151954-0000":
                    lk_params = dict(winSize=(21,21),
                                    maxLevel=1,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "39Rods_SameDir_RigidMem-05162025141934-0000":
                    lk_params = dict(winSize=(18,18),
                                    maxLevel=3,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "40Rods_OppDir_RigidMem-05162025162822-0000":
                    # lk_params = dict(winSize=(21,21),
                    #                 maxLevel=2,
                    #                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 0.03))
                    lk_params = dict(winSize=(15,15),
                                    maxLevel=2,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 7, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                elif video_name == "40Rods_SameDir_RigidMem-05162025141328-0000":
                    # use this params to detect majority of robots
                    # lk_params = dict(winSize=(15,15),
                    #                 maxLevel=2,
                    #                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 0.03))
                    points_per_robot = 2  # Using 2 points per robot for tracking
                    # use this params to detect remaining robots and merge csv later
                    lk_params = dict(winSize=(15,15),
                                    maxLevel=0,
                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
                   
                # Select points manually 
                points_to_track = []
                cv2.namedWindow("Select Points")
                cv2.setWindowProperty("Select Points", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.setMouseCallback("Select Points", select_point)
                print("Click points to track ({} per robot), then press any key to start...".format(points_per_robot))

                while True:
                    frame_copy = old_frame.copy()
                    for p in points_to_track:
                        cv2.circle(frame_copy, p, 1, (0, 0, 255), -1)
                    cv2.imshow("Select Points", frame_copy)
                    # Wait until user presses any key to start tracking
                    if cv2.waitKey(1) & 0xFF != 255:
                        break

                cv2.destroyWindow("Select Points")

                # Prepare point arrays for tracking
                points_to_track = np.array(points_to_track, dtype=np.float32).reshape(-1, 1, 2)
                
                # uncomment this when detecting all robots at once
                # Group points into sets of 2 per robot
                # if len(points_to_track) != number_of_robots * points_per_robot:
                #     raise ValueError(f"Expected {number_of_robots * points_per_robot} points per robot, but got {len(points_to_track)} total points.")
                
                points_restructured = points_to_track.reshape(-1, points_per_robot, 2)
                for robot_id in range(points_restructured.shape[0]):
                    x1, y1 = map(int, points_restructured[robot_id][0])
                    x2, y2 = map(int, points_restructured[robot_id][1])
                    # x3, y3 = map(int, points_restructured[robot_id][2])
                    x, y = (x1 + x2) / 2, (y1 + y2) / 2
                    deltax1 = x2 - x1
                    deltay1 = y2 - y1
                    angle1 = np.arctan2(deltay1, deltax1) * 180 / np.pi
                    # angle2 = np.arctan2(deltay2, deltax2) * 180 / np.pi
                    # angle = np.abs((angle1 + angle2) / 2)
                    angle = np.abs(angle1)
                    if angle > 90: 
                        angle = 180 - angle
                    writer.writerow([frame_idx, robot_id, x, y, angle])  # Initial angle set to 0
                plotted_frame = plot_points_to_track(old_frame, 0, points_restructured,points_per_robot)
                out.write(plotted_frame)

                # Start optical flow tracking
                frame_idx = 1
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    new_points, status, err = cv2.calcOpticalFlowPyrLK(
                        old_gray, frame_gray, points_to_track, None, **lk_params
                    )

                    good_new = new_points[status == 1]
                    # good_old = points_to_track[status == 1]

                    # Draw points and motion
                    frame_copy = frame.copy()
                    points_restructured = good_new.reshape(-1, points_per_robot, 2)
                    for robot_id in range(points_restructured.shape[0]):
                        x1, y1 = map(int, points_restructured[robot_id][0])
                        x2, y2 = map(int, points_restructured[robot_id][1])
                        # x3, y3 = map(int, points_restructured[robot_id][2])
                        # x, y = (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3
                        x, y = (x1 + x2) / 2, (y1 + y2) / 2
                        ddeltax1 = x2 - x1
                        deltay1 = y2 - y1
                        # deltax2 = x3 - x2
                        # deltay2 = y3 - y2
                        angle1 = np.arctan2(deltay1, deltax1) * 180 / np.pi

                        # angle2 = np.arctan2(deltay2, deltax2) * 180 / np.pi
                        angle = np.abs(angle1)
                        writer.writerow([frame_idx, robot_id, x, y, angle])
                    plotted_frame = plot_points_to_track(frame, frame_idx, points_restructured,points_per_robot)
                    out.write(plotted_frame)
                    
                    # Update for next iteration
                    old_gray = frame_gray.copy()
                    points_to_track = good_new.reshape(-1, 1, 2)
                    frame_idx += 1
                cap.release()
                out.release()
                cv2.destroyAllWindows()
                print(f"Saved video to {out_path}")

            else:
                    writer.writerow(["Frame","ObjectID","X","Y","Angle","Detected"])

                    robot_positions = {}
                    next_id = 0
                    prev_centroids = []
                    frame_idx = 0

                    while True:
                        ret, frame = cap.read()
                        if not ret:
                            break
                        
                        # convert to grayscale frame
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        thresh  = grayscale_to_thresh(gray, video_name, frame_idx)
                    
                        contours, _ = cv2.findContours(thresh, cv2.RETR_LIST ,cv2.CHAIN_APPROX_SIMPLE)
                        contours = filter_contours(contours, video_name,frame_idx,thresh,frame)
                        # print(len(contours))

                        centroids = []
                        detections = []
                        rectangles = []
                        for c in contours:
                            area = cv2.contourArea(c)
                            rect = cv2.minAreaRect(c)
                            (x, y), (w, h), angle = rect     
                            # print(w,h)           
                            centroids.append((x, y))
                            detections.append((x, y, angle))
                            rectangles.append(rect)

                        videos_dist = [
                            "34Rods_SameDir_RigidMem-05162025143506-0000",
                            "36Rods_OppDir_RigidMem-05162025163948-0000",
                            "36Rods_SameDir_RigidMem-05162025142903-0000",
                            "39Rods_SameDir_RigidMem-05162025141934-0000",
                            "40Rods_OppDir_RigidMem-05162025162822-0000"
                        ]

                        if video_name in videos_dist:
                            max_dist = 20
                        else:
                            max_dist = 15
                        new_robot_positions, carried_forward, detection_to_id,next_id = match_robots(robot_positions, detections,next_id,max_dist=max_dist)  
                        for i, (x, y, angle) in enumerate(detections):
                            rid = detection_to_id[i]
                            writer.writerow([frame_idx, rid, x, y, angle,"True"])
                            # if frame_idx == 0:
                            #     print(rid, w, h, angle)
                            
                            rect = rectangles[i]  # get corresponding rect
                            # Draw rectangle
                            box = cv2.boxPoints(rect)
                            box = np.int0(box)
                            cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)

                            # Draw ID and angle
                            cv2.putText(frame, f"ID:{rid}", (int(x), int(y)),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                        # Write carried-forward robots (not drawn)
                        for rid, x, y, angle in carried_forward:
                            # rid = detection_to_id[i]   # get the robot ID for this detection
                            writer.writerow([frame_idx, rid, x, y, angle,"False"])

                        # prev_centroids = centroids
                        robot_positions = new_robot_positions

                        out.write(frame)

                        # Save frame image
                        os.makedirs(os.path.join(os.getcwd(),"figs","frames"),exist_ok = True)
                        frame_path = os.path.join(os.getcwd(),'figs','frames',f"frame_{frame_idx:05d}.jpg")
                        cv2.imwrite(frame_path, frame)
                        frame_idx += 1
                    cap.release()
                    out.release()
                    print(f"Saved results to {csv_name}")
                    print(f"Saved video to {out_path}")