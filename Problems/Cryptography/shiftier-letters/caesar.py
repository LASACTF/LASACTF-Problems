#!/usr/bin/python3
import random
import string
import sys
import time

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

timeRem = 10
curTime = time.time()
dictFile = open('words.txt', 'r')
dictionary = dictFile.read().splitlines()
dictLength = len(dictionary)
testCount = 50
for x in range(0, testCount) :
    wordCount = random.randrange(20,30)
    sentence = ''
    for y in range(0, wordCount) :
        sentence += dictionary[random.randrange(dictLength)].lower()
        if y != wordCount - 1 :
            sentence += ' '
    print (caesar(sentence, random.randrange(26)), flush=True)
    answer = input()
    now = time.time()
    timeRem -= now - curTime
    curTime = now
    if timeRem <= 0 :
        print ("Ran out of time", flush=True)
        sys.exit()
    if answer != sentence :
        print ("Incorrect", flush=True)
        sys.exit()
print ("You made it to the end! lasactf{shif73d-3n0ugh-ar3-we}", flush=True)
