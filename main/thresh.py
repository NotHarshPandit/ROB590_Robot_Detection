import cv2
import os

def grayscale_to_thresh(gray, video_name, frame_idx):
    if video_name == "25Rods_OppDir_RigidMem-05162025171253-0000":
        # print("In 25Rods_OppDir_RigidMem-05162025171253-0000")
        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
            
    elif video_name == "25Rods_SameDir_RigidMem-05162025150152-0000":
        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh) 
    elif video_name == "25Rods_SameDir_FlexMem-05162025160946-0000":
        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "26Rods_SameDir_FlexMem-05162025160700-0000":
        _, thresh = cv2.threshold(gray, 88, 255, cv2.THRESH_BINARY)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "26Rods_OppDir_RigidMem-05162025171018-0000":
        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "26Rods_SameDir_RigidMem-05162025145903-0000":

        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "27Rods_OppDir_RigidMem-05162025170726-0000":

        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    
    elif video_name == "27Rods_SameDir_FlexMem-05162025160403-0000":

        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "27Rods_SameDir_RigidMem-05162025145613-0000":

        _, thresh = cv2.threshold(gray, 82, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "28Rods_OppDir_RigidMem-05162025170439-0000":

        _, thresh = cv2.threshold(gray, 82, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "28Rods_SameDir_FlexMem-05162025155844-0000":

        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "28Rods_SameDir_RigidMem-05162025145314-0000":

        _, thresh = cv2.threshold(gray, 81, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    
    elif video_name == "29Rods_OppDir_RigidMem-05162025165939-0000":

        _, thresh = cv2.threshold(gray, 81, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "29Rods_SameDir_FlexMem-05162025155017-0000":

        _, thresh = cv2.threshold(gray, 84.5, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "29Rods_SameDir_RigidMem-05162025145019-0000":

        _, thresh = cv2.threshold(gray, 79, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "30Rods_OppDir_RigidMem-05162025165645-0000":

        _, thresh = cv2.threshold(gray, 81, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)

    elif video_name == "30Rods_SameDir_FlexMem-05162025154730-0000":

        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        if frame_idx % 5 == 0: 
            thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
            cv2.imwrite(thresh_path, thresh)
    elif video_name == "30Rods_SameDir_RigidMem-05162025144721-0000":

        _, thresh = cv2.threshold(gray, 76, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)
    elif video_name == "31Rods_OppDir_RigidMem-05162025165359-0000":

        _, thresh = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)   
    elif video_name == "31Rods_SameDir_FlexMem-05162025154431-0000":

        _, thresh = cv2.threshold(gray,85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "31Rods_SameDir_RigidMem-05162025144416-0000":

        _, thresh = cv2.threshold(gray,78, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)
        
    elif video_name == "32Rods_OppDir_RigidMem-05162025165119-0000":

        _, thresh = cv2.threshold(gray,80, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "32Rods_SameDir_FlexMem-05162025154112-0000":

        _, thresh = cv2.threshold(gray,85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh) 
        
    elif video_name == "32Rods_SameDir_RigidMem-05162025144104-0000":

        _, thresh = cv2.threshold(gray,78, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)     
    elif video_name == "33Rods_OppDir_RigidMem-05162025164826-0000":

        _, thresh = cv2.threshold(gray,77, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)    

    elif video_name == "33Rods_SameDir_FlexMem-05162025153722-0000":

        _, thresh = cv2.threshold(gray,85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)
    elif video_name == "33Rods_SameDir_RigidMem-05162025143812-0000":

        _, thresh = cv2.threshold(gray,77, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "34Rods_OppDir_RigidMem-05162025164545-0000":

        _, thresh = cv2.threshold(gray,78, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "34Rods_SameDir_FlexMem-05162025153427-0000":

        _, thresh = cv2.threshold(gray,83, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "34Rods_SameDir_RigidMem-05162025143506-0000":

        _, thresh = cv2.threshold(gray,77, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "35Rods_OppDir_RigidMem-05162025164249-0000":

        _, thresh = cv2.threshold(gray,77, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)
    elif video_name == "35Rods_SameDir_FlexMem-05162025153139-0000":

        _, thresh = cv2.threshold(gray,78, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "35Rods_SameDir_RigidMem-05162025143206-0000":

        _, thresh = cv2.threshold(gray,77, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)
        
    elif video_name == "36Rods_OppDir_RigidMem-05162025163948-0000":

        _, thresh = cv2.threshold(gray,76, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)
        
    elif video_name == "36Rods_SameDir_FlexMem-05162025152832-0000":

        _, thresh = cv2.threshold(gray,82, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "36Rods_SameDir_RigidMem-05162025142903-0000":

        _, thresh = cv2.threshold(gray,76.5, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "37Rods_OppDir_RigidMem-05162025163704-0000":
        _, thresh = cv2.threshold(gray,76, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "37Rods_SameDir_FlexMem-05162025152535-0000":
        _, thresh = cv2.threshold(gray,77, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "37Rods_SameDir_RigidMem-05162025142527-0000":
        _, thresh = cv2.threshold(gray,75, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)
        
    elif video_name == "38Rods_OppDir_RigidMem-05162025163417-0000":
        _, thresh = cv2.threshold(gray,73, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)
    elif video_name == "38Rods_SameDir_FlexMem-05162025152234-0000":
        _, thresh = cv2.threshold(gray,73, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "38Rods_SameDir_RigidMem-05162025142150-0000":
        _, thresh = cv2.threshold(gray,75, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "39Rods_SameDir_RigidMem-05162025141934-0000":
        _, thresh = cv2.threshold(gray,75, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "40Rods_OppDir_RigidMem-05162025162822-0000":
        _, thresh = cv2.threshold(gray,63, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make obects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.erode(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    elif video_name == "40Rods_SameDir_RigidMem-05162025141328-0000":

        _, thresh = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)

        # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.erode(thresh, kernel, iterations=1)

        # Dilate (expand white regions, make objects thicker
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
        thresh = cv2.dilate(thresh, kernel, iterations=1)

        # Erode (shrink white regions, remove noise)
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # thresh = cv2.erode(thresh, kernel, iterations=1)

        # # Dilate (expand white regions, make objects thicker
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        # thresh = cv2.dilate(thresh, kernel, iterations=1)

        os.makedirs(os.path.join(os.getcwd(),"figs","thresh"),exist_ok = True)
        
        thresh_path = os.path.join(os.getcwd(),'figs',"thresh",f"thresh_frame_{frame_idx:05d}.jpg")
        cv2.imwrite(thresh_path, thresh)

    else:
        print("Video not found in thesh")
    return thresh
