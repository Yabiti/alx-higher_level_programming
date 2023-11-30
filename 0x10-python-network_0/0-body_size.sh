#!/bin/bash
# take url, send request to the url,display the size of the bodyresponse
curl -s "$1" | wc -c
