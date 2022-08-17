import random
training_methods_py = ("Udemy", "CodeCademy",
                       "F-3", "Open source")
training_methods_C = ("CodeCademy",)
training_methods_Java = ("CodeCademy",)
training_methods_PeopleSoft = ("Milton Book",)
aws_training = ("Udemy Solutions Architect",)
cyber_training = ("Read the book", "Security+")
react_training = ("Udemy", "Goal Tracker Front End")


def selector(list):
    selected_method = random.choice(list)
    return(selected_method)
