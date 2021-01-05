"""
Filter out activation keys from blob of text.
"""
import sys
import re
from tkinter import Tk


def get_key():
    """
    keyf() {
        shortlisted=$(python3 /home/atb00ker/Documents/develop/scripts-lab/scripts/YoutubeRedeemer.py)
        echo "$shortlisted" | xclip -sel clip
    }
    """
    root = Tk()
    root.withdraw()
    correct_regex = '(([A-Za-z0-9]{5}-?)){3,5}'
    number = input()
    inputstr = root.clipboard_get()
    inputstr = inputstr.replace("&", number)
    pattern = re.compile(correct_regex, re.MULTILINE)
    matched = pattern.search(inputstr)
    try:
        output = matched.group(0)
        print(output)
    except:
        pass


if __name__ == "__main__":
    get_key()

