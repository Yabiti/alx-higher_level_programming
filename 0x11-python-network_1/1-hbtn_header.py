#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request
from sys import argv
import sys

if __name__ == "__main__":
    my_url = sys.argv[1]

    with urllib.request.urlopen(my_url) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
