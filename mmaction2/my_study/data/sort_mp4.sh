#!/bin/bash

echo "Enter the class number: "
read class_num

# Set the directory path
directory="rawvideo_dataset"

# Change to the directory
cd "$directory" || exit

# Sort the files and rename them
count=1
for file in $(ls ${class_num}_* | sort -V); do
  new_name="${class_num}_${count}.mp4"
  mv "$file" "${new_name}"
  ((count++))
done
