
instructions = '''1. You will be asked to enter a shape 
2. You will be asked to enter the measurements of your shape, please only enter a number
3. You will be asked for the units of your shape (mm, cm, M)
4. You will be asked if you would like to convert the units to another
5. Enter if you're trying to find area or perimeter
6. You'll get the answer!'''

#define the function
def instructions_function(question):
  valid_answer = False
  while valid_answer == False:
    #make sure to use things like .lower() to make the program more functional
    answer = input(question).lower().strip()
    if answer == "yes" or answer == "y":
      valid_answer = True
      print(instructions)
      print("─── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ───")

    elif answer == "no" or answer == "n":
      valid_answer = True
      print("─── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ───")
    else:
      print("Please answer yes or no: ")

#use the function 
instructions_function("Would you like instructions? ")

