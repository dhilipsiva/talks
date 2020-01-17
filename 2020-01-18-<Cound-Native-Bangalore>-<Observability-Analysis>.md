<!--
$theme: gaia
template: invert
-->

# OpenTelemetry + Jaeger

#### Container Meetup, Bangalore

#### [@dhilipsiva](https://github.com/dhilipsiva)

---

- Optimistic Nihilist.
- Wannabe Astrophysicist.
- I code for fun & profit.
- I love Science, Python, FOSS & fitness.
- Dad of 2. Environmentalist. Story Teller. Gamer.
- Jack of all trades & Master of none
- [http://dhilipsiva.com](http://dhilipsiva.com)
- [dhilipsiva@pm.me](mailto:dhilipsiva@pm.me)

---

# I have no idea what I am talking about :stuck_out_tongue_winking_eye:

---


# Why Distributed Tracing?
* Distributed microservices
* Hard to debug process flow in conventional tracing
* context propagation

---

#### OpenTracing + OpenCensus
#### =
# OpenTelemetry

---

# Before we get started

- It's okay to not know python for this talk. You can use the same prinsiples in other languages too
- How many of you are comfortable with containers?
- How many of you are comfortable with gRPC?
- Have anyone use ***traefik*** before?

---

# Specification 101

* Span
* Traces
* SpanContext

---

# OpenTelemetry Data Model

```
Causal relationships between Spans in a single Trace


        [Span A]  ←←←(the root span)
            |
     +------+------+
     |             |
 [Span B]      [Span C] ←←←(Span C is a `ChildOf` Span A)
     |             |
 [Span D]      +---+-------+
               |           |
           [Span E]    [Span F] >>> [Span G] >>> [Span H]
                                       ↑
                                       ↑
                                       ↑
                         (Span G `FollowsFrom` Span F)
```

---

## Visualize Traces with a time axis

```
Temporal relationships between Spans in a single Trace


––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–> time

 [Span A············································]
   [Span B·······································]
      [Span D··································]
    [Span C·································]
         [Span E·······]  [Span F··] [Span G··] [Span H··]
```

---

# Demo

---

# Thanks! :pray:

### https://github.com/dhilipsiva/talks

This copy is released under the [MIT License](https://github.com/dhilipsiva/talks/blob/master/LICENSE)

[Source Code](https://github.com/dhilipsiva/talks/blob/master/2020-01-18-%3CCound-Native-Bangalore%3E-%3CObservability-Analysis%3E.md)
[SlideShare Link](http://www.slideshare.net/dhilipsiva)

# Questions:question:
[http://dhilipsiva.com](http://dhilipsiva.com)
[dhilipsiva@pm.me](mailto:dhilipsiva@pm.me)
