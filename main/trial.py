import os
import numpy as np
import pandas as pd
import cv2
import csv
from scipy.spatial import distance_matrix
import glob


def merge_close_contours(contours, distance_thresh=50):
    """
    Merge contours whose centroids are closer than distance_thresh.
    Returns a new list of merged contours.
    """
    merged = []
    used = [False] * len(contours)

    # Compute centroids
    centroids = []
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0
        centroids.append((cx, cy))

    for i, c1 in enumerate(contours):
        if used[i]:
            continue
        merge_points = [c1]
        used[i] = True
        for j, c2 in enumerate(contours[i+1:], start=i+1):
            if used[j]:
                continue
            dist = np.linalg.norm(np.array(centroids[i]) - np.array(centroids[j]))
            if dist < distance_thresh:
                merge_points.append(c2)
                used[j] = True
        # Merge all points into one contour
        all_points = np.vstack(merge_points)
        merged.append(all_points)
    return merged



# path where the videos are stored
video_path = os.path.join(os.getcwd(),'Videos')

# tune this later
min_robot_area = 4000
max_robot_area = 13000

merge_distance_thresh = 50

# Edge detection parameters
canny_thresh1 = 50
canny_thresh2 = 150

for video_file in glob.glob(os.path.join(video_path,"*.avi")):
    print(f"Processing {video_file}...")
    # get the video name without .avi extension
    video_name = os.path.basename(video_file).split('.')[0]
    #make a csv file in the CSV folder with the same name as the video
    csv_name = os.path.join(os.getcwd(),"CSV",video_name + ".csv")

    # read the video
    cap = cv2.VideoCapture(video_file)
    with open(csv_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Frame","ObjectID","X","Y","Angle"])

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
            # frame_path = os.path.join(os.getcwd(),'figs',f"frame_{frame_idx:05d}.jpg")
            os.makedirs(os.path.join(os.getcwd(),"figs","grayscale"),exist_ok = True)
            if frame_idx == 1:
                gray_path = os.path.join(os.getcwd(),'figs',"grayscale",f"grayscale_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(gray_path, gray)

            # Gaussian blur
            gray = cv2.GaussianBlur(gray, (5, 5), 0)

            # Otsu thresholding for segmentation
            # _, thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            thresh = cv2.adaptiveThreshold(gray, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV,
                               11, 2)
            os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
            if frame_idx == 1: 
                thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(thresh_path, thresh)

            # Morphological cleanup
            kernel = np.ones((3, 3), np.uint8)
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
            kernel = np.ones((6, 6), np.uint8)
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

            os.makedirs(os.path.join(os.getcwd(),"figs","cleanup"),exist_ok = True)
            if frame_idx == 1:
                cleanup_path = os.path.join(os.getcwd(),'figs',"cleanup",f"cleanup_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(cleanup_path, thresh)
            
            # # ---- Fill holes inside contours ----
            # contours_all, _ = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            # thresh_filled = np.zeros_like(thresh)

            # for c in contours_all:
            #     cv2.drawContours(thresh_filled, [c], -1, 255, thickness=cv2.FILLED)
            # os.makedirs(os.path.join(os.getcwd(),"figs","flood_fill"),exist_ok = True)
            # if frame_idx == 1:
            #     floodfill_path = os.path.join(os.getcwd(),'figs',"flood_fill",f"floodfill_frame_{frame_idx:05d}.jpg")
            #     cv2.imwrite(floodfill_path, thresh_filled)
            # thresh = thresh_filled

            # # --- Edge detection ---
            # edges = cv2.Canny(thresh, canny_thresh1, canny_thresh2)

            # # Save edge image for debugging
            # os.makedirs(os.path.join(os.getcwd(),"figs","edges"),exist_ok = True)
            # if frame_idx == 1:
            #     edge_path = os.path.join(os.getcwd(),"figs","edges",f"edges_{frame_idx:05d}.jpg")
            #     cv2.imwrite(edge_path, edges)


            # Find contours
            # contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            contours, _ = cv2.findContours(thresh, cv2.RETR_LIST ,cv2.CHAIN_APPROX_SIMPLE)
            # Sort by area, largest first
            contours = sorted(contours, key=cv2.contourArea, reverse=True)

            # Drop the largest contour (outer boundary)
            # if len(contours) > 0:
            #     contours = contours[1:]
            # Merge nearby contours
            # contours = merge_close_contours(contours, distance_thresh=25)

            # Filter contours by area
            robot_contours = [c for c in contours if min_robot_area < cv2.contourArea(c) < max_robot_area]
            # Compute bounding boxes for each contour
            boxes = [cv2.boundingRect(c) for c in robot_contours]  # (x, y, w, h)
            merged_boxes = []
            used = [False] * len(boxes)
            # Merge nearby boxes
            for i, (x1, y1, w1, h1) in enumerate(boxes):
                if used[i]:
                    continue
                x_min, y_min = x1, y1
                x_max, y_max = x1 + w1, y1 + h1
                used[i] = True
                cx1, cy1 = x1 + w1 / 2, y1 + h1 / 2
                for j, (x2, y2, w2, h2) in enumerate(boxes):
                    if i == j or used[j]:
                        continue
                    cx2, cy2 = x2 + w2 / 2, y2 + h2 / 2
                    dist = np.hypot(cx1 - cx2, cy1 - cy2)
                    if dist < merge_distance_thresh:
                        x_min = min(x_min, x2)
                        y_min = min(y_min, y2)
                        x_max = max(x_max, x2 + w2)
                        y_max = max(y_max, y2 + h2)
                        used[j] = True
                merged_boxes.append((x_min, y_min, x_max - x_min, y_max - y_min))

            if frame_idx == 1:
                for c in contours:
                    cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
                # Make a copy of the frame to draw on
                frame_copy = frame.copy()
                # Draw all contours (in green)
                cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
                # Save or show the visualization
                os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
                contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(contour_path, frame_copy)

            centroids = []
            detections = []
            if frame_idx < 5:   # only print for first 5 frames
                for c in contours:
                    area = cv2.contourArea(c)
                    print(f"Frame {frame_idx}, Contour area: {area}")

            for (x, y, w, h) in merged_boxes:
                cx, cy = x + w / 2, y + h / 2
                angle = 0  # you can replace with minAreaRect if orientation is needed
                centroids.append((cx, cy))
                detections.append((cx, cy, angle))
                box = np.array([[x, y], [x + w, y], [x + w, y + h], [x, y + h]])
                cv2.polylines(frame, [box.astype(int)], isClosed=True, color=(0, 255, 0), thickness=2)

            # Hungarian-style matching (manual)
            if prev_centroids and centroids:
                dist = distance_matrix(prev_centroids, centroids)
                row_ind, col_ind = np.unravel_index(np.argsort(dist, axis=None), dist.shape)
            else:
                row_ind, col_ind = [], []

            assigned = {}
            used_cols = set()
            for r, c in zip(row_ind, col_ind):
                if r in robot_positions and c not in used_cols and dist[r, c] < 50:
                    assigned[c] = robot_positions[r]
                    used_cols.add(c)

            new_robot_positions = {}
            for i, (x, y, angle) in enumerate(detections):
                if i in assigned:
                    rid = assigned[i]
                else:
                    rid = next_id
                    next_id += 1
                new_robot_positions[i] = rid
                writer.writerow([frame_idx, rid, x, y, angle])
            
            cv2.putText(frame, f"ID:{rid}", (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            prev_centroids = centroids
            robot_positions = new_robot_positions

            # Save frame image
            os.makedirs(os.path.join(os.getcwd(),"figs","frames"),exist_ok = True)
            frame_path = os.path.join(os.getcwd(),'figs','frames',f"frame_{frame_idx:05d}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_idx += 1

    cap.release()
    print(f"Saved results to {csv_name}")