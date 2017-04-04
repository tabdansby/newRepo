width = int(input('What is the width of the wall in feet?'))
height = int(input('what is the height of the wall in feet?'))
cost = int(input('How much does a gallon of paint cost?'))
coats = int(input('How many coats will you apply?'))
result = int(((width * height * coats)/400)*cost)

print(result)
