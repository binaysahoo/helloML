# https://www.bsc.es/support/LSF/9.1.2/ 


## https://www.ibm.com/docs/en/slac/10.2.0?topic=jobs-get-basic-job-information-get


Description
URL

scheme://domain:port/platform/ws/jobs

Description

By default, gets basic information for all jobs in all states submitted by the logged in user. Includes jobs with the status DONE and EXIT that have finished recently within the interval specified by CLEAN_PERIOD in the LSF configuration file lsb.params.

The logged on user must be have the cluster administrator role to retrieve information about jobs submitted by other users.

HTTP Method

GET

Parameters

Name	Description
 	
jobname

Optional.

Gets basic information about jobs that have the specified job name.

The job name can be up to 4094 characters long. Job names are not unique.

You can use the wildcard character (*) anywhere within a job name. For example, job* returns jobA, jobB, jobC, and so on.

 	
username

Optional.

If user name is not specified, gets information about jobs submitted by the logged in user.

OS user name or LSF user group name. You must be logged on as a cluster administrator or group administrator to use this parameter.

Gets basic information about jobs submitted by the specified user, or jobs submitted by users belonging to the specified LSF user group.

Use the keyword all to return jobs and basic job information for jobs submitted by all users.

To specify a windows user name, use the format DOMAIN_NAME\\user_name. For example: mydomain\\user1.

To get a list of users, use the API /platform/ws/users.

To get a list of user groups, use the API /platform/ws/usergroups.

 	
queuename

Optional.

Returns information about jobs in the specified queue.

To get a list of queues, use the API /platform/ws/queues.

 	
hostname

Optional. Gets basic information about jobs that have been dispatched to the specified host, jobs that have been dispatched to all hosts in the specified host group, or jobs that have been dispatched to all hosts in the specified cluster.

To get a list of hosts, use the API /platform/ws/hosts.

To get a list of host groups, use the API /platform/ws/hostgroups.

To get the local cluster name, use the API /platform/ws/clusters/local.

 	
status

Optional. Gets basic information about jobs with the specified job status.

If status is not specified, gets information about jobs in all states.

Valid values:

ACTIVE: Gets basic information about jobs that have the LSF status PEND, RUN, PSUSP, USUSP, SSUSP.
PENDING: Gets basic information about jobs that have the LSF status PEND.
SUSPENDED: Get basic information about jobs that have the LSF status PSUSP, USUSP, SSUSP.
RUNNING: Gets basic information about jobs that have the LSF status RUN.
DONE: Gets basic information about jobs that have the LSF status DONE.
EXIT: Gets basic information about jobs that have the LSF status EXIT.
COMPLETE: Gets basic information about jobs with the LSF status DONE and EXIT that have finished recently(within the interval specified by CLEAN_PERIOD in the LSF configuration file lsb.params. The default is 1 hour).
 	
start

Optional.  The start index for job paging. Must be a positive integer.

If this parameter is not set, the default start number is 1.

For example, if there are 1024 jobs to return from LSF, and you set start to 20 and pagesize to 50, the API returns 50 jobs, and the first job of these 50 jobs is the twentieth job of all 50 jobs:

/platform/jobs?start=20&pagesize=50

 	
pagesize

Optional. Maximum number of jobs that are returned. Must be a positive integer.

If this parameter is not set, the default is to return all jobs
