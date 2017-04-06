"""Write a function that returns the meal for any given hour of the day.
Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM
>>> meal(7)
'Breakfast time.'
>>> meal(13)
'Lunch time.'
>>> meal(20)
'Dinner time.'
>>> meal(21)
'No meal scheduled at this time.'
>>> meal(0)
'No meal scheduled at this time.'
>>> meal(3)
'Hammer time.'
>>> meal(9999)
'Not a valid time.'
"""

u_i = int(input("Enter the meal time. Use a 24 hour clock: "))

if u_i in range(700, 901):
    print("Breakfast time")

elif u_i in range(1200, 1401):
    print("Lunch time")

elif u_i in range(1900-2100):
    print("Dinner time")

elif u_i in range(2200, 2401) or range(0-401):
    print("Hammer time")
else:
    print("not a meal time or hammer time")



"""def meal1
    for hour in meal(700, 900):
        print('Breakfast time')

def meal2
    for hour in meal(1200, 1400):
        print('Lunch time')
def meal3:
    for hour in meal(1900, 2100):
        print('Dinner time')
def meal4:
    for hour in meal(22):
        print ('Hammer time')"""
