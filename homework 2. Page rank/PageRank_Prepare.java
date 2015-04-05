package org.myorg;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class PageRank_Prepare {
    
    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, LongWritable, Text> {
        private LongWritable art = new LongWritable();
        private Text cit = new Text();
        
        public void map(LongWritable key, Text value, OutputCollector<LongWritable, Text> output, Reporter reporter) throws IOException {
            for (String str : value.toString().split("\n")) {
            	if (str.charAt(0) != '"') {
                	String[] input = str.split(",");
                    art.set(Integer.parseInt(input[0]));
                    cit.set(input[1]);
                    output.collect(art, cit);
                }
            }
        }
    }

    public static class Reduce extends MapReduceBase implements Reducer<LongWritable, Text, LongWritable, Text> {
        public void reduce(LongWritable key, Iterator<Text> values, OutputCollector<LongWritable, Text> output, Reporter reporter) throws IOException {
            String res = "";
            while (values.hasNext()) {
                if (res != "") {
                    res += ",";
                } 
                res += values.next().toString();
            }
            String result = String.format("%.15f\t[%s]", 0.15, res);
            output.collect(key, new Text(result));
        }
    }
    
    public static void main(String[] args) throws Exception {
        JobConf conf = new JobConf(PageRank_Prepare.class);
        conf.setJobName("pagerank-prep");
        
        conf.setMapOutputKeyClass(LongWritable.class);
        conf.setMapOutputValueClass(Text.class);
        conf.setOutputKeyClass(LongWritable.class);
        conf.setOutputValueClass(Text.class);
        
        conf.setMapperClass(Map.class);
        conf.setReducerClass(Reduce.class);
        
        conf.setInputFormat(TextInputFormat.class);
        conf.setOutputFormat(TextOutputFormat.class);
        
        FileInputFormat.setInputPaths(conf, new Path("/data/patents/cite75_99.txt"));
        FileOutputFormat.setOutputPath(conf, new Path("PageRank_Java_Output"));
        
        JobClient.runJob(conf);
    }
}
