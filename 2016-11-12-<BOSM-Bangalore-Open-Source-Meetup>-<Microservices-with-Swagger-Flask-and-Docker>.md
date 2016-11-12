<!--
$theme: gaia
template: invert
-->

# Microservices with Swagger, Flask and Docker

#### BOSM - Bangalore Open Source Meetup

## [@dhilipsiva](https://github.com/dhilipsiva)

Tech Lead, Full-Stack & DevOps - @Appknox
[http://dhilipsiva.com](http://dhilipsiva.com)
[dhilipsiva@gmail.com](mailto:dhilipsiva@gmail.com)

---

# @dhilipsiva
- Tech Lead, Full-Stack & DevOps - @Appknox
- I code for Web, Mobile, Embedded & IoT. Open-Source Fanatic. Big Data & Machine Learning Enthusiast. Dad. Atheist
- So primarily a Developer + little bit of this & that
- Jack of all trades & Master of none

---

# I have no idea what I am talking about :stuck_out_tongue_winking_eye:

---

## The Open API Specification - V2.0  (f.k.a. Swagger Specification)

The OpenAPI Specification (originally known as the Swagger Specification) is a specification for machine-readable interface files for describing, producing, consuming, and visualizing RESTful web services. (Quoted from [Wikipedia](https://en.wikipedia.org/wiki/OpenAPI_Specification))

Swagger™ is a project used to describe and document RESTful APIs.

https://github.com/OAI/OpenAPI-Specification

---

# Uses

* Language Neutral & Machine Readable Format
* APIs can be defined in JSON or YAML
* API-First Development
* Tooling Support (core, UI, codegen, editor)

---

# History

* 2010: Tony Tam @Wordnik founded Swagger
* 2010-2014: Development, Growth, Adoption, Tooling, Community
* Early 2015: Swagger acquired by SmartBear
* Late 2015: Swagger donated to "Linux Foundation" as“OpenAPI Specification” 

---

# Google Search Activity

![Google](https://raw.githubusercontent.com/dhilipsiva/talks/master/2016-11-12-content/01-google-search.png)

---

# GitHub - Starts / Forks / Pulls

![GitHub 1](https://raw.githubusercontent.com/dhilipsiva/talks/master/2016-11-12-content/02-github-1.png)

---

# Issues / Events / Commits

![GitHub 2](https://raw.githubusercontent.com/dhilipsiva/talks/master/2016-11-12-content/02-github-2.png)

--- 

# Tooling

* [swagger-core](https://github.com/swagger-api/swagger-core)
* [swagger-ui](https://github.com/swagger-api/swagger-ui)
* [swagger-codegen](https://github.com/swagger-api/swagger-codegen)
* [swagger-editor](https://github.com/swagger-api/swagger-editor)
* [swagger-hub](https://swaggerhub.com/)

---

# Few of the Language Tools

* [swagger-node](https://github.com/swagger-api/swagger-node)
* [django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger)
* [swagger-php](https://github.com/zircote/swagger-php)
* [swagger-js](https://github.com/swagger-api/swagger-js)
* [go-swagger](https://github.com/go-swagger/go-swagger)

---

# Break

--- 

# Hands On

Connection Example Repo: https://github.com/ds-forks/connexion-example

```
swagger-codegen generate -i swagger.yaml -l java -o /tmp/swag
connexion run swagger.yaml --stub --debug
```

---

# Docker

```
    $ docker build -t connexion-example .
    $ docker run -d -p 8080:8080 connexion-example
    $ ./test.sh # do some test HTTP requests
```


---


# Thanks! :pray:

### https://github.com/dhilipsiva/talks

Copyright &copy; 2016 [dhilipsiva](https://github.com/dhilipsiva)

This copy is released under the [MIT License](https://github.com/dhilipsiva/talks/blob/master/LICENSE)

[Source Code](https://github.com/dhilipsiva/talks/blob/master/2016-11-12-%3CBOSM-Bangalore-Open-Source-Meetup%3E-%3CMicroservices-with-Swagger-Flask-and-Docker%3E.md)

# Questions:question:
[http://dhilipsiva.com](http://dhilipsiva.com)