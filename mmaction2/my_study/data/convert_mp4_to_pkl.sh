#!/bin/bash

echo "Enter the class number: "
read class_num

# echo "Enter the starting video number: "
# read start_num

# echo "Enter the data type (train or val): "
# read data_type

echo "変換元のmp4ファイルが入っているディレクトリ/mmaction2以降を指定 ex: my_study/data/rawvideo_dataset"
read directory_original

echo "変換後のpklファイルを保存するディレクトリ/mmaction2以降を指定 ex: my_study/data/pkl_dataset"
read directory_converted

# Change to the mmaction2 directory
directory="../../"
cd "$directory" || exit

# train_test_split済みのデータセットを用いる場合のコマンド
# (${クラス番号}_${train}_${動画番号}.mp4ファイルをpklに変換する。）
# `python ../my_study/ntu_pose_extraction.py ./rawvideo_dataset/${クラス番号}_${train}_${動画番号}.mp4 ./pkl_dataset/${train}/${クラス番号}_${train}_${動画番号}.pkl --skip-postproc`
# for filepath in $(ls -1 ${directory_original}/${class_num}_${data_type}_*.mp4 | sort -V); do
#   file_name=$(basename $filepath)
#   # .mp4を削除して、代わりに.pklを追加する
#   new_name=${file_name%.mp4}.pkl

#   video_num=$(echo $file_name | rev | cut -d '_' -f 1 | rev | cut -d '.' -f 1)
#   if [[ $video_num -ge $start_num ]]; then
#     echo pkl_dataset/${data_type}/${new_name}を作成しようとしています。
#     python my_study/ntu_pose_extraction.py "$filepath" "./my_study/data/pkl_dataset/${data_type}/${new_name}" --skip-postproc
#     ((count++))
#     echo pkl_dataset/${data_type}/${new_name}を作成しました
#   fi
# done


# train_test_splitしていないデータセットを用いる場合のコマンド
# (${クラス番号}_${動画番号}.mp4ファイルをpklに変換する。）
for filepath in $(ls -1 ${directory_original}/${class_num}_*.mp4 | sort -V); do
  file_name=$(basename $filepath)
  # .mp4を削除して、代わりに.pklを追加する
  new_name=${file_name%.mp4}.pkl

  echo pkl_dataset/${new_name}を作成しようとしています。
  python my_study/ntu_pose_extraction.py "$filepath" "${directory_converted}/${new_name}" --skip-postproc
  echo pkl_dataset/${new_name}を作成しました。
done
