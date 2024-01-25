#!/bin/bash
# Take a URL, send request and displays the size of the response body in bytes.

url="$1"
curl -sI "$url" | grep -i Content-Length | awk '{print $2}'
