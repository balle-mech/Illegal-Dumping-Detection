#!/bin/bash

echo "Enter the class number: "
read class_num

echo "Enter the train or val: "
read train_or_val

# Set the directory path
directory="raw_video"

# ソート前のファイル名を正規表現で取得
un_datatype_file_name=${class_num}_[0-9]*.mp4
# un_datatype_file_name=IMG_[0-9]*.mp4

# Change to the directory
cd "$directory" || exit

current_date=$(date +%m%d%H%M)

# Sort the files and rename them
# 値が２〜１７であるファイル以外をtrainに変換する
count=1
for file_name in $(ls ${un_datatype_file_name} | sort -V); do
  echo "file_name: $file_name"
  # video_num=$(echo $file_name | rev | cut -d '_' -f 1 | rev | cut -d '.' -f 1)
  base_name="${file_name%.mp4}"
  video_num=$(echo $base_name | cut -d '_' -f 2)
  echo "video_num $video_num"
  new_name="${class_num}_${train_or_val}_${current_date}_${video_num}.mp4"
  echo "newname: $new_name"
  mv "$file_name" "${new_name}"
  ((video_num++))
done
