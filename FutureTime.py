#FutureTime.py
#Name: Sienna Bonner
#Date: 1/28/26
#Assignment: Lab 2 FutureTime

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour + 6
  currentMinute = now.minute

  

  #TODO:
  #Ask user for hours
  hours = int(input("how many hours?\n"))
  #Ask user for minutes
  minutes = int(input("how many minutes?\n"))
  #Calculate the time after the user-supplied time has passed.
  passedMinutes = (currentMinute + minutes) % 60
  extraHours = (currentMinute + minutes) // 60
  passedHours = (currentHour + hours + extraHours) % 12

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("future time: " + str(passedHours) + ":" + str(passedMinutes))
0
if __name__ == '__main__':
  main()
