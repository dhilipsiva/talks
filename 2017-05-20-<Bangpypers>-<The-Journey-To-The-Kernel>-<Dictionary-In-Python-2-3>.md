<!--
$theme: gaia
template: invert
-->

# Dictionary in Python 2 & 3

## BangPypers

## [@dhilipsiva](https://github.com/dhilipsiva)

---

- Tech Lead, Full-Stack & DevOps - [@Appknox](https://twitter.com/appknox)
- I code for Web, Mobile, Embedded & IoT. Open-Source Fanatic. Big Data & Machine Learning Enthusiast. Dad. Atheist
- So primarily a Developer + little bit of this & that
- Jack of all trades & Master of none
- No, I do not keep Bindi for religious reasons. Its for a scientific reason & a fashion statement.
- [http://dhilipsiva.com](http://dhilipsiva.com)
- [dhilipsiva@gmail.com](mailto:dhilipsiva@gmail.com)

---

# I have no idea what I am talking about :stuck_out_tongue_winking_eye:

---

# SillyDict

## [SillyDict.py](https://github.com/dhilipsiva/talks/blob/master/assets/2017-05-20/ex_01_sillydict.py)

---

# Is something wrong with SillyDict implemention?

Think about it. Its called "silly" for a reason.

---

# Time Complexity

- Array
	* Member access - O(1)
	* Member search - O(n)
- Dictionary
	* Member access - O(1)
	* Member search - O(1)

---

# How do we improve time complexity?

##### This means accessing values directly without looking for its index from keys

---

# How do you do it?

## Hash Maps

---

# SillyHashDictionary

## [SillyHashDict.py](https://github.com/dhilipsiva/talks/blob/master/assets/2017-05-20/ex_02_sillyhashdict.py)

---

# Is something wrong with SillyHashDict implemention?

---

# yes, there is!

### Too many Collision

---

# How to solve it?

---

# 1. Better Hash function
# 2. Collision handling

---

# Better hash function

## SillyBetterHashDict

### [SillyBetterHashDict.py](https://github.com/dhilipsiva/talks/blob/master/assets/2017-05-20/ex_03_sillybetterhashdict.py)

---

# Collision handling

### Open Addressing & Linked List

## OkayishDict

### [OkayishDict.py](https://github.com/dhilipsiva/talks/blob/master/assets/2017-05-20/ex_04_okayishdict.py)

---

# A Hash table
```
-+-----------------+
0| <hash|key|value>|
-+-----------------+
1|      ...        |
-+-----------------+
.|      ...        |
-+-----------------+
i|      ...        |
-+-----------------+
.|      ...        |
-+-----------------+
n|      ...        |
-+-----------------+
```

---

## Python 2.7
### On a lower level, a dict with 40 items will occupy more memory than a dict with 39 items
#### True / False?

---

# False
## But why?
### Lets analyze the underlying C that makes up python code

---

# This is why

* Arrays vs ArrayList in Java
* In C length of Array cannot be changes dynamically.
* VLA can be created at runtime, but still cannot change the length
* When elements exceeds the array length, create a new array with biggger size and copy over element.

---

# Sample Dict

```
d = {'timmy': 'red', 'barry': 'green', 'guido': 'blue'}
```

---

### Old Dictionary Implementation

```
struct dict_entry {
   long hash;
   PyObject *key;
   PyObject *value;
}
struct dict {
   long num_items;
   dict_entry *items;
}
```
```
entries = [['--', '--', '--'],
           [-8522787127447073495, 'barry', 'green'],
           ['--', '--', '--'],
           ['--', '--', '--'],
           [-9092791511155847987, 'timmy', 'red'],
           ['--', '--', '--'],
           [-6480567542315338377, 'guido', 'blue']]
```
---

### New Dictionary Implementation
```
struct dict_entry {
    long hash;
    PyObject *key;
    PyObject *value;
}
struct dict {
    long num_items;
    variable_int *sparse_array;
    dict_entry *compact_array;
}
```
```
indices =  [None, 1, None, None, 0, None, 2]
entries =  [[-9092791511155847987, 'timmy', 'red'],
            [-8522787127447073495, 'barry', 'green'],
            [-6480567542315338377, 'guido', 'blue']]
```

---

# How efficient?

For a sparse table of size t with n entries:
```
curr_size = 24 * t
new_size = 24 * n + sizeof(index) * t
# 30% - 95% less memory
```
In the above timmy/barry/guido example, the current size is `192` bytes (eight 24-byte entries) and the new size is `80` bytes (three 24-byte entries plus eight 1-byte indices). That gives 58% compression.

Resize is faster

---

# Pure python dict implementation

## Dict

### [Dict.py](https://github.com/dhilipsiva/talks/blob/master/assets/2017-05-20/ex_05_dict.py)

#### Uses in built `hash` function

---

## Python 3.6
### On a lower level, a dict with 40 items will occupy more memory than a dict with 39 items
#### True / False?

---

# False
## But again, why?
### For the same reasons as pervious one. But in this case, it is atleast it is a lot optimized that 2.7

---
# Thanks! :pray:jar

### https://github.com/dhilipsiva/talks

This copy is released under the [MIT License](https://github.com/dhilipsiva/talks/blob/master/LICENSE)

[Source Code](https://github.com/dhilipsiva/talks/blob/master/2017-05-20-<Bangpypers>-<The-Journey-To-The-Kernel>-<Dictionary-In-Python-2-3>.md)
[SlideShare Link](http://www.slideshare.net/dhilipsiva)

# Questions:question:
[http://dhilipsiva.com](http://dhilipsiva.com)
