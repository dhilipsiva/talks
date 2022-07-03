---
marp: true
theme: gaia
class:
  - lead
  - invert
---

# Introduction to DevOps

## Workshop @ New Horizon College 

## [@dhilipsiva](https://github.com/dhilipsiva)

---

## Vice President Of Engineering @ [Reckonsys](https://www.reckonsys.com/)

## Chief Technology Officer @ [Nitimis](https://nitimis.com/)

An Optimistic Nihilist who loves Science, Python, Rust, FOSS, e-Games, Fitness, Astrophysics & தமிழ்.  Jack of all trades & Master of none.

## [https://dhilipsiva.com](https://dhilipsiva.com)

## [dhilipsiva@pm.me](mailto:dhilipsiva@pm.me)

---

# I have no idea what I am talking about :stuck_out_tongue_winking_eye:

---

# What is DevOps?

## DEVelopment + OPerationS

Basically, taking a piece of working code and running it on a cloud server in a reliable, secure and scalable way 

---

# DevOps Sikllset 

* Linux OS (cmd, ssh, git, vim, etc)
* Cloud Computing: SaaS, IaaS & PaaS(AWS, GCP, Azure, DigitalOcean, Heroku, Netlify)
* Container Technologies (Docker, Kubernetes, Mesos, Nomad)
* IaaC (Terraform, Pulumi, AWS CDK)
* Deployment/Configuration tools (Fabric, Ansible, AWS CoPilot, Chef, Puppet)
* CI/CD Pipelines (GitHub Actions, Jenkins, Drone, CircleCI)
* Monitoring (APM, Logging) & Alerting (OpenTracing, Pormetheus, ELK, Google Stackdriver, CloudWatch, Datadog, New Relic)
* Bash (Shell) & Python/Ruby Scripting

---

# Bonus 

* Linux scripting & packaging
* Memory management, scheduling, filesystems, networking
* nginx, traefik, etc.
* RabbitMQ, Redis & Elasticsearch
* SQL, MySQL, Postgres, MongoDB
* AWS services - EC2, RDS, S3, Lambda, Cloudfront, ECR, ECS, EKS, IAM, DynamoDB, SNS, SQS, EMR, etc.
* Understanding of Networking, Load Balancers, HTTP/TCP proxies, High availability, k8s Ingress routers

---

# Roles associated with DevOps

* DevOps Engineer
* Site Reliability Engineer (SRE)
* Infrastructure Engineer

---

# Linux Command Line

* `~` is the current user's HOME directory `/home/username`
* `.` current and `..` parent directory
* `.hidden` files and directories
* syntax: `cmd argument1 [optional-argument2] --option1 --option-with-value some-value`
* `pwd` present working directory
* `ls` list files and directories 
* `cd` change directory

---

# Linux Command Line (contd.)

* `touch` create empty file
* `mkdir` make directory
* `rm` remove file[s]
* `rmdir` remove directory
* `cp` copy & `mv` move
* `man` manual
* `cat` conCATenate
* `{}` expand / shorthand

---

# RSA - public key cryptography

* `ssh-keygen -t rsa -b 4096`
* private key - super secret password like file
* public key - public file that can be shared with anyone and everyone
* passphraze - password
* `~/.ssh` directory

---

# SSH 

Secure Shell [remote terminal]

* `ssh username@host`
* `~/.ssh/authorized_keys`

---

# Git

https://docs.github.com/en/get-started/quickstart/hello-world

* `git clone` clone a repository
* `git pull` pull latest changes from remote
* `git push` push local changes to remote
* `git commit` commit changes
* `git merge` to merge the branches
* `git checkout` checkout / create branches
* `git reset` reset all changes
* `git stash` stash all changes 

---

# Vim - Text Editor

* Press `Esc` key to enter `NORMAL` (or `COMMAND`) mode. This is the default mode that the editor opens in. In this mode, you can execute commands
* Press `i` key to enter `INSERT` mode. In this mode, you can insert text. Press `Esc` to go backk to `NORMAL` mode
* Press `v` key to enter `VISUAL` mode. In this mode, you can selct text and do cut (`x`) / copy (`y` yank) / paste (`v`)
* In `NORMAL` mode: type `:w` to write; `:q` to quit; `:wq` to write and quit and `:wqa` to write and quit all

---

# Cloud Computing

Basically running code on a remote server

* Software as a Service (SaaS): Gmail, Google Drive, WhatsApp, Twitter
* Infrastrcture as Service (IaaS): AWS, DigitalOcean
* Platform as a Service (PaaS): Heroku, Netlify

---

# Digital Ocean

https://www.digitalocean.com/github-students

Let's explore some of the services that DO offers.

---

# Docker

Like virtual machine, but lightweight and without hardware emulation

### Demo

* Build a sample image
* Push it to DockerHub
* Let the students pull and run it
* Walk then through bigga

---

# IaaC 

Show a demo of using Terraform with DigitalOcean + Docker

---

# Deployment/Configuration tools 

Show a demo of using fabric to install & configure packages

---

# CI/CD Pipelines

Show a demo with GitHub actions

---

# Monitoring & Alerting

Show a demo of Sentry and uptrace.dev

---

# Thanks! :pray:

### https://github.com/dhilipsiva/talks

This copy is released under the [MIT License](https://github.com/dhilipsiva/talks/blob/master/LICENSE)

[Source Code](https://github.com/dhilipsiva/talks/blob/master/2022-07-04-%3CNew-Horizon-College%3E-%3CIntroduction-To-Devops%3E-%3CWorkshop%3E.md)
[SlideShare Link](https://www.slideshare.net/dhilipsiva)

# Questions:question:

## [https://dhilipsiva.com](https://dhilipsiva.com)

## [dhilipsiva@pm.me](mailto:dhilipsiva@pm.me)
