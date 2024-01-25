#!/bin/bash

# rawvideo_datasetディレクトリ内の${クラス番号}_${動画番号}.MOVファイルを指定したコーデックでmp4に変換する
# ffmpeg -i ./illegal_2.MOV -c:v libx264 -c:a aac -strict experimental -b:a 192k -movflags faststart illegal_2.mp4

echo "Enter the class number: "
read class_num

echo "Enter the file number: "
read file_num

for file in rawvideo_dataset/*.MOV; do
  ffmpeg -i "$file" -c:v libx264 -c:a aac -strict experimental -b:a 192k -movflags faststart "rawvideo_dataset/${class_num}_${file_num}.mp4"
  ((file_num++))
done

# 元のMOVファイルを全て削除する
# rm rawvideo_dataset/*.MOV
