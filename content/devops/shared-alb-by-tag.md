Title: AWS Shared ALB by EC2 instance tag
Date: 2021-02-15 08:00
Tags: aws, lambda, python, alb, automation
slug: shared-alb-by-tag

### motivation

in AWS setups, loadbalancers can be are quite cost-intensive.     
If you are in a non-production environment, you probably do not need one LB for each (micro-)service.    
This lambda function automatically adds ec2 instances to a targetgroup & adds a host-header-based rule to a single shared ALB

#### source 

the sources, documentation and examples are located [here](https://github.com/k11h-de/aws-lambda/tree/main/shared-alb-by-tag){:target="_blank"}