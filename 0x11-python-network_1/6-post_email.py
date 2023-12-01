#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    pay = {'email': sys.argv[2]}
    result = requests.post(sys.argv[1], data=pay)
    file = result.text
    print(file)
