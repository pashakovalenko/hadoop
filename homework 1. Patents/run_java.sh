#!/bin/sh
hadoop fs -rm -r patents_java

javac -d ./classes/ Patents.java

jar -cvf patents.jar -C ./classes/ ./

hadoop jar patents.jar org.myorg.Patents

hadoop fs -text ./patents_java/part*