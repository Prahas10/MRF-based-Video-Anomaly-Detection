import cv2
import os
import numpy as np


def compute_statistics(frame):
    # Compute mean and standard deviation of pixel values
    mean_value = np.mean(frame)
    std_dev = np.std(frame)
    return mean_value, std_dev


def extract_spatiotemporal_features(frames_dir):
    features = []

    # Iterate through each frame in the directory
    frame_files = sorted(os.listdir(frames_dir))
    prev_frame = None

    for frame_file in frame_files:
        # Read the frame
        frame_path = os.path.join(frames_dir, frame_file)
        frame = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE)

        # Compute statistics for the current frame
        mean_value, std_dev = compute_statistics(frame)
        frame_features = [mean_value, std_dev]

        # Compute optical flow if it's not the first frame
        if prev_frame is not None:
            flow = cv2.calcOpticalFlowFarneback(
                prev_frame, frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            # Compute magnitude and mean of the flow
            magnitude = np.sqrt(flow[..., 0]**2 + flow[..., 1]**2)
            mean_flow = np.mean(magnitude)
            frame_features.append(mean_flow)
        else:
            # Default values for optical flow in the first frame
            frame_features.append(0.0)
        # print(frame_features)
        features.append(frame_features)

        # Save the current frame as the previous frame for the next iteration
        prev_frame = frame

    return np.array(features)


# List of video names (adjust these based on your folder structure)
video_names = ['01', '02', '03', '04', '05', '06', '07', '08',
               '09', '10', '11', '12', '13', '14', '15', '16']

for video_name in video_names:
    frames_dir = f"extracted_frames/{video_name}"
    output_features = extract_spatiotemporal_features(frames_dir)

    # Save the features to a file or use them for further processing
    np.save(f"Features/{video_name}_features.npy", output_features)

print("Completed Extraction.")
