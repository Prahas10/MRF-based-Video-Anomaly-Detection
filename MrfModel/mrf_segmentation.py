from skimage import color, segmentation
import os
import cv2
import numpy as np
from skimage import segmentation
from skimage import graph
from tqdm import tqdm


def perform_segmentation(frame):
    # Convert the frame to a 2D array
    image_2d = color.rgb2gray(frame)

    # Create a graph-based image representation
    labels = segmentation.slic(frame, compactness=30, n_segments=450)

    g = graph.rag_mean_color(frame, labels)

    # Apply Normalized Cuts algorithm to segment the image
    cut_mask = graph.cut_normalized(labels, g)

    # Modify the mask to create a binary mask for the segmented region
    mask = np.asarray(cut_mask, dtype=np.uint8)

    # Apply the mask to the original frame
    segmented_frame = frame * mask[:, :, np.newaxis]

    return segmented_frame


# Path to the root directory containing all frame directories
base_path = 'extracted_frames/testing'
video_names = [f'{i+1}' for i in range(21)]

# Iterate over all video directories
for video_name in tqdm(video_names, desc='Videos Progress'):
    video_path = os.path.join(base_path, video_name)

    if os.path.isdir(video_path):
        # Create a new directory for segmented frames
        output_directory = os.path.join(
            base_path, f'segmented_{video_name}')
        os.makedirs(output_directory, exist_ok=True)

        # Iterate over the files in the video directory
        for filename in os.listdir(video_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                # Construct the full path to the frame
                frame_path = os.path.join(video_path, filename)

                # Read the frame
                frame = cv2.imread(frame_path)

                # Perform segmentation
                segmented_frame = perform_segmentation(frame)

                # Save the segmented frame with the same name as the original frame
                output_path = os.path.join(output_directory, filename)
                cv2.imwrite(output_path, cv2.cvtColor(
                    segmented_frame, cv2.COLOR_BGR2RGB))
    print(f"Completed Segmenting Video {video_name}.")
