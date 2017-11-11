Open Edge Core a software which is installed on edge nodes to enable the Open Edge platform

# Introduction
Open Edge is a edge computing platform which is describled in our pater (TODO: insert paper). In this platform, an edge node is simply a computer that has Open Edge Core installed and running. With Open Edge Core, a edge node can:
- Singlely or collaboratedly form a group of nodes called Open Edge platform
- Provide interface (command line and API access) to users to interact with Open Edge platform

## Open Edge Platform
Open Edge platform is a group of one or more edge nodes that provides lambda runtime. Not only being able to host, execute, and manage lambda functions, these nodes can collaborate to provide offloading.

## Lambda run time
A run time for lambda computing model. Currently, this run time leverages Docker containers to execute lambda functions. Other virtualization tech like LightVM is also being examined. This is why I don't reuse some other open lambda implementations. 

The programing model (how to write a lambda function and provide associated dependencies) for this lambda run time follows AWS Lambda, but compatibility is not guaranteed.

# Usage
## Function
Open Edge's function's programming model is similar to AWS Lambda function's: a function takes a special context object as the first parameter, followed by other optional paramenters. Using the context object, users can interact with Open Edge.

### How to write functions
A task consists of a function handler and its configuration.

### How to upload functions

### How to trigger functions

## Edge Group
A edge group is a group of node that contains one master node and (optional) worker nodes. Master node is the node users has direct access to its cli, and workers are nodes to which master offloads computing tasks to. 

Master and workers are just regular open edge nodes: any node can be master and any node can be worker. To form a edge computing group, users just need to add workers to the current node:

`openedge worker add <ip_address`

A master is also counted as a worker as it can offloading computing tasks to itself. So if you have only one node, you can think it's a edge group with one 'hidden' worker.


