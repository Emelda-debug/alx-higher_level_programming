#!/bin/bash
# this script takes in a URL, sends a GET request to the URL,
#and displays the size of the body of the response
curl -Xs GET $1 -L

