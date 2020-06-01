DOCKER_NETWORK = docker-hadoop_default
ENV_FILE = hadoop.env
current_branch := $(shell git rev-parse --abbrev-ref HEAD)
serv:
	docker-compose up -d
run:
	docker exec namenode bash -c "/hadoop/jobs/run.sh $(mp) $(input) $(output)"
check:
	docker exec namenode bash -c "/opt/hadoop-3.2.1/bin/hadoop fs -cat /foo/data/wordcount/$(file)/part-00000"
put:
	docker exec namenode bash -c "/opt/hadoop-3.2.1/bin/hadoop fs -put /hadoop/jobs/$(file) /foo/data/wordcount/"
init:
	docker exec namenode bash -c "apt update && apt install -y python"
	docker exec datanode bash -c "apt update && apt install -y python"
	docker exec resourcemanager bash -c "apt update && apt install -y python"
	docker exec nodemanager bash -c "apt update && apt install -y python"
	docker exec historyserver bash -c "apt update && apt install -y python"