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


#### kafdrop

## java --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -jar kafdrop-4.0.1.jar --kafka.brokerConnect=localhost:9092 --server.port=9000

2024-03-13 20:40:18.700  INFO 27546 [kground-preinit] o.h.v.i.u.Version                        : HV000001: Hibernate Validator 8.0.1.Final
2024-03-13 20:40:18.728  INFO 27546 [           main] o.s.b.StartupInfoLogger                  : Starting Kafdrop v4.0.1 using Java 20.0.1 with PID 27546 (/Users/binaysahoo/workspace/apachesoft/kafka/kafdrop/kafdrop-4.0.1.jar started by binaysahoo in /Users/binaysahoo/workspace/apachesoft/kafka/kafdrop)
2024-03-13 20:40:18.730  INFO 27546 [           main] o.s.b.SpringApplication                  : No active profile set, falling back to 1 default profile: "default"
2024-03-13 20:40:19.774  INFO 27546 [           main] i.u.s.s.ServletContextImpl               : Initializing Spring embedded WebApplicationContext
2024-03-13 20:40:19.775  INFO 27546 [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1021 ms
2024-03-13 20:40:19.877  INFO 27546 [           main] k.c.KafkaConfiguration                   : Checking truststore file kafka.truststore.jks
2024-03-13 20:40:19.878  INFO 27546 [           main] k.c.KafkaConfiguration                   : Checking keystore file kafka.keystore.jks
2024-03-13 20:40:19.878  INFO 27546 [           main] k.c.KafkaConfiguration                   : Checking properties file kafka.properties
2024-03-13 20:40:19.919  INFO 27546 [           main] k.c.KafkaConfiguration                   : Checking truststore file kafka.truststore.jks
2024-03-13 20:40:19.919  INFO 27546 [           main] k.c.KafkaConfiguration                   : Checking keystore file kafka.keystore.jks
2024-03-13 20:40:19.920  INFO 27546 [           main] k.c.KafkaConfiguration                   : Checking properties file kafka.properties
2024-03-13 20:40:19.937  INFO 27546 [           main] k.s.BuildInfo                            : Kafdrop version: 4.0.1, build time: 2023-11-02T13:01:08.419Z
2024-03-13 20:40:20.471  INFO 27546 [           main] o.s.b.a.e.w.EndpointLinksResolver        : Exposing 13 endpoint(s) beneath base path '/actuator'
2024-03-13 20:40:20.509  INFO 27546 [           main] i.u.Undertow                             : starting server: Undertow - 2.3.8.Final
2024-03-13 20:40:20.515  INFO 27546 [           main] o.x.Xnio                                 : XNIO version 3.8.8.Final
2024-03-13 20:40:20.520  INFO 27546 [           main] o.x.n.NioXnio                            : XNIO NIO Implementation Version 3.8.8.Final
2024-03-13 20:40:20.535  INFO 27546 [           main] o.j.t.Version                            : JBoss Threads version 3.5.0.Final
2024-03-13 20:40:20.556  INFO 27546 [           main] o.s.b.w.e.u.UndertowWebServer            : Undertow started on port(s) 9000 (http)
2024-03-13 20:40:20.570  INFO 27546 [           main] o.s.b.StartupInfoLogger                  : Started Kafdrop in 2.045 seconds (process running for 2.528)


