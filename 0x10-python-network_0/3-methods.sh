#!/bin/bash
# Displays accepted HTTP methods for the provided URL.
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-
