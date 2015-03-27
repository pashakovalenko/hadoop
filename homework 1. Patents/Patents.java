package org.myorg;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class Patents {
    
    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
        private Text val = new Text();
        private Text year = new Text();
        
        public void map(LongWritable key, Text value, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
            for (String str : value.toString().split("\n")) {
            	if (str.charAt(0) != '"') {
                	String[] input = str.split(",");
                    val.set(input[4]);
                    year.set(input[1]);
                    output.collect(year, val);
                }
            }
        }
    }

    public static class Reduce extends MapReduceBase implements Reducer<Text, Text, Text, Text> {
        public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {
            HashMap<String, Integer> a = new HashMap<String, Integer>();
            while (values.hasNext()) {
                String[] vl = values.next().toString().split("\t");
                if (a.containsKey(vl[0])) {
                    a.put(vl[0], (int)a.get(vl[0]) + 1);
                } else {
                    a.put(vl[0], 1);
                }
            }
            Integer[] val = a.values().toArray(new Integer[a.size()]);
            Arrays.sort(val);
            int m = val[val.length / 2];
            double s = 0, d = 0;
            for (int i : val) {
                s += i;
                d += (double)i * i ;
            }
            s /= val.length;
            d = Math.sqrt(d / val.length - s * s);
            String result = String.format("%d\t%d\t%d\t%d\t%f\t%f", val.length, val[0], m, val[val.length - 1], s, d);
            output.collect(key, new Text(result));
        }
    }
    
    public static void main(String[] args) throws Exception {
        JobConf conf = new JobConf(Patents.class);
        conf.setJobName("patents");
        
        conf.setMapOutputKeyClass(Text.class);
        conf.setMapOutputValueClass(Text.class);
        conf.setOutputKeyClass(Text.class);
        conf.setOutputValueClass(Text.class);
        
        conf.setMapperClass(Map.class);
        conf.setReducerClass(Reduce.class);
        
        conf.setInputFormat(TextInputFormat.class);
        conf.setOutputFormat(TextOutputFormat.class);
        
        FileInputFormat.setInputPaths(conf, new Path("/data/patents/apat63_99.txt"));
        FileOutputFormat.setOutputPath(conf, new Path("patents_java"));
        
        JobClient.runJob(conf);
    }
}
