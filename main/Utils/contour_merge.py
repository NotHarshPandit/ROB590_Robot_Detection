import cv2
import numpy as np

def merge_close_contours(contours, dist_threshold):
    """
    Merge contours if the minimum distance between any points of the contours is less than dist_threshold.
    
    Args:
        contours (list): List of contours (each contour is an ndarray of points).
        dist_threshold (float): Distance threshold below which contours are merged.
    
    Returns:
        merged_contours (list): List of merged contours.
    """
    merged = [False] * len(contours)
    output_contours = []

    for i in range(len(contours)):
        if merged[i]:
            continue
        current = contours[i]
        merged[i] = True

        # Merge loop: try to merge with other contours that are close
        merge_indices = [i]
        did_merge = True
        while did_merge:
            did_merge = False
            for j in range(len(contours)):
                if not merged[j]:
                    # Compute min distance between current contour and contour j
                    x, y = current[0][0]
                    pt = (int(x), int(y))
                    # Using boundingRect overlap approximate distance:
                    dist = contour_dist(current, contours[j])
                    if dist < dist_threshold:
                        merge_indices.append(j)
                        merged[j] = True
                        # Concatenate contours
                        current = np.vstack([current, contours[j]])
                        did_merge = True
        
        # After merging nearby contours, get convex hull as merged contour
        hull = cv2.convexHull(current)
        output_contours.append(hull)

    return output_contours

def contour_dist(c1, c2):
    # Efficient min Euclidean distance between points in two contours
    # Flatten contours to Nx2 arrays
    pts1 = c1.reshape(-1, 2)
    pts2 = c2.reshape(-1, 2)
    dists = np.linalg.norm(pts1[:, None] - pts2[None, :], axis=2)
    return np.min(dists)