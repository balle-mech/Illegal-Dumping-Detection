#!/bin/bash

# rawvideo_datasetディレクトリ内の${クラス番号}_${動画番号}.MOVファイルを指定したコーデックでmp4に変換する
# ffmpeg -i ./illegal_2.MOV -c:v libx264 -c:a aac -strict experimental -b:a 192k -movflags faststart illegal_2.mp4

# 変換元のMOVファイルが入っているディレクトリを指定
directory_original="../rasp_cam/raw_video"
# 変換後のmp4ファイルを保存するディレクトリを指定
directory_converted="../rasp_cam/mp4_video"

# echo "Enter the class number: "
# read class_num

echo "mov or MOV?"
read mov_or_MOV

for file in ${directory_original}/*.${mov_or_MOV}; do
  # 拡張子を取り除いたファイル名を取得
  new_file_name=${file%.${mov_or_MOV}}.mp4
  ffmpeg -i "$file" -c:v libx264 -c:a aac -strict experimental -b:a 192k -movflags faststart "${directory_converted}/${new_file_name}"
  echo "${file}を${directory_converted}/${new_file_name}に変換しました"
done

# 元のMOVファイルを全て削除する
# rm rawvideo_dataset/*.MOV
