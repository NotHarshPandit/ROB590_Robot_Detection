import os
import numpy as np
import cv2

def plot_points_to_track(frame, frame_idx, points,points_per_robot):
    """
    Plots the points to track (3 points per robot) on the given frame,
    connects them with lines, labels robot IDs, and saves the result.
    """
    imag_path = os.path.join(os.getcwd(), 'figs', "Tracked Points")
    os.makedirs(imag_path, exist_ok=True)

    frame_copy = frame.copy()

    for robot_id in range(points.shape[0]):
        # Ensure points are integers
        x1, y1 = map(int, points[robot_id][0])
        x2, y2 = map(int, points[robot_id][1])
    
        x = int((x1 + x2) / 2)
        y = int((y1 + y2) / 2)
        # Draw the 3 points
        cv2.circle(frame_copy, (x1, y1), 3, (0, 255, 0), -1)
        cv2.circle(frame_copy, (x2, y2), 3, (0, 255, 0), -1) 

        # Draw lines connecting them
        # x1 = 132
        # x2 = 186
        # y1 = 226
        # y2 = 217
        cv2.line(frame_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # if frame_idx == 0:
        #     print(x1, y1, x2, y2)


        # Label robot
        # cv2.putText(frame_copy, f"ID:{robot_id}", (int((x1+x2)/2), int((y1+y2)/2)),
                    # cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        cv2.putText(frame_copy, f"ID:{robot_id}", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


    # Save the full frame (after all robots are drawn)
    fig_path = os.path.join(imag_path, f"frame_{frame_idx:05d}.jpg")
    cv2.imwrite(fig_path, frame_copy)
    return frame_copy
