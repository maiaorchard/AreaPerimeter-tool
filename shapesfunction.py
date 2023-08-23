
#Functions go at the top
def shape_picker(question):
  valid_shape = False
  while valid_shape == False:
    shape_selected = input(question).strip().lower()
    if shape_selected == shapes[0]:
      valid_shape = True
      
      #ask for measurements
      valid_number = False
      while valid_number == False:
        try:
          length = float(input("What is the length of the square? (Please enter only a number) "))
          valid_number = True
        except:
          print("Please enter a number")
      
      #ask for units
      #units = input("Please enter the units: ")

    elif shape_selected == shapes[1]:
      valid_shape = True
      valid_triangle = False
      while valid_triangle == False:
        triangle_type = input("Which type of triangle? ").strip().lower()
      
        if triangle_type == triangles[0]:
          valid_triangle = True
          #ask for measurements depending on the formulas
          
          
        elif triangle_type == triangles[1]:
          valid_triangle = True
          #ask for other measurements depending on the formulas
          
        elif triangle_type == triangles[2]:
          valid_triangle = True
          #ask for other measurements depending on the formulas
          
        elif triangle_type == triangles[3]:
          valid_triangle = True
          #ask for other measurements depending on the formulas
          
        elif triangle_type == triangles[4]:
          valid_triangle = True
          #ask for other measurements depending on the formulas
          
        elif triangle_type == triangles[5]:
          valid_triangle = True
          #ask for other measurements depending on the formulas
          
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
triangles = ["right angle", "equilateral", "isosceles", "acute", "scalene", "obtuse"]

#Use the function
shape_picker("Choose a shape: ")

