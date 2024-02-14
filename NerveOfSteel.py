"""
This program is for in-class exercise 4 for MGTC28 by Ibrahim

"""


import random # random libary to generate random time between the required time frame
import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")
randomtime = random.randint(5, 25)

print('Welcome to Nerve of Steel\nGame Rule: Last to sit down wins')

print('Players Stand')

print(input('Press Enter to Start'))

time.sleep(randomtime)

im.show()


