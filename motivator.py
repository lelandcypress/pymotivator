import sys
from selector import *
import random
training_goals = ("Python", "C#", "Java", "AWS", "Cyber", "React",
                  "PeopleSoft", "AWS",)
training_methods_py = ("Udemy", "CodeCademy", 'Start Coding',
                       "Write Hokey-Pokeys script", "Open source")
training_methods_C = ("CodeCademy", "Pick a project")
training_methods_Java = ("CodeCademy", "Pick a project")
training_methods_PeopleSoft = ("Milton Book",)
aws_training = ("Udemy Solutions Architect",)
cyber_training = ("Read the book", "Udemy")
react_training = ("Udemy", "Goal Tracker Front End")
motivation = ("You Got This", "Put in the time",
              "Give me 1 hour", "Give me 2 hours", "No more excuses")
chosen_training = random.choice(training_goals)


def motivateMe():
    print("Work on", chosen_training)
    if chosen_training == "Python":
        selector(training_methods_py)
    elif chosen_training == "C#":
        selector(training_methods_C)
    elif chosen_training == "Java":
        selector(training_methods_Java)
    elif chosen_training == "PeopleSoft":
        selector(training_methods_PeopleSoft)
    elif chosen_training == "AWS":
        selector(aws_training)
    elif chosen_training == "Cyber":
        selector(cyber_training)
    elif chosen_training == "React":
        selector(react_training)
    print(random.choice(motivation))


motivateMe()
