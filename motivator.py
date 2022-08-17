import sys
from selector import *
import random
training_goals = ("Python", "C#", "Java", "AWS", "Cyber", "React",
                  "PeopleSoft", "AWS",)
slogan = ("You Got This", "Put in the time",
          "Give me 1 hour", "Give me 2 hours", "No more excuses")
chosen_training = random.choice(training_goals)
motivation = random.choice(slogan)


def motivateMe():

    if chosen_training == "Python":
        training = selector(training_methods_py)
    elif chosen_training == "C#":
        training = selector(training_methods_C)
    elif chosen_training == "Java":
        training = selector(training_methods_Java)
    elif chosen_training == "PeopleSoft":
        training = selector(training_methods_PeopleSoft)
    elif chosen_training == "AWS":
        training = selector(aws_training)
    elif chosen_training == "Cyber":
        training = selector(cyber_training)
    elif chosen_training == "React":
        training = selector(react_training)
    return training


train = motivateMe

message_to_self = f"Hey Dude! Start the week off right. Focus your efforts on {chosen_training}! Specifically {train()}! Remember {motivation}!"
