#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    my_url = sys.argv[1]
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
