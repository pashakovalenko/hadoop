#!/bin/sh
#Рекомендую запускать это примерно так:

NAME='1_1000'
#Может быть all, 1_10, 1_100, 1_1000

hadoop fs -rm -r search_out_${NAME}

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -file mapper.py reducer.py \
    -mapper 'python ./mapper.py' \
    -reducer 'python ./reducer.py' \
    -input /data/sites/lenta.ru/${NAME}/docs-*.txt \
    -output search_out_${NAME}

rm -r search_out_${NAME}
mkdir search_out_${NAME}

hadoop fs -get ./search_out_${NAME}/* ./search_out_${NAME}

mkdir urls

hadoop fs -get /data/sites/lenta.ru/${NAME}/urls.txt ./urls/urls_${NAME}.txt

mkdir index_${NAME}

cat search_out_${NAME}/part-* | python build.py ./index_${NAME}/ simple9
#Может быть simple9 или fibonacci

python finder.py index_${NAME}/index.txt index_${NAME}/index.bin urls/urls_${NAME}.txt

#Теперь можно писать запросы. Поддерживаются ключевые слова and, or, and not, и, или, и не
#Два написанных подряд слова считаются соединенными "и": "белый дом" == "белый и дом"
#Также можно делать невложенные скобки
