## https://docs.kafka-ui.provectus.io/development/building/without-docker

java -Dspring.config.additional-location=kafkaui/kafka-ui-api/src/main/resources/application-local.yml -jar kafka-ui-api-v0.7.1.jar 


## https://github.com/obsidiandynamics/kafdrop/releases/download/4.0.1/kafdrop-4.0.1.jar


# cd  /Users/binaysahoo/workspace/apachesoft/kafka/kafka/3.7.0/libexec


# generate a ClusterUUID
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"


# Format Log Directories

bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties


(base) binaysahoo@binays-Mac-mini libexec % bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
metaPropertiesEnsemble=MetaPropertiesEnsemble(metadataLogDir=Optional.empty, dirs={/opt/homebrew/var/lib/kraft-combined-logs: EMPTY})
Formatting /opt/homebrew/var/lib/kraft-combined-logs with metadata.version 3.7-IV4.


# start
bin/kafka-server-start.sh config/kraft/server.properties


# crate topic to store event
(base) binaysahoo@binays-Mac-mini libexec % bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
Created topic quickstart-events.
(base) binaysahoo@binays-Mac-mini libexec % 


(base) binaysahoo@binays-Mac-mini libexec % bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
Topic: quickstart-events	TopicId: 8DcPvVUHRi2hlSEHqk5jyQ	PartitionCount: 1	ReplicationFactor: 1	Configs: segment.bytes=1073741824
	Topic: quickstart-events	Partition: 0	Leader: 1	Replicas: 1	Isr: 1
(base) binaysahoo@binays-Mac-mini libexec % 


# write some event 
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
This is my first event
This is my second event

# read the message and events
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
This is my first event
This is my second event

