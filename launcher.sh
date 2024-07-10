#!/bin/bash


current_dir="$(pwd)"
current_dir_escaped=$(echo "$current_dir" | sed 's/ /\\040/g')
echo $current_dir_escaped
python3 $current_dir_escaped/desktopAppCreator.py
