import cv2
import os
from tqdm import tqdm


def extract_frames(video_path, output_dir, fps=3):
    # Make sure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Start capturing the video
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the frame index increment based on the desired fps
    frame_index_increment = int(cap.get(cv2.CAP_PROP_FPS) / fps)

    # Use tqdm for progress bar
    for frame_idx in tqdm(range(0, frame_count, frame_index_increment), desc="Extracting frames"):
        # Set the frame index
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)

        # Read the frame
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop if no frame is returned

        # Save each frame to the output directory
        frame_file = os.path.join(output_dir, f"frame_{frame_idx:05d}.png")
        cv2.imwrite(frame_file, frame)

    # Release the video capture object
    cap.release()


video_paths = ['Avenue Dataset/testing_videos/01.avi', 'Avenue Dataset/testing_videos/02.avi',
               'Avenue Dataset/testing_videos/03.avi', 'Avenue Dataset/testing_videos/04.avi',
               'Avenue Dataset/testing_videos/05.avi', 'Avenue Dataset/testing_videos/06.avi',
               'Avenue Dataset/testing_videos/07.avi', 'Avenue Dataset/testing_videos/08.avi',
               'Avenue Dataset/testing_videos/09.avi', 'Avenue Dataset/testing_videos/10.avi',
               'Avenue Dataset/testing_videos/11.avi', 'Avenue Dataset/testing_videos/12.avi',
               'Avenue Dataset/testing_videos/13.avi', 'Avenue Dataset/testing_videos/14.avi',
               'Avenue Dataset/testing_videos/15.avi', 'Avenue Dataset/testing_videos/16.avi',
               'Avenue Dataset/testing_videos/17.avi', 'Avenue Dataset/testing_videos/18.avi',
               'Avenue Dataset/testing_videos/19.avi', 'Avenue Dataset/testing_videos/20.avi',
               'Avenue Dataset/testing_videos/21.avi']

for video_path in video_paths:
    video_name = os.path.basename(video_path).split('.')[0]
    output_dir = f'extracted_frames/testing/{video_name}'
    extract_frames(video_path, output_dir, fps=3)
