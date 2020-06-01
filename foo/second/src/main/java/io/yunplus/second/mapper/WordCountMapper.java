package io.yunplus.second.mapper;

import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Mapper;

public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable>{

    IntWritable one = new IntWritable(1);
    Text word = new Text();
    
    @Override
    protected void map(LongWritable k1, Text v1, Context context) throws IOException,InterruptedException {
        String line = v1.toString();
        String[] words = line.split(" ");
        for(String w: words){
            word.set(w);
            context.write(word, one);
        }
        
    }
    
}