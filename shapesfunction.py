
#Functions go at the top
def shape_picker(question):
  valid_shape = False
  while valid_shape == False:
    shape_selected = input(question).strip().lower()
    if shape_selected == shapes[0]:
      valid_shape = True
       #ask for measurements 

    elif shape_selected == shapes[1]:
      valid_shape = True
      triangle_type = input("Which type of triangle? ").strip().lower()
      #ask for measurements 
    
    elif shape_selected == shapes[2]:
      valid_shape = True
      #ask for measurements 

    elif shape_selected == shapes[3]:
      valid_shape = True
      #ask for measurements 

    elif shape_selected == shapes[4]:
      valid_shape = True
      #ask for measurements 
    else:
      print("That shape is not in the list. Please enter a different shape")

#Lists go under functions
shapes = ["square", "triangle", "rectangle", "circle", "parallelogram"]
triangles = ["right angle", "equilateral", "isoceles", "acute", "scalene", "obtuse"]

#Use the function
shape_picker("Choose a shape: ")

