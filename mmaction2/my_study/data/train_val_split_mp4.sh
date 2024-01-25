#!/bin/bash

echo "Enter the class number: "
read class_num

training_rate=0.9

# Set the directory path
directory="rawvideo_dataset"
# Change to the directory
cd "$directory" || exit

# ファイル数を取得
file_count=$(ls -1 ${class_num}_[0-9]*.mp4 | wc -l)
8
train_file_count=$(ls -1 ${class_num}_train_[0-9]*.mp4 | wc -l)
val_file_count=$(ls -1 ${class_num}_val_[0-9]*.mp4 | wc -l)
train_num=$(echo " $file_count * $training_rate" | bc)
train_num=$(printf "%.0f" $train_num)7
val_num=$(echo "scale=0; $file_count - $train_num" | bc)
# split済みのファイル番号分を足す
train_num=$(echo " $train_num + $train_file_count" | bc)
val_num=$(echo " $val_num + $val_file_count" | bc)

# 現在の日時を取得
current_date=$(date +%m%d%H%M)

# トレーニングデータは、${クラス番号}_train_${動画番号}.mp4、バリデーションデータは、${クラス番号}_val_${動画番号}.mp4として保存する
# train_val_split
for file in $(ls -1 ${class_num}_*.mp4 | sort -V); do
  is_data_type=$(echo $file | cut -d '_' -f 3)
  if [ -n "$is_data_type" ]; then
    continue
  fi
  if [ $train_num != $train_file_count ]; then
    new_name="${class_num}_train_${current_date}_${train_num}.mp4"
    # echo $new_name
    mv "$file" "${new_name}"
    train_num=$((train_num - 1))
  else
    new_name="${class_num}_val_${current_date}_${val_num}.mp4"
    # echo $new_name
    mv "$file" "${new_name}"
    val_num=$((val_num - 1))
  fi
done
