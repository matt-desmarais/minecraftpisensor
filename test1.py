from mcpi.minecraft import Minecraft
import RPi.GPIO as GPIO
import time
import pyautogui


mc = Minecraft.create()

mc.postToChat("Hello world")

#adjust for where your switch is connected
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)



while True:
  if(GPIO.input(buttonPin)):
    pyautogui.click()
  
  
  
