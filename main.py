from microbit import *
import random

ROCK = Image("00900:09990:99999:09990:00900")
SCISSORS = Image("90009:09090:00900:99099:99099")
PAPER = Image("99999:99999:99999:99999:99999")

shapes = [ROCK, SCISSORS, PAPER]

def start_countdown():
 
    for i in range(3, -1, -1):
        display.show(str(i))
        sleep(500)
    display.clear()


while True:

    if accelerometer.was_gesture('shake'):
        start_countdown()
        
     
        choice_a = None
        choice_b = None
        
        display.show("?") 
        
        while choice_a is None or choice_b is None:
            if button_a.was_pressed():
                choice_a = random.choice(shapes)
                display.show("A") 
                sleep(500)
                display.show("?")
            
            if button_b.was_pressed():
                choice_b = random.choice(shapes)
                display.show("B") 
                sleep(500)
                display.show("?")
 
        display.show("1")
        sleep(800)
        display.show(choice_a)
        sleep(2000)
        
        # Результат Игрока B
        display.show("2")
        sleep(800)
        display.show(choice_b)
        sleep(2000)
        
        display.clear()
    
    sleep(100)