import random
training_methods_py = ["Free Code Camp", "Udemy",
                       "CodeCademy", 'Start Coding', "Write Hokey-Pokeys script"]
training_methods_C = ["CodeCademy"]
aws_training = ["Free Code Camp Practinioner",
                "AWS Game", "Udemy Solutions Architect"]
cyber_training = ["Read the book", "Udemy"]
react_training = ["Udemy", "Building your App"]


def selector(list):
    selected_method = random.choice(list)
    print(selected_method)


