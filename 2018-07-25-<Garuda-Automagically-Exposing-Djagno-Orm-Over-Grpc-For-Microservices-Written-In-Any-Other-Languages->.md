<!--
$theme: gaia
template: invert
-->

# Garuda

##  Automagically Exposing Django ORM over gRPC for microservices written in any other languages

## [@dhilipsiva](https://github.com/dhilipsiva)

---

# A bit about myself
- Optimistic Nihilist.
- Wannabe Astrophysicist.
- I code for fun & profit.
- I love Science, Python, FOSS & fitness.
- Dad of 2. Environmentalist. Story Teller. Gamer.
- [http://dhilipsiva.com](http://dhilipsiva.com)
- [dhilipsiva@gmail.com](mailto:dhilipsiva@gmail.com)

---

# I have no idea what I am talking about :stuck_out_tongue_winking_eye:

---

# Microservices

- I am assuming that everyone has a basic understanding of a microservice architecture
- For the uninitiated, it is an architectural style that structures an application as a collection of loosely coupled services, which implement business capabilities. The microservice architecture enables the continuous delivery/deployment of large, complex applications. It also enables an organization to evolve its technology stack.

---

# Implementation of microservices that I have come across

- I am just talking about small & medium startups [The only space that I have experience with]
- CLI, HTTP, RPC, Thrift

---

# CLI

- Call a command line/console application with Popen or something similar
- Very notorious (because we have limited control over the called program)
- Scaling is a bit tricky

---

# HTTP

- Build a REST / SOAP endpoint
- Document the message exchange format (which is a manual process and might be error prone)
- relatively easier to scale compared to CLI method

---

# RPC & Thirft

- Build RPC Server and clients
- Just as easy to scale as HTTP method, but this is faster because of strongly typed messages serialize and deserialize very fast and data is smaller compared to JSON / XML
- Relatively harder (Implementation wise) because of all the learning curve involved
- We have well-defined Data schemas; So manual intervention is not required to communicate changes

---

# Garuda

- How to make the RPC Implementation relatively easier
- Introducing Garuda
- Automagically Exposing Django ORM over gRPC for microservices written in any other languages
- It's done with the help of gRPC (for now). So you need to understand Protobuf, gRPC and the likes.

---

# RPC Frameworks

- **gRPC**: A high performance, open-source universal RPC framework
- **Cap'n Proto**: Cap'n Proto is an insanely fast data interchange format and capability-based RPC system.

---

# Protobuf (Which we use with gRPC)

- Protocol Buffers are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.
```
message Article {
    string id = 1;
    string content = 2;
    int32 status = 3;
    string title = 4;
}
```

---

# gRPC

Service Definition

```
service Blog {
  rpc CreateArticle (Article) returns (Article) {}
  rpc UpdateArticle (Article) returns (Article) {}
}
```

---

# What's pending?

- Documentation
- Cap'n Proto Backend
- Complex queries

---

# Garuda Demo

---

# Thanks! :pray:

### https://github.com/dhilipsiva/talks

This copy is released under the [MIT License](https://github.com/dhilipsiva/talks/blob/master/LICENSE)

[Source Code](https://github.com/dhilipsiva/talks/blob/master/2018-07-25-<Garuda-Automagically-Exposing-Djagno-Orm-Over-Grpc-For-Microservices-Written-In-Any-Other-Languages->.md)
[SlideShare Link](http://www.slideshare.net/dhilipsiva)

# Questions:question:
[http://dhilipsiva.com](http://dhilipsiva.com)
[dhilipsiva@gmail.com](mailto:dhilipsiva@gmail.com)


