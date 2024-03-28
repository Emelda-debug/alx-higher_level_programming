#!/bin/bash
# this script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -Is "$1" -L | grep 'Allow' | cut -d ' '  -f2-
