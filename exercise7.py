# Healthy programmer

# 9am -5pm

# Water - water.mp3  (3.5 litres)  -Drank-log every 1 hr


# Eyes -eyes.mp3 every 30 min- Eydone every 30 min

# physical activity -physical.mp3 every- 45 min

# Rules
# pygame module to play audio
import os
from datetime import datetime
from time import time
from pygame import mixer


def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(os.path.join(os.path.dirname(__file__), file))
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

# in below 'a' means append 
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
    # musiconloop("water.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_execise=time()
    water_time=60*60
    eyes_time=45*60
    exercise_time=45*60



    while True:
        if time()-init_water>water_time:
            print("Water drinking time. Enter 'done' to stop the alarm")
            musiconloop("alarm.wav","done")
            init_water=time()
            log_now("water alarm at")

        if time()-init_eyes>eyes_time:
            print("Eyes Exercise time. Enter 'done' to stop the alarm")
            musiconloop("alarm.wav","done")
            init_eyes=time()
            log_now("eyes exercise alarm at")

        if time()-init_execise>exercise_time:
            print("physical exercise  time. Enter 'done' to stop the alarm")
            musiconloop("water.mp3","drank")
            init_execise=time()
            log_now("Exercise alarm at")

