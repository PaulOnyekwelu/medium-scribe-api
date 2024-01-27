#!/usr/bin/env bash

countdown(){
  declare desc="A simple countdown"
  local seconds="${1}"
  local d=$(($(date +%s) + ${seconds}))

  while [ "$d" -ge `date +%s` ]; do
    # echo -ne "$(date -u --date @$(($d - `date +%s`)) +%H:%M:%S)\r"
    echo -ne "$(date -u -r $(($d - $(date +%s))) +%H:%M:%S)\n" 

    sleep 1
  done
  
}

countdown 200