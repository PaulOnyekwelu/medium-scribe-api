#!/usr/bin/env bash

countdown(){
  declare desc="A simple countdown"
  local seconds="${1}"
  local d=$(($(date +%s) + "${second}"))

  while [ "$d" -ge `date +%s` ]; do
    echo -ne "$(date -u --date @$(($d - `date +%s`)) +%H:%M:%S)\r"
    sleep 1
  done
  
}

# while true;do
#   echo -ne "$(date -u -r $((datenow - $(date +%s))) +%H:%M:%S)\n" 
#   sleep 1
# done

# while [ "$datenow" -ge `date +%s` ]; do
#   echo -ne "$(date -u --date @$(($datenow - `date +%s`)) +%H:%M:%S)\r"
#   sleep 1
# done