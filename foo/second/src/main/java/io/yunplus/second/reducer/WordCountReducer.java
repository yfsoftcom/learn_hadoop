package io.yunplus.second.reducer;

import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
	IntWritable result = new IntWritable();

	public void reduce(Text	k2, Iterable<IntWritable> v2s, Context context) throws IOException,InterruptedException {
		int sum = 0;
		for(IntWritable val:v2s) {
			sum += val.get();
		}
		result.set(sum);
		context.write(k2,result);
	}
}