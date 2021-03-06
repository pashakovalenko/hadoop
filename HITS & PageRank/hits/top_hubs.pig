diogen = LOAD 'hits/stage5/part-00000' USING PigStorage('\t') AS (pid:long, g1:chararray, g2:chararray, a:chararray, h:chararray);
urls = LOAD '/data/sites/lenta.ru/all/urls.txt' USING PigStorage('\t') AS (pid:long, name:chararray);
short = FOREACH diogen GENERATE pid, h;
data = JOIN short BY pid, urls BY pid;
sorted = ORDER data BY h DESC;
STORE sorted INTO 'hits/sorted_hubs/';
top = LIMIT sorted 30;
DUMP top;