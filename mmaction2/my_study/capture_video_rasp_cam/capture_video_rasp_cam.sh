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
source .env
# 現在の日時を取得
current_date=$(date +%m%d%H%M)

filename="${class_num}_${current_date}.mp4"
output_file_path="${RASP_VIDEO_PATH}${filename}"
# ------------------------------------------------------------------------------

# Capture video using raspivid
raspivid -o "$output_file_path" -t $((duration * 1000))

echo "Video captured and saved to $output_file_path"
