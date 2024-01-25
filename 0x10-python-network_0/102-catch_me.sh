#!/bin/bash
# Triggers a response with "You got me!" from 0.0.0.0:5000/catch_me
curl -s -L -X PUT 0.0.0.0:5000/catch_me --data "user_id=98" -H "Origin: HolbertonSchool"
