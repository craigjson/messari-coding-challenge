#!/bin/zsh
# run_eth.zsh
# runs ETL feed every 10 seconds
while true
do
  sleep 10
  echo "Running ETL Feed"
  curl -s "http://app:8000/feed/run_etl"
done
