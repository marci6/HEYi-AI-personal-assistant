# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:53:04 2021

@author: MARCELLOCHIESA
"""

import pyttsx3

engine=pyttsx3.init('sapi5')

""" RATE"""
engine.setProperty('rate', 140)     # setting up new voice rate
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()
