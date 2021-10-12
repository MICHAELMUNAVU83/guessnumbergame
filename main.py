# shape = input('what is your shape :')
# size = input('what is your size :')
# color = input('what is your color :')


# print('your favorite shape is' + shape)
# print('your favorite size is' + size)
# print('your favorite color is' + color)


# def sayhi(num):
#    return num*num*num
    
# print(sayhi(3)b

    

# guess = ''
# guess_count = 0

# while guess != 'giraf' and guess_count<3:
   
#     guess = input('take a guess:')
#     guess_count += 1
    
# if guess== 'giraf':
#      print('you won!') 
# if guess_count>=3 and guess!= 'giraf':
#      print('you lost') 
     
     
# class Student:
#      def __init__(self, name , age, uni):
#           self.name = name
#           self.age = age
#           self.uni = uni
          
     
   
     
# studen1 = Student('moffat', 20 , 'uon')     
# print(studen1.uni)
         
# print('Welcome to your band name generator')          
     
# city =  input('Which city were you born in : \n')


# pet = input('What is  your favourite pet :\n') 
# print("Your band name can be" + ' ' + city + ' ' + pet)




# print('BMI calculator!!!!')

# weight = input('Enter your weight i kilograms : \n' )
# height = input('Enter your height in metres : \n' )

# height_num = float(height)
# weight_num = float(weight)


# from math import*

# bmi = (weight_num)/(height_num **2)
# full_bmi = int(bmi)
# print(full_bmi)

# f string




# my_age = input('what is your age : \n')
# rem_age = 90 -int( my_age)
# print(rem_age)

# years_remaining = rem_age
# month_remaining = rem_age*12
# day_remaining = rem_age*365

# print(f'You have {years_remaining} years remaining, {month_remaining} months, and {day_remaining} days')
# print('WELCOME TO YOUR BILL CALCULATOR')

# bill = input('What is your total bill ? \n $')
# print(float(bill))
# tip = input('What percentage tip would you like to give ? 10, 12 or 15 \n ')
# guys_splitting = input('How many people are you splitting the bill with ?\n')

# total_tip=(float(tip) * 0.01 ) * (float(bill))


# total_bill = float(total_tip) + float(bill)
# bill_for_each =  total_bill/ float(guys_splitting)
# bill_for_each_round = round(bill_for_each, 2)

# print(f'Each person should pay : ${bill_for_each_round}')


    
# # odd and even


# num = input('enter a number :')
# numint = int(num)

# if numint%2==0:
#     print('even number')
# else:
#     print('odd number')    
    
                                   


# nested if statements

# num1 = input('Enter your height : \n')
# height = int(num1)

# if height <= 120:
#     age = input('What is your age ? \n')
#     age_int = int(age)
#     if age_int <= 18:
#         print('ticket is 7$')
#     else:
#         print('ticket is 12 $')
# else :
#     print('you are too tall for the slide')
    
    
# year = int(input('Enter year to test : \n'))

#  if start % 4==0:
#         if start % 100==0:
#         if start% 400==0:
#             print('This is a leap year ')
#         else:
#             print('This is not a leap year ')
#     else:
#         print('This is a leap year ')
# else:
#     print('This is not a leap year')

# leap year between


# start =int( input('year to start : \n') )   
# end = int(input('year to end :\n'))

# print('')
# print('')


# print(f'The leap years between {start} and {end} are :')
# while  end > start:
    
#     start +=1
    
    
   
    
#     if start%4 ==0:
#         if start%100 ==0:
#             if start%400 ==0 :
#                 print(start)
            
#         else:
           
#             print(start)           
    
    
# pizza ordering system


# print('Welcome to the Trance Pizza hut  !!')

# size = input('What size do you want ? \n small, medium,large\n') 
# peper= input('Do you want pepperoni on your pizza ?\n yes or no \n')   
# cheese = input('Do you want extra cheese on your pizza ?\n yes or no..\n')
# num = int(input('How many of such pizzas do you want ? \n 1,2,3..... \n'))

# if size == 'small':
#     pizza_price = 500
#     if peper== 'yes':
#         peper_price = 50
#     else:
#         peper_price= 0    
#     if cheese=='yes':
#         cheese_price= 50
#     else:
#         cheese_price=0    
# elif size == 'medium':
#     pizza_price = 700
#     if peper== 'yes':
#         peper_price = 100
#     else:
#         peper_price= 0    
#     if cheese=='yes':
#         cheese_price= 100
#     else:
#         cheese_price=0    
# elif size == 'large':
#     pizza_price = 1000
#     if peper== 'yes':
#         peper_price = 150
#     else:
#         peper_price= 0    
#     if cheese=='yes':
#         cheese_price= 150
#     else:
#         cheese_price=0         
        
       
# full_price = pizza_price+peper_price+cheese_price
# full_cost = full_price*num



# print(f'Your total cost of your {num} {size} sized pizza(s) plus toppings is {full_cost}')            
   
