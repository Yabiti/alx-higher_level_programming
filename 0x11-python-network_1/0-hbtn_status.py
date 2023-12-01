#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request
    web = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(web) as response:
        my_file = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(my_file)))
    print("\t- content: {}".format(my_file))
    print("\t- utf8 content: {}".format(my_file.decode('utf-8')))
