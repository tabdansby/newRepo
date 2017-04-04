

phrase1 = 'this_is_snake_case'

#new_phrase1 = phrase1a.replace("_","")
new_phrase1 = phrase1.split("_")

new_list = []
for word in new_phrase1:
    new_list.append(word.capitalize())



print(''.join(new_list))

#new_phrase1.capitalize()
#new_phrase1a = new_phrase1.capitalize()




#phrase1.split()
#phrase1.capitalize()
#phrase1.join()

#print()
"""
string = 'HelloHowAreYouToday'
for i in range(len(string)):
    if string[i].isupper():
        if i != 0:
            string_list.append(string[last_index:i])
            last_index = i"""









#remove, .capitalize, replace, split, join
