#!/bin/sh
hadoop fs -rm -r patents_python

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -file mapper.py reducer.py \
    -mapper 'python ./mapper.py' \
    -reducer 'python ./reducer.py' \
    -input /data/patents/apat63_99.txt \
    -output patents_python

hadoop fs -text ./patents_python/part*