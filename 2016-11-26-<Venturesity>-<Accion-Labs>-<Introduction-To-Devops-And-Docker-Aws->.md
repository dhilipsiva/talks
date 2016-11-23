<!--
$theme: gaia
template: invert
-->

# Introduction to DevOps and Docker (AWS)

---

# Thanks to Venturesity & AccionLabs

---

## [@dhilipsiva](https://github.com/dhilipsiva)

- Tech Lead, Full-Stack & DevOps - @Appknox
- I code for Web, Mobile, Embedded & IoT. Open-Source Fanatic. Big Data & Machine Learning Enthusiast. Dad. Atheist
- So primarily a Developer + little bit of this & that
- Jack of all trades & Master of none
- [http://dhilipsiva.com](http://dhilipsiva.com)
- [dhilipsiva@gmail.com](mailto:dhilipsiva@gmail.com)

---

# I have no idea what I am talking about :stuck_out_tongue_winking_eye:


---

# The dark days before DevOps

* Developers, Testers & SysAdmins Silos
* Functionally Separated 
* Blame Culture
* Buggy Code
* Insanely longer deployment process
* Longer Feedback loops

---

![DevOps](https://raw.githubusercontent.com/dhilipsiva/talks/master/assets/2016-11-26/devops.png)

---

# DevOps

- Collaboration
- Automated
- Shorter feedback loops
- Agile

---


#### DevOps is a development methodology with a set of practices aimed at bridging the gap between Development and Operations, emphasizing communication and collaboration, continuous integration, quality assurance and delivery with automated deployment - Wikipedia

---

# DevOps Toolchain

- Code 
- Build 
- Test 
- Package 
- Release 
- Configure
- Monitor

---

# Code 

Code development and review, Version control tools, code merging

- GitHub / BitBucket / GitLab
- Issus / JIRA / BugZilla
- Waffle / Tagia

---

![DevOps](https://raw.githubusercontent.com/dhilipsiva/talks/master/assets/2016-11-26/git-model.png)

---

# Build, Test, Package

Continuous integration tools, build status. 

Test and results determine performance. 

Artifact repository, application pre-deployment staging

- Jenkins
- Drone
- Travis
- CircleCI

---

# Release, Configure 

Change management, release approvals, release automation

Infrastructure configuration and management, Infrastructure as Code tools

- Chef / Puppet / Fabric / Kubernetes / Mesos / 

---

# Monitor – Applications performance monitoring, end user experience

- New Reli
- Sentry
- DataDog

---

# DevOps Engg. != SysAdmin

* SysAdmins are people who manually deploy other people's code on a server, assuming devs provide them with dependencies & instructions. More often than not Code is a black box to them.
* DevOps Engineers are either developers who get interested in deployment and network operations, or sysadmins who have a passion for scripting and coding, and move into the development side where they can improve the planning of test and deployment.

---

# True Stories

- Building Device iOS and Android Device Farm @ Appknox
- Stolen Code

---

# Containers (Docker &  rkt)

---

# 12 Factor App

- **Codebase** - One codebase tracked in revision control, many deploys
- **Dependencies** - Explicitly declare and isolate dependencies
- **Config** - Store config in the environment
- **Backing services** - Treat backing services as attached resources

---

# ..contd

- **Build, release, run** - Strictly separate build and run stages
- **Processes** - Execute the app as one or more stateless processes
- **Port binding** - Export services via port binding
- **Concurrency** - Scale out via the process model

---

# ..contd
- **Disposability** - Maximize robustness with fast startup and graceful shutdown
- **Dev/prod parity** - Keep development, staging, and production as similar as possible
- **Logs** - Treat logs as event streams
- **Admin processes** - Run admin/management tasks as one-off processes

---

# AWS
Demo

---

# Thanks! :pray:

### https://github.com/dhilipsiva/talks

Copyright &copy; 2016 [dhilipsiva](https://github.com/dhilipsiva)

This copy is released under the [MIT License](https://github.com/dhilipsiva/talks/blob/master/LICENSE)

[Source Code](https://github.com/dhilipsiva/talks/blob/master/2016-11-26-<Venturesity>-<Accion-Labs>-<Introduction-To-Devops-And-Docker-Aws->.md)
[SlideShare Link](http://www.slideshare.net/dhilipsiva/slide)

# Questions:question:
[http://dhilipsiva.com](http://dhilipsiva.com)
