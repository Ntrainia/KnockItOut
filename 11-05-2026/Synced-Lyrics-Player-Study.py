import time
import re
import sys

import colorist
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
BLUE = '\033[34m'
RESET = '\033[0m'

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
                lyrics.append((int(minutes) * 60 + float(seconds), text.strip()))
    return lyrics


# ^^^ 11-03-2026
'''
Today I am studying the second function of Sandreke's code. 
Sandreke left a comment stating that this function 'display lyrics with typewriter effect synchronized with timestamps'.
Reading the lines of code, I find this function already more difficult to write than the load_lrc.

I see that the time and sys modules are used, but I am a bit puzzled on what the sys module does in this case.
The code:
for char in text:
    sys.stdout.write(YELLOW + char) 
    sys.stdout.flush()
    time.sleep(0.03)
sys.stdout.write(RESET + '\n')

https://docs.python.org/3/library/sys.html <- I am using this documentation to learn more about sys module
sys.stdout - file objects used by the interpreter, is used for the output of print() and expression statements
and for the prompts of input()
flush() forces data out of a temporary memory buffer and directly into its detination
time.sleep() - suspends the execution of the current thread for a specified numbers of seconds
'''

def play_lyrics(lyrics):
    start_time = time.time() # return the time in seconds since the epoch as a floating-point number
    for timestamp, text in lyrics:
        while time.time() - start_time < timestamp:
            time.sleep(0.01)
        sys.stdout.write('\r' + ' ' * 80 + '\r') # https://stackoverflow.com/questions/14606799/what-does-r-do-in-the-following-script - helps me understand what \r does
        for char in text:
            sys.stdout.write(BLUE + char) # can exclude the YELLOW since my default text color is blue from the colorist module
            sys.stdout.flush()
            time.sleep(0.03)
        sys.stdout.write(RESET + '\n')
        sys.stdout.flush()

if __name__ == "__main__":
    lyrics = load_lyrics("\lyrics\Guilty_as_Sin.lrc") # had to edit the pathname since the absolute path revealed private information
    play_lyrics(lyrics)


# it works, but the text does not return blue. I was misled myself. For tomorrow, I would like to tweak some things
# to make this my own version truly.

'''
editing to make adjustments to the synced lyrics
- made the text color blue instead now, unfortunately the colorist module only applies onto text (print)
'''