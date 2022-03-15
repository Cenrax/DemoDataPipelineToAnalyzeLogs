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

