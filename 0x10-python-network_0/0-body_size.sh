#!/bin/bash
# Take a URL, send request and displays the size of the response body in bytes.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
