#! python
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard

import pyperclip
import sys
import webbrowser

if len(sys.argv) > 1:
    # Get address from the command line.
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)
