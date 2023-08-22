
#Functions go at the top
def shape_picker(question):
  valid_shape = False
  while valid_shape == False:
    shape_selected = input(question).strip().lower()
    if shape_selected == shapes[0]:
      valid_shape = True
      length = input("What is the length of the square?")

    elif shape_selected == shapes[1]:
      valid_shape = True
      valid_triangle = False
      while valid_triangle == False:
        triangle_type = input("Which type of triangle? ").strip().lower()
      
        if triangle_type == triangles[0]:
          valid_triangle = True
          angle = 90
          #ask for measurements 
        elif triangle_type == triangles[1]:
          valid_triangle = True
          angle = int(input("Enter the angle of the triangle: "))
          #ask for other measurements 
  
        elif triangle_type == triangles[2]:
          valid_triangle = True
          angle = int(input("Enter the angle of the triangle: "))
          #ask for other measurements 
        elif triangle_type == triangles[3]:
          valid_triangle = True
          angle = int(input("Enter the angle of the triangle: "))
          #ask for other measurements

        elif triangle_type == triangles[4]:
          valid_triangle = True
          angle = int(input("Enter the angle of the triangle: "))
          #ask for other measurements 

        elif triangle_type == triangles[5]:
          valid_triangle = True
          angle = int(input("Enter the angle of the triangle: "))
          #ask for other measurements 
      
        else:
          valid_triangle = False
          print("Please enter a type of triangle.")
    
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

