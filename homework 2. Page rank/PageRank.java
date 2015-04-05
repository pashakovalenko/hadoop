package org.myorg;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class PageRank {
    
    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, LongWritable, Text> {
        public void map(LongWritable key, Text value, OutputCollector<LongWritable, Text> output, Reporter reporter) throws IOException {
            for (String str : value.toString().split("\n")) {
                String[] x = str.split("\t");
                int len = x[2].length();
                if (len > 2) {
                    String[] arr = x[2].substring(1, len - 1).split(",");
                    double w = Double.parseDouble(x[1]) / arr.length;
                    for (String k : arr) {
                        output.collect(new LongWritable(Integer.parseInt(k)), new Text(String.format("1\t%.15f", w)));
                    }
                    output.collect(new LongWritable(Integer.parseInt(x[0])), new Text("2\t" + x[2]));
                }
            }
        }
    }

    public static class Reduce extends MapReduceBase implements Reducer<LongWritable, Text, LongWritable, Text> {
        double D = 0.85;
        public void reduce(LongWritable key, Iterator<Text> values, OutputCollector<LongWritable, Text> output, Reporter reporter) throws IOException {
            HashMap<String, Integer> a = new HashMap<String, Integer>();
            double w = 1 - D;
            String list = "[]";
            while (values.hasNext()) {
                String[] x = values.next().toString().split("\t");
                if (x[0].equals("1")) {
                    w += Double.parseDouble(x[1]) * D;
                } else {
                    list = x[1];
                }
            }
            output.collect(key, new Text(String.format("%.15f\t%s", w, list)));
        }
    }
    
    public static void main(String[] args) throws Exception {
        JobConf conf = new JobConf(PageRank.class);
        conf.setJobName("pagerank_java");
        
        conf.setMapOutputKeyClass(LongWritable.class);
        conf.setMapOutputValueClass(Text.class);
        conf.setOutputKeyClass(LongWritable.class);
        conf.setOutputValueClass(Text.class);
        
        conf.setMapperClass(Map.class);
        conf.setReducerClass(Reduce.class);
        
        conf.setInputFormat(TextInputFormat.class);
        conf.setOutputFormat(TextOutputFormat.class);
        
        FileInputFormat.setInputPaths(conf, new Path("PageRank_Java_Input"));
        FileOutputFormat.setOutputPath(conf, new Path("PageRank_Java_Output"));
        
        JobClient.runJob(conf);
    }
}
