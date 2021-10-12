names= input('Enter your names seperated by a comma :\n')

import random
name_split = names.split(',')
total_num = len(name_split)


random_num =random.randint(0, total_num)
random_name = name_split[random_num]

print('The bill will be paid by ' + random_name)

    
    
    
    
    
 