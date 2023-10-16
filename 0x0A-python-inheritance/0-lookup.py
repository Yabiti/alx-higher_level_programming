#!/usr/bin/python3
songs = open('file.txt')
for lines in songs.read():
    print(lines, end = ' ')