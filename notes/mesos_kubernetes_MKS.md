Apache Mesos is typically used as a standalone cluster manager, and Kubernetes is a separate container orchestration platform. However, if you want to run Apache Mesos on Kubernetes, there is an integration project called Mesos Kubernetes (MKS). MKS allows you to run Mesos tasks as Kubernetes pods.

Here's a simplified guide for setting up Mesos Master and Mesos Slaves using Kubernetes virtualization:
### https://github.com/mesosphere-backup/docker-containers/tree/master/mesos 
### Prerequisites:

1. Have Kubernetes installed on your machine or cluster.
2. Have `kubectl` configured to connect to your Kubernetes cluster.

### Steps:

#### 1. Deploy Mesos Master:

Create a Mesos Master deployment YAML file (e.g., `mesos-master.yaml`):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mesos-master
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mesos-master
  template:
    metadata:
      labels:
        app: mesos-master
    spec:
      containers:
      - name: mesos-master
        image: mesosphere/mesos-master:1.10.0
```

Deploy the Mesos Master:

```bash
kubectl apply -f mesos-master.yaml
```

#### 2. Deploy Mesos Slaves:

Create a Mesos Slave deployment YAML file (e.g., `mesos-slave.yaml`):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mesos-slave
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mesos-slave
  template:
    metadata:
      labels:
        app: mesos-slave
    spec:
      containers:
      - name: mesos-slave
        image: mesosphere/mesos-slave:1.10.0
```

Deploy the Mesos Slaves:

```bash
kubectl apply -f mesos-slave.yaml
```

#### 3. Expose Mesos Web UI:

Expose the Mesos web UI to access it externally. Create a service YAML file (e.g., `mesos-web-ui.yaml`):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mesos-web-ui
spec:
  selector:
    app: mesos-master
  ports:
    - protocol: TCP
      port: 5050
      targetPort: 5050
  type: LoadBalancer
```

Deploy the Mesos Web UI service:

```bash
kubectl apply -f mesos-web-ui.yaml
```

Now you can access the Mesos Web UI using the external IP of the service.

Note: This is a basic setup, and in a production environment, you would need to consider security, networking, and other aspects.

Keep in mind that Mesos and Kubernetes are two different paradigms for cluster management, and running them together may not be the most straightforward or common use case. It's recommended to thoroughly test and evaluate the compatibility and performance for your specific requirements.
