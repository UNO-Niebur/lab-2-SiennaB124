#Magic8Ball.py
#Name: Sienna Bonner
#Date: 1/28/26
#Assignment: Lab 2 Magic8Ball

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answers = ("yes", "most likely no", "maybe", "absolutly", "it is likely", "ask again later")
  response = random.choice(answers) 
  #Prompt the user for their question.
  question = input("ask the magic 8 ball a yes or no question:\n")
  #Answer question randomly with one of the options from your earlier list.
  print("the magic 8 ball says:", response)
if __name__ == '__main__':
  main()
