#!/bin/bash

echo "Enter the class number: "
read class_num

echo "Enter the start file number: "
read file_num

# Set the directory path
directory="raw_video"

# ソート前のファイル名を正規表現で取得
unsorted_file_name=${class_num}__[0-9]*.mp4
# unsorted_file_name=IMG_[0-9]*.mp4

# Change to the directory
cd "$directory" || exit

# Rename the files
# for file in $(ls ${class_num}_* | sort -V); do
for file in $(ls $unsorted_file_name | sort -V); do
  new_name="${class_num}_${file_num}.mp4"
  mv "$file" "${new_name}"
  ((file_num++))
done
