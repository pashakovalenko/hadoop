#!/bin/sh
hadoop fs -rm -r hits/stage0/

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -file mapper0.py reducer0.py \
    -mapper 'python ./mapper0.py' \
    -reducer 'python ./reducer0.py' \
    -input /data/sites/lenta.ru/all/* \
    -output hits/stage0/

hadoop fs -rm -r hits/stage00/

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -file mapper1.py reducer1.py \
    -mapper 'python ./mapper1.py' \
    -reducer 'python ./reducer1.py' \
    -input hits/stage0/* \
    -output hits/stage00/

#hadoop fs -rm -r hits/stage0/

OUT='hits/stage00/'

for ((i=1;i<=5;i++))
do
    IN=${OUT}
    OUT='hits/stage'${i}
    
    hadoop fs -rm -r ${OUT}
    
    hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file mapper.py reducer.py \
        -mapper 'python mapper.py' \
        -reducer 'python reducer.py' \
        -input ${IN} \
        -output ${OUT}

    #hadoop fs -rm -r ${IN}

done
