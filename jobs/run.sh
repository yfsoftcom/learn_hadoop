# /bin/sh

HADOOP_CMD="/opt/hadoop-3.2.1/bin/hadoop"

STREAM_JAR_PATH="/opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar"

INPUT_FILE_PATH_1="/foo/data/wordcount/$2"

OUTPUT_PATH="/foo/data/wordcount/$3"

PROGRAME_DIR="/hadoop/jobs"

$HADOOP_CMD fs -rm -r -skipTrash $OUTPUT_PATH

# Step 1.

$HADOOP_CMD jar $STREAM_JAR_PATH   \
-input $INPUT_FILE_PATH_1   \
-output $OUTPUT_PATH   \
-mapper $PROGRAME_DIR/$1/mapper.py   \
-file $PROGRAME_DIR/$1/mapper.py   \
-reducer $PROGRAME_DIR/$1/reducer.py  \
-file $PROGRAME_DIR/$1/reducer.py   \