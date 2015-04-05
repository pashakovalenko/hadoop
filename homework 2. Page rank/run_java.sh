#!/bin/sh
hadoop fs -rm -r PageRank_Java_Output
javac -d ./classes/ PageRank_Prepare.java
jar -cvf pagerank_prepare.jar -C ./classes/ ./
hadoop jar pagerank_prepare.jar org.myorg.PageRank_Prepare

for ((i=1;i<=30;i++))
do
	hadoop fs -rm PageRank_Java_Input/*
	hadoop fs -mv PageRank_Java_Output/* PageRank_Java_Input/

	hadoop fs -rm -r PageRank_Java_Output
	javac -d ./classes/ PageRank.java
	jar -cvf pagerank.jar -C ./classes/ ./
	hadoop jar pagerank.jar org.myorg.PageRank
	echo 'Step '${i}
done
