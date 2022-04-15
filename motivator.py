from selector import *
import random
training_goals = ["Python", "C#", "AWS", "Cyber", "React"]

training_methods_py = ["Free Code Camp", "Udemy",
                       "CodeCademy", 'Start Coding', "Write Hokey-Pokeys script"]
training_methods_C = ["CodeCademy"]
aws_training = ["Free Code Camp Practinioner",
                "AWS Game", "Udemy Solutions Architect"]
cyber_training = ["Read the book", "Udemy"]
react_training = ["Udemy", "Building your App"]

motivation = ["You Got This", "Put in the time",
              "Give me 1 hour", "Give me 2 hours", "No more excuses"]
chosen_training = random.choice(training_goals)


def motivateMe():
    print("Work on", chosen_training)
    if chosen_training == "Python":
        selector(training_methods_py)
    elif chosen_training == "C#":
        selector(training_methods_C)
    elif chosen_training == "AWS":
        selector(aws_training)
    elif chosen_training == "Cyber":
        selector(cyber_training)
    elif chosen_training == "React":
        selector(react_training)
    print(random.choice(motivation))
    

motivateMe()
