
#Functions go at the top
def shape_picker(question):
  valid_shape = False
  while valid_shape == False:
    shape_selected = input(question).strip().lower()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif shape_selected == shapes[1]:
      valid_shape = True
      valid_triangle = False
      while valid_triangle == False:
        triangle_type = input("Which type of triangle? ").strip().lower()
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if triangle_type == triangles[0]:
          valid_triangle = True
          #ask for length
          valid_length = False
          while valid_length == False:
            try:
              length = float(input("What is the length of the triangle? (Please enter only a number) "))
              valid_length = True
            except:
              print("Please enter a number")

          #ask for width
          valid_width = False
          while valid_width == False:
            try:
              width = float(input("What is the width of the triangle? (Please enter only a number) "))
              valid_width = True
            except:
              print("Please enter a number")
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif triangle_type == triangles[1]:
          valid_triangle = True
          #ask for length
          valid_length = False
          while valid_length == False:
            try:
              length = float(input("What is the length of the triangle? (Please enter only a number) "))
              valid_length = True
            except:
              print("Please enter a number")
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif triangle_type == triangles[2]:
          valid_triangle = True
          #ask for base length
          valid_base = False
          while valid_base == False:
            try:
              base = float(input("What is the length of the base of the triangle? (Please enter only a number) "))
              valid_base = True
            except:
              print("Please enter a number")

          #ask for height
          valid_height = False
          while valid_height == False:
            try:
              height = float(input("What is the height of the triangle? (Please enter only a number) "))
              valid_height = True
            except:
              print("Please enter a number")

          #ask for the length of the side
          valid_length = False
          while valid_length == False:
            try:
              side = float(input("What is the length of the side of the triangle? (Please enter only a number) "))
              valid_length = True
            except:
              print("Please enter a number")
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif triangle_type == triangles[3]:
          valid_triangle = True
          #ask for base measurement
          valid_base = False
          while valid_base == False:
            try:
              base = float(input("What is the length of the base of the triangle? (Please enter only a number) "))
              valid_base = True
            except:
              print("Please enter a number")

          #ask for height
          valid_height = False
          while valid_height == False:
            try:
              height = float(input("What is the height of the triangle? (Please enter only a number) "))
              valid_height = True
            except:
              print("Please enter a number")

          #ask for the length of one side
          valid_length = False
          while valid_length == False:
            try:
              side = float(input("What is the length of one side of the triangle? (Please enter only a number) "))
              valid_length = True
            except:
              print("Please enter a number")

          #ask for the length of the other side
          valid_length2 = False
          while valid_length2 == False:
            try:
              side = float(input("What is the length of the other side of the triangle? (Please enter only a number) "))
              valid_length2 = True
            except:
              print("Please enter a number")
    
        elif triangle_type == triangles[4] or triangle_type == triangles[5]:
          valid_triangle = True
          #ask for base measurement
          valid_base = False
          while valid_base == False:
            try:
              base = float(input("What is the length of the base of the triangle? (Please enter only a number) "))
              valid_base = True
            except:
              print("Please enter a number")

          #ask for height
          valid_height = False
          while valid_height == False:
            try:
              height = float(input("What is the height of the triangle? (Please enter only a number) "))
              valid_height = True
            except:
              print("Please enter a number")

          #ask for the length of one side
          valid_length = False
          while valid_length == False:
            try:
              side = float(input("What is the length of one side of the triangle? (Please enter only a number) "))
              valid_length = True
            except:
              print("Please enter a number")

          #ask for the length of the other side
          valid_length2 = False
          while valid_length2 == False:
            try:
              side = float(input("What is the length of the other side of the triangle? (Please enter only a number) "))
              valid_length2 = True
            except:
              print("Please enter a number")
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        else:
          valid_triangle = False
          print("Please enter a type of triangle or check your spelling of the triangle type.")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif shape_selected == shapes[2]:
      valid_shape = True
      #ask for length
      valid_length = False
      while valid_length == False:
        try:
           length = float(input("What is the length of the rectangle? (Please enter only a number) "))
           valid_length = True
        except:
          print("Please enter a number")
          #ask for width
        valid_width = False
        while valid_width == False:
          try:
            width = float(input("What is the width of the rectangle? (Please enter only a number) "))
            valid_width = True
          except:
            print("Please enter a number")
            #ask for units
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif shape_selected == shapes[3]:
      valid_shape = True
      #ask for radius
      valid_radius = False
      while valid_radius == False:
        try:
          radius = float(input("What is the radius of the circle? (Please enter only a number) "))
          valid_radius = True
        except:
          print("Please enter a number")
      #ask for units 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif shape_selected == shapes[4]:
      valid_shape = True
      #ask for base length
      valid_base = False
      while valid_base == False:
        try:
          base = float(input("What is the length of the base of the parallelogram? (Please enter only a number) "))
          valid_base = True
        except:
          print("Please enter a number")

      #ask for height
      valid_height = False
      while valid_height == False:
        try:
          height = float(input("What is the height of the parallelogram? (Please enter only a number) "))
          valid_height = True
        except:
          print("Please enter a number")

      #ask for the length of the side
      valid_length = False
      while valid_length == False:
        try:
          side = float(input("What is the length of the side of the parallelogram? (Please enter only a number) "))
          valid_length = True
        except:
          print("Please enter a number")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
      print("That shape is not in the list. Please enter a different shape or  check your spelling of the shape")


#Lists go under functions
shapes = ["square", "triangle", "rectangle", "circle", "parallelogram"]
triangles = ["right angle", "equilateral", "isosceles", "acute", "scalene", "obtuse"]

#Use the function
shape_picker("Choose a shape: ")

