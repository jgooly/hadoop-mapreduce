# Hadoop and MapReduce

This course is available on [Udacity](https://www.udacity.com/) as [Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617). More specifically, this course covers the use of MapReduce with Hadoop Streaming and Python 2.7. 

## Python Coding Projects and Topics Covered

### Overview of "Big Data"
* What is "Big Data"?
*The problems it creates.
* How Apache Hadoop addresses these problems.

### HDFS and MapReduce
* Discover how HDFS distributes data over multiple computers.
* Learn how MapReduce enables analyzing datasets in parallel across multiple machines.

### MapReduce Code
* Writing your own MapReduce code in Python.

### MapReduce Design Patterns
* Use common patterns for MapReduce programs to analyze Udacity forum data.

---
##### Running MapReduce Jobs and Hadoop Distribution
The MapReduce jobs were run on a virtual machine using CDH (Cloudera Distribution of Apache Hadoop).

##### Data
Data types, shapes, size varies by lesson. However, the Final Project dataset can be found [here](https://www.udacity.com/wiki/ud617). The dataset consists of two files; _forum_nodes.tsv_ and _forum_users.tsv_. This dataset consists of Udacity forum data which is designed and has a similar structure to that of the StackOverflow forums. 

##### Testing Locally
One method to test MapReduce code before running them on Hadoop is to test a smaller sample of data locally. This is accomplished using the command line with some simple bash commands. This was very helpful for debugging and testing.

First create a small sample of data:  
>`head -100 path/to/data.txt > data_sample.txt`

Run the MapReduce pipeline on sample data:  
>`cat path/to/data_sample.txt | python mapper.py | sort | python reducer.py`
---
## Final Project Objectives
##### Students and Posting Time on Forums

Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.  Find for each student what is the hour during which the student has posted the most posts. Output from reducers should be: "author_id \t hour".  If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.

##### Post Length and Answer Length on Forums

We are interested to see if there is a correlation between the length of a post and the length of answers.  Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post.

##### Top 10 Question Tags

We are interested seeing what are the top tags used in posts.  Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

##### Potential Student Study Groups

We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.  As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
