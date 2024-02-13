### http://events17.linuxfoundation.org/events/archive/2017/mesoscon-europe/program/slides

##  https://mesosphere.github.io/marathon/

## https://www.nextplatform.com/2015/04/21/teaching-grid-engine-to-speak-mesos/ 

https://blog.griddynamics.com/more-details-on-building-cloud-portable-devops-stack-with-mesos-and-marathon/

## https://kb.iu.edu/d/avmy    - TORQUE MPI (message passing interface)

# like qsub , qdel , qstat , showq    - --- is it similar to UGE or LSF?

## https://docs.adaptivecomputing.com/torque/4-0-2/help.htm#topics/2-jobs/submittingManagingJobs.htm 

## https://slurm.schedmd.com/quickstart.html

## https://openpbs.org/ 

## https://slurm.schedmd.com/mpi_guide.html#intel_mpirun_hydra 

## apache messos

Extendable architecture via support for pluggable frameworks. The true power of Mesos as a platform comes with extendable architecture that allows additional features to be delivered via pluggable “frameworks.” Examples of features delivered by the pluggable framework include support for long-running services, batch scheduling, big data processing and data storage. Marathon is one such framework. Many frameworks already exist for common use cases, and it’s fairly easy to add a custom one if needed:
Aurora, Marathon, and Singularity for long-running tasks support,
Chronos, Jenkins, and JobServer for batch processing,
Hadoop, MPI, Spark, and Storm for big data processing,
ElasticSearch, Hypertable, MrRedis for data storage


In the previous blog post we explained our overall approach to the DevOps stack used for the deployment and management of the In-Stream Processing blueprint. In this post we’ll focus on more details of Mesos and Marathon, and provide you with scripts to provision the complete computational environment on any cloud of your choice. 

The advantage of Docker containers over configuration management tools for DevOps operations:

Let’s quickly recap, once again, why the Docker-based DevOps stack is better than traditional configuration management tools.

Docker-based application deployment solutions represent the second-generation approach to DevOps. The traditional first-generation approach was based on configuration management tools such as Chef, Puppet, Ansible, and SaltStack. These tools share the same core idea: to provide a layer of abstraction above the OS in order to simplify routine operations and deliver, more or less, application portability across different operating environments. Their deployment scripts can run on different environments, and produce the required application configurations with little or no modification. 

This approach worked well in most cases — but not without limitations, such as:

Cloud portability. The “write once, deploy everywhere” promise has not been fully realized with configuration management tools. The differences between cloud vendors in operating systems, image management, and networking infrastructure, to mention just a few big items, has made all VM-based deployments non-portable between major cloud platforms.
A reliable “write once, run everyone” application deployment across all CI environments in the release pipeline, from a developer’s laptop to production infrastructure, has proven hard to achieve.
Rapid provisioning of new VMs to address application scenarios like scaling or failover is not addressed. These scenarios require changes to the infrastructure footprint, but the logic of provisioning new VMs must be handled outside of configuration management tooling.
A heavy-duty re-configuration cycle is required to execute most changes — such as verifying base dependencies in Java, checking application server configuration, etc.— which is time-consuming. It is not uncommon for a complete application deployment to take 30-60 minutes to build or upgrade.
Introduces notable run time overhead on the operational infrastructure required to run configuration management scripts on every VM, all the time
Containers are rapidly gaining momentum because they take the “build once, run everywhere” promise to the next level, and provide significantly lighter-weight application virtualization. Effectively, they do for process management what Java did for application management. We can now package all the dependencies between an application and its underlying operating system into a container that can be reused all the way from developer workstation to production infrastructure.

Advantages of container-based DevOps:
 Container (not VM) as a standard unit of deployment across the board
 Container-based application infrastructure is abstracted out from cloud vendor-specific differences in the infrastructure and its APIs.
Lightweight virtualization of containers saves resources leading to better utilization of the underlying infrastructure
Dynamic spin-up and down of new containers in seconds delivers on the promise of dynamic environments and easily-supported use cases like scaling, blue-green upgrades, disaster recoveries, and failover.
DevOps automation can now originate on developer workstations and end up all the way in production within a seamless CICD pipeline
Using Mesos/Marathon as a DevOps foundation for Docker 
 

Docker logo

Let’s review the container-centric DevOps stack we are using for deployment and management of our in-Stream Processing platform.

Mesos, the distributed kernel for resource management
Mesos has a number of outstanding features that makes it one of the best modern choices as a container management platform.

Turning a fleet of VMs into source management fabrics. Mesos takes a fleet of VMs and manages their collective resources to host applications. Mesos is our kernel sources manager - it keeps track on all of them, allocates resources when requested (cpu, ram, disk), and makes sure the load is spread evenly if possible in order to avoid bottlenecks.
Mesos is the cluster resource manager which spans across all available resources and manages them as a whole.
Extendable architecture via support for pluggable frameworks. The true power of Mesos as a platform comes with extendable architecture that allows additional features to be delivered via pluggable “frameworks.” Examples of features delivered by the pluggable framework include support for long-running services, batch scheduling, big data processing and data storage. Marathon is one such framework. Many frameworks already exist for common use cases, and it’s fairly easy to add a custom one if needed:
Aurora, Marathon, and Singularity for long-running tasks support,
Chronos, Jenkins, and JobServer for batch processing,
Hadoop, MPI, Spark, and Storm for big data processing,
ElasticSearch, Hypertable, MrRedis for data storage
An example frameworks variety for Mesos 

Scalability. “Above normal” ability to scale is one of the key success factors for Mesos. A key contributing factor here is the two-layer scheduler design which keeps the core system scheduler very lightweight and delegates framework-related scheduling duties to the framework’s scheduler. Also, as an additional feature of this design, this keeps the Mesos master from being the system’s the performance bottleneck. This paper provides a good overview of the Mezos scheduling mechanism as well as some test numbers: <4% overhead for Mesos itself and scalability up to 50000 slaves.
Maturity. Mesos is almost 10 years old and is used by industry giants including Twitter, Uber, eBay, and Yelp, plus it has an active and supportive user community, something we look for in all open source projects we recommend.
The advantage of Docker containers over configuration management tools for DevOps operations
Mesos design is based on the following principles:
A group of master nodes take care of the overall coordination of all activities on the managed nodes
These master node clusters rely on synchronized, distributed record systems such as Zookeeper or Etcd
Each managed node has a Mesos-slave process that makes its resources available to the common pool.
A typical deployment topology of Mesos master nodes and managed nodes looks like this:

Typical deployment topology for Mesos cluster 

Marathon, the process manager framework for Mesos

Basic Mesos features permit resource allocation out of the VM fabrics to a specific task, like running a Docker container, but Mesos does not itself handle that. The role of process management is delivered via the framework, in our case, Marathon.

Marathon is one of the most commonly used Mesos frameworks that provides the following standard capabilities:

 Manages long-running processes or services on Mesos managed nodes.
Allows configuration for up/down scaling and other workload-spreading strategies
Provides integrated basic health checks (tcp, http, shell scripts)
Offers convenient REST API
 … and you can even try it out in the debugging mode locally!
Mesos and Marathon in action (illustrations below)
Mesos and 2 its most popular frameworks - Chronos and Marathon. In the analogy of "single giant machine" Chronos will represent scheduler, Marathon - process manager.  

Continuous Delivery Blueprint by Max Martynov and Krill Evstigneev
Mesos and 2 its most popular frameworks - Chronos and Marathon. In the analogy of "single giant machine" Chronos will represent scheduler, Marathon - process manager. Marathon can run pretty much anything, including native support for Docker containers.

We need more features!
We can have a perfectly fine working setup with a “plainvanilla” installation of Mesos and Marathon, but some features can provide additional functionality. Here are a few we found useful in our  reference architecture:

Node labeling. What if you have a non-heterogeneous underlying infrastructure and want to distinguish between nodes with specializations, such as compute nodes vs. storage nodes? Or you need to combine a group of nodes that share fast interconnects for deployment of certain applications? Tag them with labels
 Distribution strategies - node constraints. This feature allows to manipulate the way applications are spread across your fleet. Most typical scenario here is making sure that your DB servers, for example, are not sitting on one physical machine.
Combine labels with constraints. — our DB will use faster storage and your calculations will be done on the fastest CPU cores.
Persistent volumes. This feature name speaks for itself. It’s not a big deal if your setup assumes separate datastore facilities, but it could be a nasty surprise to learn that your database just disappeared because its container had to be restarted. There are several possible options, but we will stick to the “plain vanilla” one in order to keep the list of tools as short as possible.
Since the “Persistent volumes” feature is still shown as “experimental,” it needs to be explicitly enabled. (The official documentation is a big help here.)

Here's how to deploy Mesos/Marathon on any cloud
As we described in some detail in the previous post, we will use Ansible to deploy Mesos and Marathon on a collection of VMs, some of which will be used as Master nodes and the rest as a resource pool.

The process is very simple and straightforward, requiring only a minimal learning curve. Here is a quick-start guide on how to do it: 

 Ansible code is published here
After it is checked out, edit the hosts file and fill it with addresses of your cluster-to-be
Run Ansible playbook: ansible-playbook -i ./hosts mesos-cluster.yml
Wait 10-15 minutes and you are good to go!
For super-quick learning, you can spin up the complete environment right on your workstation, in which case no additional cloud infrastructure will be required until you are ready to scale your cluster.

-----
Now you know the basics of setting up Mesos and Marathon as a DevOps foundation for Docker, and you have scripts you can install on your workstation (or wherever) to get some hands-on experience with them. If you you have any questions, Grid Dynamics is happy to help. Please email and we’ll get back to you shortly. And don’t forget to subscribe to our blog. We have lots more useful information about Mesos, Marathon, Docker, DevOps, and other interesting topics coming up.

Links
We will continue to cover technology behind the scene of our project deeper in next posts, however here are some links if you want to know more:

Mesos
Docker
Swarm
kubernetes
Marathon
Persistent volumes in marathon
Advanced persistence - rexray
Software projects built on Mesos
Mesos architecture
Digging deeper into Apache Mesos
Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center
