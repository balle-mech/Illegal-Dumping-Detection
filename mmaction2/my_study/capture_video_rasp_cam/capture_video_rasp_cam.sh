#!/bin/bash
#!/bin/bash

echo "Enter the class number: "
read class_num

echo "Enter the file number: "
read file_num

# Set the duration of the video capture (in seconds)
duration=15

# Set the output file name and path --------------------------------------------

# Load the environment variables from the .env file
video_path="capture_video_rasp_cam/video/"
# 現在の日時を取得
current_date=$(date +%m%d%H%M)

filename="${class_num}_${current_date}"
output_file_path="${RASP_VIDEO_PATH}${filename}"
# ------------------------------------------------------------------------------

# Capture video using raspivid
libcamera-vid -t 15000 -o $output_file_path.h264

echo "ビデオを $output_file_path.h264に保存しました。"

# Convert the video to mp4 format
MP4Box -add $output_file_path.h264 $output_file_path.mp4

echo "ビデオをmp4ファイルに変換しました。ファイル名は$output_file_path.mp4"
