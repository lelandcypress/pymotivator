import random
import datetime
date = datetime.datetime.now().weekday()
now=datetime.datetime.now().strftime("%x")

study_task=''
caloric_allowance= None
message=''

eagles_dates=('09/25/23', '10/01/23', '10/08/23','10/15/23', '10/22/23','10/29/23','11/05/23','11/20/23','11/26/23','12/03/23','12/10/23','12/17/23','12/25/23','12/31/23')
motivation = ('You\'ve got this brother! Kickass', 'little increments add up over a long time', 'You only fail when you stop trying', 'You got the job, now keep it!')
motivation = random.choice(motivation)
#0: Sunday 6:Saturday
match date:
    case 0:
        study_task = 'Your choice of tech topics'
        caloric_allowance= 2300
    case 1: 
        study_task = 'Python or bash scripting'
    case 2: 
        study_task = 'C#'
        caloric_allowance: 2100
    case 3: 
        study_task = 'Java'
        caloric_allowance: 2100 
    case 4: 
        study_task = 'Java'
        caloric_allowance: 2100
    case 5: 
        study_task = 'Rest'
        caloric_allowance: 2100    
    case 6:
        study_task='Rest and reflection'
        caloric_allowance= 2300

if now in eagles_dates:
    message ='Game day! GO BIRDS'
else:
    message = f'Another awesome day! Let\'s run down our priorities. \n Your focus for studies today: {study_task} \n Remember to limit your calories to {caloric_allowance}, movement is key. \n Finally: {motivation}...oh, and play with those boys, love your wife, and give glory to God'

