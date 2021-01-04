#!/bin/bash

streamlit run app.py &

for (( ; ; ))
do
   echo $(date -u) > lastrun.txt
   python get_data.py
   sleep 60s
done


