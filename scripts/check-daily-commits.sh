#!/bin/bash
# Scheduled to run at 00:00, therefore checking "yesterdays" date.

last_commit_date=$(git log -1 --format=%as)
current_date=$(date -d 'yesterday' +'%Y-%m-%d')

readme_path='./README.md'

current_streak_s='Current_streak-'
reset_string="${current_streak_s}0"

if [ "$last_commit_date" != "$current_date" ]; then
    echo 'No commits found yesterday.'
    if grep -q $reset_string "$readme_path"; then
        echo 'Streak already reset, exiting.'
        exit 0
    fi
    echo 'Resetting streak.'
    sed -i "s/${current_streak_s}[1-9][0-9]*/$reset_string/" $readme_path
fi