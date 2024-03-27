#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the size of the body of the response using curl's '-s' option to suppress progress meter and other unnecessary output
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size of the body of the response
echo "Size of the response body: $response bytes"
