from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            print("You Are Good To Go!!!")
            break

def log_now(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__== '__main__':
    init_water =time()
    init_eyes = time()
    init_exercise=time()
    watersec = 40
    eyessec = 30
    exercisesec = 45

    while True:
        if time() - init_water > watersec:
            print("Water Drinking time!!!! Enter 'drank' to stop alarm")
            musiconloop("water.mp3","drank")
            init_water = time()
            log_now("Drank Water at ")

        if time() - init_eyes > eyessec:
            print("Eye Exercise time!!!! Enter 'done' to stop alarm")
            musiconloop("water.mp3","done")
            init_eyes = time()
            log_now("Eye Exercise at ")

        if time() - init_exercise > exercisesec:
            print("Physical Exercise time!!!! Enter 'done' to stop alarm")
            musiconloop("water.mp3","done")
            init_exercise = time()
            log_now("Done Exercise at ")

