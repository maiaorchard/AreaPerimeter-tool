f = True

#Functions go at the top
def shape_picker(question):
  shape_selected = input(question).strip().lower()
  if shape_selected == shapes[0]:
    print(shape_selected)
    #ask for measurements 
  elif shape_selected == shapes[1]:
    triangle_type = input("Which type of triangle? ").strip().lower()
    #ask for measurements 
    print(triangle_type)
  elif shape_selected == shapes[2]:
    print(shape_selected)
    #ask for measurements 
  elif shape_selected == shapes[3]:
    print(shape_selected)
    #ask for measurements 
  elif shape_selected == shapes[4]:
    print(shape_selected)
    #ask for measurements 
  else:
    print("That shape is not in the list. Please enter a different shape")
    shape_selected = input(question)

#Lists go under functions
shapes = ["square", "triangle", "rectangle", "circle", "parallelogram"]
triangles = ["right angle", "equilateral", "isoceles", "acute", "scalene", "obtuse"]

#Use the function
while f == True:
  shape_picker("Choose a shape: ")

