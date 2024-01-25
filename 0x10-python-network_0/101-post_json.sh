#!/bin/bash
# Sends a JSON POST request with file contents in the body.
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
