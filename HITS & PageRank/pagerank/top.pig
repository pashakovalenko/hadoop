diogen = LOAD 'pagerank/stage5/part-00000' USING PigStorage('\t') AS (pid:long, val:float);
urls = LOAD '/data/sites/lenta.ru/all/urls.txt' USING PigStorage('\t') AS (pid:long, name:chararray);
data = JOIN diogen BY pid, urls BY pid;
sorted = ORDER data BY val DESC;
STORE sorted INTO 'pagerank/sorted/';
top = LIMIT sorted 30;
DUMP top;