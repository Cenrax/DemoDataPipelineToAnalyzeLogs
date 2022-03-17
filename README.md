# Demo: Data Pipeline To AnalyzeLogs
This is a demo project to create a pipeline based on the logs collected from a NGINX log file

## Problem Statement and Goal
The goal of our pipeline will be to take log lines, from the example_log.txt file, and create a summary CSV file of unique HTTP request types and their associated counts. Each line from the example_log.txt file is from an NGINX log file. This log file contains each client request sent to a running web server in a client-server model.

![image](https://user-images.githubusercontent.com/43017632/158326607-e89c695b-79eb-4639-98c7-09f0822746f2.png)

```
200.155.108.44 - - [30/Nov/2017:11:59:54 +0000] "PUT /categories/categories/categories HTTP/1.1" 401 963 "http://www.yates.com/list/tags/category/" "Mozilla/5.0 (Windows CE) AppleWebKit/5332 (KHTML, like Gecko) Chrome/13.0.864.0 Safari/5332"
36.139.255.202 - - [30/Nov/2017:11:59:54 +0000] "PUT /search HTTP/1.1" 404 171 "https://www.butler.org/main/tag/category/home.php" "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_0) AppleWebKit/5332 (KHTML, like Gecko) Chrome/15.0.813.0 Safari/5332"
50.112.115.219 - - [30/Nov/2017:11:59:54 +0000] "POST /main/blog HTTP/1.1" 404 743 "http://deleon-bender.com/categories/category.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_5 rv:2.0; apn-IN) AppleWebKit/531.48.1 (KHTML, like Gecko) Version/4.0 Safari/531.48.1"
204.132.56.4 - - [30/Nov/2017:11:59:54 +0000] "POST /list HTTP/1.1" 404 761 "http://smith.com/category.htm" "Opera/9.39.(Windows 98; Win 9x 4.90; mn-MN) Presto/2.9.163 Version/12.00"
233.154.7.24 - - [30/Nov/2017:11:59:54 +0000] "GET /app HTTP/1.1" 404 526 "http://www.cherry.com/main.htm" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/5360 (KHTML, like Gecko) Chrome/13.0.839.0 Safari/5360"
```
The above lines are the first few lines of the nginx log file

The syntax of the files are as follows:
```
$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
```
- $remote_addr — the ip address of the client making the request to the server.
- $remote_user — if the client authenticated with basic authentication, this is the user name (blank in the examples above).
- $time_local — the local time when the request was made.
- $request — the type of request, and the URL that it was made to.
- $status — the response status code from the server.
- $body_bytes_sent — the number of bytes sent by the server to the client in the response body.
- $http_referrer — the page that the client was on before sending the current request.
- $http_user_agent — information about the browser and system of the client.

***Before diving to the pipeline we need to understand what is a Generator in Python and why we need it***
When creating a list, Python loads each element of the list into RAM. For files that exceed multiple gigabytes, this file loading can cause a program to run out of memory.

So how do we overcome this:
Instead of reading the file into memory, we can take advantage of file streaming. File streaming works by breaking a file into small sections (called chunks), and then loaded one at time into memory. Once a chunk has been exhausted (all the bytes of that chunk has been read), Python requests the next chunk, and then that chunk is loaded into memory to be iterated on.

This is actually abstracted from us using the context manager
```
with open('example_log.txt') as file:
    for line in file:
        # The file acts like an iterator.
        print(line)
```
We can see evidence of exhausted bytes if you try to read from the opened file again:
```
with open('example_log.txt') as file:
    for line in file:
        do_something()

    # At this point, the file has been read and
    # no unread bytes are remaining.
    for line in file:
        # The `file` is empty and the loop ends
        # immediately.
        do_something()
```

This stream-like behavior is extremely helpful when working with large data sets. We can replicate this behavior with other iterators with the use of generators. A generator is an iterable object that is created from a generator function.

The generator function differs from a regular function by two important differences:

    - A generator uses yield, instead of return. (However, a return statement is used to stop iteration).
    - Local variables are kept in memory until the generator completes.
    
For more details into generator see the generator.md file 


After parsing our logs into a generator of tuples, it's now time to write a task, and save the rows to a CSV file. This keeps the data in a well known data storage structure that we can use in future tasks. In the next lesson, we will discuss the role of files in a data pipeline.

Please look at the createCSV.py to see how we are doing that
