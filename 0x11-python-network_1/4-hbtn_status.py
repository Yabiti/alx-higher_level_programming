#!/usr/bin/python3
""" takes URL, email and  encodes the email """

from requests import get

if __name__ == "__main__":
    req = get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
