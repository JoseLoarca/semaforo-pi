from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
        buzzer.beep(1)
        lights.green.on()
        sleep(20)
        buzzer.beep(0.5, 0.5)
        lights.green.blink(0.5, 0.5)
        sleep(3)
        lights.green.off()
        buzzer.beep(1)
        lights.amber.on()
        sleep(2)
        buzzer.beep(0.5, 0.5)
        lights.amber.blink(0.5, 0.5)
        sleep(3)
        lights.amber.off()
        buzzer.beep(1)
        lights.red.on()
        sleep(20)
        lights.red.off()
        
