import numpy as np
from scipy.spatial import distance_matrix

def match_robots(robot_positions, detections, next_id, max_dist=15, max_missed=3):
    """
    Matches detections to existing robot positions based on distance.
    Assigns new IDs to unmatched detections.
    Unmatched previous robots carry forward their previous position 
    Args:
        robot_positions (dict): {robot_id: {'pos': (x, y, angle), 'missed': int}} from previous frame
        detections (list): [(x, y, angle), ...] for current frame
        next_id (int): next available ID for new robots
        max_dist (float): maximum distance to consider a match valid
        max_missed (int): how many frames a robot can be missing before being removed

    Returns:
        new_robot_positions (dict): updated {robot_id: {'pos': (x, y, angle), 'missed': int}}
        carried_forward (list): [(robot_id, x, y, angle), ...] robots with no matched detection
        detection_to_id (dict): {detection_index: robot_id}
        next_id (int): updated next_id after assigning new robots
    """
    new_robot_positions = {}
    carried_forward = []
    detection_to_id = {}

    robot_ids = list(robot_positions.keys())
    n_r = len(robot_ids)
    n_d = len(detections)

    if n_r == 0:
        # No previous robots → all detections get new IDs
        for d_idx, (x, y, angle) in enumerate(detections):
            new_robot_positions[next_id] = {'pos': (x, y, angle), 'missed': 0}
            detection_to_id[d_idx] = next_id
            next_id += 1
        return new_robot_positions, carried_forward, detection_to_id, next_id

    # Build distance matrix: robots x detections
    robot_coords = np.array([robot_positions[rid]['pos'][:2] for rid in robot_ids])
    detection_coords = np.array([det[:2] for det in detections])
    dist_matrix = distance_matrix(robot_coords, detection_coords)

    used_detections = set()
    # For each robot, assign closest detection within max_dist
    for r_idx, rid in enumerate(robot_ids):
        dists = dist_matrix[r_idx]
        dists[list(used_detections)] = np.inf
        min_idx = np.argmin(dists)
        if dists[min_idx] < max_dist:
            # Match found → update position and reset missed
            x, y, angle = detections[min_idx]
            new_robot_positions[rid] = {'pos': (x, y, angle), 'missed': 0}
            detection_to_id[min_idx] = rid
            used_detections.add(min_idx)
        else:
            # No match → carry forward previous position and increment missed
            prev_pos = robot_positions[rid]['pos']
            missed = robot_positions[rid]['missed'] + 1
            new_robot_positions[rid] = {'pos': prev_pos, 'missed': missed}
            carried_forward.append((rid, *prev_pos))

    # Any unmatched detections → assign new IDs
    for d_idx, (x, y, angle) in enumerate(detections):
        if d_idx not in used_detections:
            new_robot_positions[next_id] = {'pos': (x, y, angle), 'missed': 0}
            detection_to_id[d_idx] = next_id
            next_id += 1

    return new_robot_positions, carried_forward, detection_to_id, next_id
