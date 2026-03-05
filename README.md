 # API Performance Profiler using Locust

This project demonstrates how to perform load testing on REST APIs using the Locust framework.

## Overview
The API Performance Profiler simulates multiple concurrent users sending requests to an API endpoint and measures performance metrics such as response time, throughput, and failure rate.

## Features
- Simulates concurrent users hitting an API
- Measures response time and latency
- Tracks request throughput (RPS)
- Displays results on an interactive dashboard

## Technologies Used
- Python
- Locust
- REST API Testing

## How to Run

1. Install dependencies

pip install locust

2. Run Locust

locust

3. Open browser

http://localhost:8089

4. Enter test parameters and start load testing.

## Example Test

Tested endpoint:
https://jsonplaceholder.typicode.com/posts

Users simulated: 10  
Spawn rate: 2 users/sec

## Output Metrics
- Requests per second
- Average response time
- Failure rate
- Performance statistics dashboard
