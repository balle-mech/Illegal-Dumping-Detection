#!/bin/bash

class_num=2
training_rate=0.8

# Set the directory path
directory="rawvideo_dataset"
# Change to the directory
cd "$directory" || exit

# ファイル数を取得
file_count=$(ls -1 ${class_num}_* | wc -l)
# echo $file_count

train_count=$(echo " $file_count * $training_rate" | bc)
train_count=$(printf "%.0f" $train_count)
val_count=$(echo "scale=0; $file_count - $train_count" | bc)
# echo $train_count

# トレーニングデータは、${クラス番号}_train_${動画番号}.mp4、バリデーションデータは、${クラス番号}_val_${動画番号}.mp4として保存する

# train_val_split
for file in $(ls -1 ${class_num}_*.mp4 | sort -V); do
  if [ $train_count != 0 ]; then
    new_name="${class_num}_train_${train_count}.mp4"
    # echo $new_name
    mv "$file" "${new_name}"
    train_count=$((train_count - 1))
  else
    new_name="${class_num}_val_${val_count}.mp4"
    # echo $new_name
    mv "$file" "${new_name}"
    val_count=$((val_count - 1))
  fi
done
