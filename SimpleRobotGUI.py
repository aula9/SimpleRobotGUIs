# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:54:51 2019

@author: Aula-Jazmati
"""

from tkinter import *
import RPi.GPIO as gpio
import time
m1p= 16 #in 1
m1n= 12 #in 2
m2p= 18 #in 3
m2n= 22 #in 4
global p1,p2,p3,p4
gpio.setmode(gpio.BOARD)
gpio.setup(m1p, gpio.OUT)
gpio.setup(m1n, gpio.OUT)
gpio.setup(m2p, gpio.OUT)
gpio.setup(m2n, gpio.OUT)
p1 = gpio.PWM(m1p, 50)
p2 = gpio.PWM(m1n, 50)
p3 = gpio.PWM(m2p, 50)
p4 = gpio.PWM(m2n, 50)
p1.start(50)
p2.start(0)
p3.start(50)
p4.start(0)
time.sleep(1) 
window = Tk()
 
window.title("Control GUI")
lbl = Label(window, text="ROBOT Control GUI", font=("Arial Bold", 14),bg="white")
 
lbl.grid(column=5, row=0)

def forwards():
    p1.ChangeDutyCycle(10)
    p2.ChangeDutyCycle(100)
    p3.ChangeDutyCycle(10)
    p4.ChangeDutyCycle(100)
    print("forwards")
    
def backwards():
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(10)
    p3.ChangeDutyCycle(100)
    p4.ChangeDutyCycle(10)
    
    print("Backwards")
def left():
    p1.ChangeDutyCycle(80)
    p2.ChangeDutyCycle(20)
    p3.ChangeDutyCycle(20)
    p4.ChangeDutyCycle(80)
    print("Left")
    
def right():
    p1.ChangeDutyCycle(20)
    p2.ChangeDutyCycle(80)
    p3.ChangeDutyCycle(80)
    p4.ChangeDutyCycle(20)    
    print("Right")   
def stop():
    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()
    
    print("Stop")
    
btn1 = Button(window, text="FORWARDS",font=("Arial Bold", 14),bg="red", command= forwards)
 
btn1.grid(column=2, row=2)

btn2 = Button(window, text="LEFT",font=("Arial Bold", 14),bg="yellow", command= left)
 
btn2.grid(column=4, row=4)

btn3 = Button(window, text="RIGHT",font=("Arial Bold", 14),bg="cyan",command= right)
 
btn3.grid(column=6, row=6)

btn4 = Button(window, text="BACKWARDS",font=("Arial Bold", 14),bg="light green",command= backwards)
 
btn4.grid(column=8, row=8)

btn5 = Button(window, text="STOP",font=("Arial Bold", 14),fg="white",bg="blue", command= stop)
 
btn5.grid(column=5, row=10)

window.mainloop()

