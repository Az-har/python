from datetime import datetime
import pygame
import time

def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()

alarm_time = input("Enter the time of alarm to be set in HH:MM:SS AM/PM format: ")
alarm_hour = int(alarm_time[:2])
alarm_minute = int(alarm_time[3:5])
alarm_seconds = int(alarm_time[6:8])
alarm_period = alarm_time[9:].upper()

print("Setting up alarm...")

while True:
    now = datetime.now()
    current_hour = int(now.strftime("%I"))
    current_minute = int(now.strftime("%M"))
    current_seconds = int(now.strftime("%S"))
    current_period = now.strftime("%p")

    if alarm_period == current_period and alarm_hour == current_hour and alarm_minute == current_minute and alarm_seconds == current_seconds:
        print("Wake Up!")
        play_alarm_sound()
        break

    # Wait for 1 second before checking the time again
    time.sleep(1)
