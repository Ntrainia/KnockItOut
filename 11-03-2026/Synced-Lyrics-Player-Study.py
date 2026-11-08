import time
import re
import sys

from colorist import Color, blue

# Color Text
# Will be attempting to play lyrics of Taylor's Swift Guilty as Sin
# That color should be


'''
ANSI escape sequences is a standard for styling text terminals with color and font options

Sequence Parts
Ex: YELLOW = '\033[93m' 
Ex: RESET = '\033[0m'

\033[ - Control Sequence Introducer (CSI), starts sequence
93 - Color code for various text and background colors, e.g. between 30-49 or 90-109
m - Select Graphic Rendition (SGR), ends sequence

^^^ https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/introduction/#examples

Based on the website above, there seems to be an easier to read strategy 
'''

blue("Is this printing out blue?") # Testing the colorist module

'''
In Sandreke's Synced-Lyrics-Player, they have two functions.

1. load_lrc. 
    This takes the lrc file and loads it, which is when Sandreke uses the re module
    to break down the pattern. After Sandreke seems to be making a file where the lyrics get added to it.
    
2. play_lyrics(lyrics)
    This is where Sandreke breaks down the lyrics with the time and tries to sync it up using the sys module.
    
 
'''
def load_lyrics(file_path): # chapter 8 in Python Crash Course (functions)
    pattern = re.compile(r"\[(\d+):(\d+\.\d+)\](.*)")
    '''
    pattern = re.compile(r"\[(\d+):(\d+\.\d+)\](.*)")
    breakdown
    [
    re module - provides regular expression operations for pattern matching in strings
    re.compile - compile a regular expression pattern into a Pattern object. Ex: 00:07.86]
    (\d+) : Matches one or more digits (usually an hour, minute, or index number)
    (\d+\.\d+) : Matches one or more digits (a literal decimal point, one or more digits in this case timestamp)
    ] 
    (.*) : Captures the actual lyrics that plays at that time stamp
    '''
    lyrics = [] #an empty list?
    with open(file_path, "r", encoding="utf-8") as f: # Chapter 10 in Python Crash Course
        for line in f: # for each line of text in file f
            sync = pattern.match(line.strip())
            if sync:
                minutes, seconds, text = sync.groups()
                lyrics.append(int(minutes) * 60 + float(seconds), text.strip())
    return lyrics


