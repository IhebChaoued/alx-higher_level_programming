#!/bin/bash
# Displays only the status code of the response for the provided URL.
curl -s -o /dev/null -w "%{http_code}" "$1"
