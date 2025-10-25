import os
import cv2
import numpy as np

def filter_contours(contours, video_name,frame_idx,thresh,frame):

    if video_name == "25Rods_OppDir_RigidMem-05162025171253-0000":
        min_contour_area = 350
        max_contour_area = 2000
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        if frame_idx % 5 == 0:
                for c in filtered_contours:
                    cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
                # Make a copy of the frame to draw on
                frame_copy = frame.copy()
                # Draw all contours (in green)
                cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
                # Save or show the visualization
                os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
                contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "25Rods_SameDir_RigidMem-05162025150152-0000":
        for c in contours:    
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "25Rods_SameDir_FlexMem-05162025160946-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        if frame_idx % 5 == 0:
                for c in contours:
                    cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
                # Make a copy of the frame to draw on
                frame_copy = frame.copy()
                # Draw all contours (in green)
                cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
                # Save or show the visualization
                os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
                contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 1200
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        if frame_idx % 5 == 0:
                for c in filtered_contours:
                    cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
                # Make a copy of the frame to draw on
                frame_copy = frame.copy()
                # Draw all contours (in green)
                cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
                # Save or show the visualization
                os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
                contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "26Rods_SameDir_FlexMem-05162025160700-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        if frame_idx % 5 == 0:
                for c in contours:
                    cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
                # Make a copy of the frame to draw on
                frame_copy = frame.copy()
                # Draw all contours (in green)
                cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
                # Save or show the visualization
                os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
                contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 1200
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        if frame_idx % 5 == 0:
                for c in filtered_contours:
                    cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
                # Make a copy of the frame to draw on
                frame_copy = frame.copy()
                # Draw all contours (in green)
                cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
                # Save or show the visualization
                os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
                contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "26Rods_OppDir_RigidMem-05162025171018-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        if frame_idx % 5 == 0:
                for c in contours:
                    cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
                # Make a copy of the frame to draw on
                frame_copy = frame.copy()
                # Draw all contours (in green)
                cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
                # Save or show the visualization
                os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
                contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 2000
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        if frame_idx % 5 == 0:
                for c in filtered_contours:
                    cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
                # Make a copy of the frame to draw on
                frame_copy = frame.copy()
                # Draw all contours (in green)
                cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
                # Save or show the visualization
                os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
                contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
                cv2.imwrite(contour_path, frame_copy)
        return filtered_contours

    elif video_name == "26Rods_SameDir_RigidMem-05162025145903-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 2000
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "27Rods_OppDir_RigidMem-05162025170726-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 1800
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(contours, key=cv2.contourArea,reverse=True)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    elif video_name == "27Rods_SameDir_FlexMem-05162025160403-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1300
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "27Rods_SameDir_RigidMem-05162025145613-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "28Rods_OppDir_RigidMem-05162025170439-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "28Rods_SameDir_FlexMem-05162025155844-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "28Rods_SameDir_RigidMem-05162025145314-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "29Rods_OppDir_RigidMem-05162025165939-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "29Rods_SameDir_FlexMem-05162025155017-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 470
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "29Rods_SameDir_RigidMem-05162025145019-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 470
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "30Rods_OppDir_RigidMem-05162025165645-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "30Rods_SameDir_FlexMem-05162025154730-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "30Rods_SameDir_RigidMem-05162025144721-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 600
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours

    elif video_name == "31Rods_OppDir_RigidMem-05162025165359-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 600
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "31Rods_SameDir_FlexMem-05162025154431-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 450
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "31Rods_SameDir_RigidMem-05162025144416-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "32Rods_OppDir_RigidMem-05162025165119-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    elif video_name == "32Rods_SameDir_FlexMem-05162025154112-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 1500
        
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "32Rods_SameDir_RigidMem-05162025144104-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    elif video_name == "33Rods_OppDir_RigidMem-05162025164826-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    elif video_name == "33Rods_SameDir_FlexMem-05162025153722-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1500
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "33Rods_SameDir_RigidMem-05162025143812-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        # contours1 = [c for c in contours if 200 <= cv2.contourArea(c) and cv2.contourArea(c) <= 2000]
        # sorted_contours = sorted(contours1, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Smallest area contours: ", [cv2.contourArea(c) for c in sorted_contours[0:3]])
        # print("frame idx: ", frame_idx, "Largest area contours: ", [cv2.contourArea(c) for c in sorted_contours[-3:]])
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1200
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "34Rods_OppDir_RigidMem-05162025164545-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 450
        max_contour_area = 1200
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "34Rods_SameDir_FlexMem-05162025153427-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 450
        max_contour_area = 1200
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "34Rods_SameDir_RigidMem-05162025143506-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1200
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if w < 60:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "35Rods_OppDir_RigidMem-05162025164249-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1200
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if w < 60:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "35Rods_SameDir_FlexMem-05162025153139-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1200
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if w < 60:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "35Rods_SameDir_RigidMem-05162025143206-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1200
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)

            if  w < 50 and h < 50:
                continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "36Rods_OppDir_RigidMem-05162025163948-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 450
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 20:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "36Rods_SameDir_FlexMem-05162025152832-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 20:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "36Rods_SameDir_RigidMem-05162025142903-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 20:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "37Rods_OppDir_RigidMem-05162025163704-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 20:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "37Rods_SameDir_FlexMem-05162025152535-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 500
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 20:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "37Rods_SameDir_RigidMem-05162025142527-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 550
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 5:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "38Rods_OppDir_RigidMem-05162025163417-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 5:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "38Rods_SameDir_FlexMem-05162025152234-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 5:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "38Rods_SameDir_RigidMem-05162025142150-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 400
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 5:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "39Rods_SameDir_RigidMem-05162025141934-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 300
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 5:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "40Rods_OppDir_RigidMem-05162025162822-0000":
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 300
        max_contour_area = 1100
        contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        filtered_contours = []
        for c in contours:
            _, _, w, h = cv2.boundingRect(c)
            w, h = max(w, h), min(w, h)
            if  w < 50 and h < 50:
                continue
            # if np.abs(w - h) < 5:
            #     continue
            filtered_contours.append(c)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours
    
    elif video_name == "40Rods_SameDir_RigidMem-05162025141328-0000":
        # print("In 25Rods_SameDir_FlexMem-05162025160946-0000")
        for c in contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","unfiltered contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"unfiltered contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        min_contour_area = 300
        max_contour_area = 1500
        filtered_contours = [c for c in contours if min_contour_area <= cv2.contourArea(c) and cv2.contourArea(c) <= max_contour_area]
        # sorted_contours = sorted(filtered_contours, key=cv2.contourArea)
        # print("frame idx: ", frame_idx, "Area: ", [cv2.contourArea(c) for c in sorted_contours[0:2]])
        split_contours = []
        expected_area = 800
        for c in filtered_contours:
            area = cv2.contourArea(c)
            if area > 2 * expected_area :  # ~2x larger than expected
                x, y, w, h = cv2.boundingRect(c)
                # Split along the longer axis
                if w > h:
                    box1 = np.array([[[x, y]], [[x + w//2, y]], [[x + w//2, y + h]], [[x, y + h]]])
                    box2 = np.array([[[x + w//2, y]], [[x + w, y]], [[x + w, y + h]], [[x + w//2, y + h]]])
                else:
                    box1 = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h//2]], [[x, y + h//2]]])
                    box2 = np.array([[[x, y + h//2]], [[x + w, y + h//2]], [[x + w, y + h]], [[x, y + h]]])
                split_contours.extend([box1, box2])
            else:
                split_contours.append(c)
        filtered_contours = split_contours
        for c in filtered_contours:
            cv2.drawContours(thresh, [c], -1, 255, thickness=cv2.FILLED)
        # Make a copy of the frame to draw on
        frame_copy = frame.copy()
        # Draw all contours (in green)
        cv2.drawContours(frame_copy, filtered_contours, -1, (0, 255, 0), 2)
        # Save or show the visualization
        os.makedirs(os.path.join(os.getcwd(),"figs","contour"),exist_ok = True)
        contour_path = os.path.join(os.getcwd(),'figs',"contour",f"contour_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(contour_path, frame_copy)
        return filtered_contours

    else:
        print("Video not found in filter contours")