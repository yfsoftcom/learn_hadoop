# learn hadoop in hard way

write mapperReducer with golang in hadoop

https://github.com/vistarmedia/gossamr

mooc -> https://www.imooc.com/video/20757


### hadoop docker-compose

https://github.com/big-data-europe/docker-hadoop



### hdfs commands

`$ hdfs dfs -ls /`

### submit mapperReducer

`$ `

### First Demo

https://songlee24.github.io/2015/07/29/mapreduce-word-count/

hadoop jar second-0.0.1-SNAPSHOT.jar io.yunplus.second.WordCount /data/foo/hello.txt /data/foo/out1.txt


### Python MapReduce

#### install python for each container
`$ apt update && apt install -y python`

#### test local
`$ cat hello.txt | python mp1/mapper.py | sort -k1,1 | python mp1/reducer.py`

#### run the script

- upload file `make put file=test.txt`
- run mapreduce `make run mp=mp1 input=test.txt output=test_out`
- checkout `make check file=test_out`