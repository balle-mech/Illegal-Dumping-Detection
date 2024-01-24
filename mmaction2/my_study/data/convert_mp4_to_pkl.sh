#!/bin/bash

echo "Enter the class number: "
read class_num

echo "Enter the starting video number: "
read start_num

# Set the directory path
directory="../../"
# Change to the directory
cd "$directory" || exit
pwd

# rawvideo_datasetディレクトリ内の${クラス番号}_${train}_${動画番号}.mp4ファイルを指定したコーデックでpklに変換する
# python ../my_study/ntu_pose_extraction.py ./rawvideo_dataset/${クラス番号}_${train}_${動画番号}.mp4 ./pkl_dataset/${train}/${クラス番号}_${train}_${動画番号}.pkl --skip-postproc

for filepath in $(ls -1 my_study/data/rawvideo_dataset/${class_num}_*.mp4 | sort -V); do
  file=$(basename $filepath)
  # echo $file
  # .mp4を削除して、代わりに.pklを追加する
  data_type=$(echo $file | cut -d '_' -f 2)
  new_name=${file%.mp4}.pkl
  # echo data_type: ${data_type}
  # echo new_name: $new_name

  video_num=$(echo $file | cut -d '_' -f 3 | cut -d '.' -f 1)
  # if [[ $video_num -ge $start_num ]]; then
  if [[ $data_type -ge 'val' ]]; then
    echo pkl_dataset/${data_type}/${new_name}を作成しようとしています。
    python my_study/ntu_pose_extraction.py "$filepath" "./my_study/data/pkl_dataset/${data_type}/${new_name}" --skip-postproc
    ((count++))
    echo pkl_dataset/${data_type}/${new_name}を作成しました
  fi
done
