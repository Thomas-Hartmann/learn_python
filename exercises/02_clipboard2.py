#! /usr/bin/python3
# add_star.py - add a star to all lines in udklipsholderen.
import sys, pyperclip
print('program to get text from clipboard and add a star to each line')
content = pyperclip.paste() # paste from the clipboard
content_array = ['* '+str.strip() for str in content.splitlines() if len(str)>0]
print(content_array)
pyperclip.copy("\n".join(content_array))
