#!/usr/bin/env python3

import sys
import time
from subprocess import call

class bcolors:
  GREEN = '\033[92m'
  RED = '\033[91m'
  ENDC = '\033[0m'

def pomo_duration(duration):
  print(bcolors.GREEN + "You set duration at", duration, "minutes" + bcolors.ENDC)
  for time_duration in range(0, duration):
    print(bcolors.RED + "Remaining...", end=" " + bcolors.ENDC)
    print(bcolors.RED + " " + str(duration-time_duration) + " " + "\r", end="" + bcolors.ENDC)
    time.sleep(60)
  print("\r")
  print(bcolors.GREEN + "Time to rest!" + bcolors.ENDC)
# lock screen with utility i3lock (official page of i3lock project https://github.com/i3/i3lock)
  call("i3lock")

# default time is set at 25 minutes
pomo_duration(25)

