#!/bin/bash

echo "Enter the class number: "
read class_num

echo "Enter the start file number: "
read file_num

# Set the directory path
directory="rawvideo_dataset"

# Change to the directory
cd "$directory" || exit

# Rename the files
for file in $(ls ${class_num}_* | sort -V); do
  new_name="${class_num}_${file_num}.mp4"
  mv "$file" "${new_name}"
  ((file_num++))
done
