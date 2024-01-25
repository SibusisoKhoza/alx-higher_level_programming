#!/bin/bash

# Check if URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a GET request and display the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read -r status
    if [ "$status" -eq 200 ]; then
        curl -s "$1"
    fi
}
