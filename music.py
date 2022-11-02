#!/usr/bin/env python3

import sys, csv, time

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

bz = TonalBuzzer(12, initial_value=None, mid_tone=Tone('A4'), octaves=3)
octave_offset = 0
bpm = 60

def set_bpm(new_bpm):
    global bpm
    bpm = new_bpm
    global sec_per_beat
    sec_per_beat = 60/bpm

    global whole
    whole = sec_per_beat * 4
    global half
    half = sec_per_beat * 2
    global quarter
    quarter = sec_per_beat * 1
    global eighth
    eighth = sec_per_beat * 0.5
    global sixteenth
    sixteenth = sec_per_beat * 0.25
    global thirty_second
    thirty_second = sec_per_beat * 0.125

def set_octave_offset(offset):
    global octave_offset
    octave_offset = offset

def pause(length):
    global whole
    global half
    global quarter
    global eighth
    global sixteenth
    global thirty_second

    if length == "1":
        time.sleep(whole)
    elif length == "2":
        time.sleep(half)
    elif length == "4":
        time.sleep(quarter)
    elif length == "8":
        time.sleep(eighth)
    elif length == "16":
        time.sleep(sixteenth)
    elif length == "32":
        time.sleep(thirty_second)


with open(sys.argv[1], "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) == 2:
            print(row)

            if row[0] == "bpm":
                set_bpm(int(row[1]))
            elif row[0] == "oct":
                set_octave_offset(int(row[1]))
            elif row[0] == "R":
                bz.stop()
                pause(row[1])
            else:
                octave = int(row[0][1])
                octave += octave_offset
                bz.play(row[0][0] + str(octave))
                pause(row[1])
        elif len(row) == 1:
            print(row) # prints out comments
