import cv2
import os

# Define the video file path and the destination directory
video_path = 'C:/tool/gaussian-splatting/source_data/guitar/orginal_video/guitar.mov'
dest_dir = 'C:/tool/gaussian-splatting/source_data/guitar/images'
n = 10  # Save every n-th frame

# Create the destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Open the video file
video_capture = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video.")
else:
    frame_count = 0
    saved_frame_count = 0
    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()
        if not ret:
            break

        # Save every n-th frame
        if frame_count % n == 0:
            # Define the filename for each frame
            frame_filename = f"frame_{saved_frame_count:05d}.jpg"
            frame_path = os.path.join(dest_dir, frame_filename)

            # Save the frame as an image file
            cv2.imwrite(frame_path, frame)
            saved_frame_count += 1

        frame_count += 1

    # Release the video capture object
    video_capture.release()
    print(f"Frames have been successfully saved to {dest_dir}.")