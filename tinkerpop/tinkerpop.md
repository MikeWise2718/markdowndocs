---
title: "TinkerPop"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Apache TinkerPop is a generalized graph traversal languauge. While a bit complicated (feels like it could be simpler) it is exceedingly powerful.

- The main documentation is here: [http://tinkerpop.apache.org/docs/current/reference] 
- Recipes is probably the best place to look for how to do things - [http://tinkerpop.apache.org/docs/current/recipes] 

# Installation
Didn't take notes. Opps.

# Language (Gremlin and Groovy)
"Gremlin" is the traveral language for TinkerPop, but the two words (TinkerPop and Gremlin) are almost used interchangable in conversation.
It is currently written in Java 8, and much of the syntax comes from Java. Also most programming is (probably) done in Java. However it has a REPL written in something called Groovy which is almost,but not quite, Java. This means that when perusing examples on StackOverflow, etc. you have to look carefully to see if it is Groovy or Java.
There are also bindings for Python, C# (Gremlin.Net), and a few others.
We are on TinkerPop3 and the various versions seem fairly different although I have not looked closely.
There seems to be no integration with R.

# File IO
I wrote a few routines in R to transfer the data. Probably should have just written Groovy commands to load the data.
Used something called GraphSON which is not even legal JSON (can't have a single root so that it is easily divied up to multiple processes) - and there seem to be a couple different versions that are not exactly compatible. Under the covers GraphSON appears to just be Java serialzation which is NOT a good thing since it is probably the root of the unnecssary reducnancy (links coded twice).<br>

Documentation is here: [http://tinkerpop.apache.org/docs/current/reference/#_gremlin_i_o] 


# Structure and Concepts
This link - [The Graph Process](http://tinkerpop.apache.org/docs/current/reference/#the-graph-process) explains a lot of the structure of how Gremlin works from the point of view of types and objects.

- Vertex - have identifiers - not sure if they are always assigned or internally managed.
- Edge - have identifiers - not sure if they are always assigned or internally managed. 
- Properties - both edges and vertices have properties, although they are different in certain aspects - edge properties can be multi-valued I think and a bit more.
- Graph - Graphs, Vertices and Edges are described [http://tinkerpop.apache.org/docs/current/reference/#_the_graph_structure]
 - Graph Process - described here - [http://tinkerpop.apache.org/docs/current/reference/#the-graph-process] and referred to mostly as a "traversal".

 # Example

```
gremlin> g = TinkerGraph.open()
==>tinkergraph[vertices:0 edges:0]
gremlin> g.io(IoCore.graphson()).readGraph("gson2.json");
org.apache.tinkerpop.shaded.jackson.core.JsonParseException: Unrecognized token 'AirIntake': was expecting ('true', 'false' or 'null')
 at [Source: java.io.ByteArrayInputStream@44d70181; line: 1, column: 29]
Display stack trace? [yN]
gremlin> g.io(IoCore.graphson()).readGraph("gson2.json");
==>null
gremlin> g
==>tinkergraph[vertices:27 edges:0]
gremlin> g = g.traversal()
==>graphtraversalsource[tinkergraph[vertices:27 edges:0], standard]
gremlin> g.V(1).valueMap()
==>[watts:[5], len:[0], name:[AINTK1]]
gremlin> g.V().values()
==>AINTK1
==>ADUCT1
... lots of them
gremlin> g.V().has('name','ESOURCE1').repeat(out('powers')).times(1).values('name')
==>ECOND40
==>ECOND1
gremlin> g.V().has('name','ESOURCE1').repeat(out('powers')).times(2).values('name')
==>EJUNT40
==>EJUNT40
==>EOUT1.3
==>EJUNT1
==>EJUNT1
==>EOUT1.1
==>EOUT1.2
gremlin> g.V().has('name','ESOURCE1')
==>v[147]
gremlin> g.V(147).repeat(out()).times(2).emit().path()
==>[v[147], v[192]]
==>[v[147], v[148]]
==>[v[147], v[192], v[147]]
==>[v[147], v[192], v[193]]
==>[v[147], v[192], v[193]]
==>[v[147], v[148], v[147]]
==>[v[147], v[148], v[151]]
==>[v[147], v[148], v[152]]
==>[v[147], v[148], v[152]]
==>[v[147], v[148], v[149]]
==>[v[147], v[148], v[150]]
gremlin> g.V().has('name','ESOURCE1').repeat(out('powers')).times(2).emit().path().by('name')
==>[ESOURCE1, ECOND40]
==>[ESOURCE1, ECOND1]
==>[ESOURCE1, ECOND40, EJUNT40]
==>[ESOURCE1, ECOND40, EJUNT40]
==>[ESOURCE1, ECOND1, EOUT1.3]
==>[ESOURCE1, ECOND1, EJUNT1]
==>[ESOURCE1, ECOND1, EJUNT1]
==>[ESOURCE1, ECOND1, EOUT1.1]
==>[ESOURCE1, ECOND1, EOUT1.2]
g.V(147).repeat(out().simplePath()).until(hasId(5)).path().by('name').limit(1)
==>[ESOURCE1, ECOND1, EJUNT1, ECOND7, EJUNT7, ECOND8, EJUNT8, ECOND9, AVAV2, ADUCT3]

```
