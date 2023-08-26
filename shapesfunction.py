
#Functions go at the top
def shape_picker(question):
  valid_shape = False
  while valid_shape == False:
    shape_selected = input(question).strip().lower()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if shape_selected == shapes[0]:
      valid_shape = True
      
      #ask for the length
      valid_number = False
      while valid_number == False:
        try:
          length = float(input("What is the length of the square? (Please enter only a number) "))
          if length > 999.9:
            print("Number is too high")
          elif length < 0.1:
            print("Number is too low")
          else:
            valid_number = True
        except:
          print("Please enter a number")
      
      #ask for units
      valid_unit = False
      while valid_unit == False:
        units = input("mm, cm, or M? ").lower().strip()
        if units != "mm" and units != "cm" and units != "m":
          print("Please enter mm, cm or M")
        else:
          valid_unit = True
          #ask what units it should be converted to
          valid_unit2 = False
          while valid_unit2 == False:
            unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
            if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
              print("Please enter mm, cm or M")
            else:
              valid_unit2 = True

      if units == "mm" and unit2 == "cm":
        length = length / 10
        print(length)

      elif units == "cm" and unit2 == "m":
        length = length / 100
        print(length)
        
      elif units == "mm" and unit2 == "m":
        length = length / 1000
        print(length)

      elif units == "m" and unit2 == "mm":
        length = length * 1000
        print(length)
        
      elif units == "m" and unit2 == "cm":
        length = length * 100
        print(length)
        
      elif units == "cm" and unit2 == "mm":
        length = length * 10
        print(length)
      
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
              if length > 999.9:
                print("Number is too high")
              elif length < 0.1:
                print("Number is too low")
              else:
                valid_length = True
              
            except:
              print("Please enter a number")

          #ask for width
          valid_width = False
          while valid_width == False:
            try:
              width = float(input("What is the width of the triangle? (Please enter only a number) "))
              if width > 999.9:
                print("Number is too high")
              elif width < 0.1:
                print("Number is too low")
              else:
                valid_width = True
            except:
              print("Please enter a number")
          #ask for units
          valid_unit = False
          while valid_unit == False:
            units = input("mm, cm, or M? ").lower().strip()
            if units != "mm" and units != "cm" and units != "m":
              print("Please enter mm, cm or M")
            else:
              valid_unit = True
              #ask what units it should be converted to
              valid_unit2 = False
              while valid_unit2 == False:
                unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
                if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
                  print("Please enter mm, cm or M")
                else:
                  valid_unit2 = True
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif triangle_type == triangles[1]:
          valid_triangle = True
          #ask for length
          valid_length = False
          while valid_length == False:
            try:
              length = float(input("What is the length of the triangle? (Please enter only a number) "))
              if length > 999.9:
                print("Number is too high")
              elif length < 0.1:
                print("Number is too low")
              else:
                valid_length = True
            except:
              print("Please enter a number")
          #ask for units
          valid_unit = False
          while valid_unit == False:
            units = input("mm, cm, or M? ").lower().strip()
            if units != "mm" and units != "cm" and units != "m":
             print("Please enter mm, cm or M")
            else:
              valid_unit = True
              #ask what units it should be converted to
              valid_unit2 = False
              while valid_unit2 == False:
                unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
                if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
                  print("Please enter mm, cm or M")
                else:
                  valid_unit2 = True
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif triangle_type == triangles[2]:
          valid_triangle = True
          #ask for base length
          valid_base = False
          while valid_base == False:
            try:
              base = float(input("What is the length of the base of the triangle? (Please enter only a number) "))
              if base > 999.9:
                print("Number is too high")
              elif base < 0.1:
                print("Number is too low")
              else:
                valid_base = True
            except:
              print("Please enter a number")

          #ask for height
          valid_height = False
          while valid_height == False:
            try:
              height = float(input("What is the height of the triangle? (Please enter only a number) "))
              if height > 999.9:
                print("Number is too high")
              elif height < 0.1:
                print("Number is too low")
              else:
                valid_height = True
            except:
              print("Please enter a number")

          #ask for the length of the side
          valid_length = False
          while valid_length == False:
            try:
              side = float(input("What is the length of the side of the triangle? (Please enter only a number) "))
              if side > 999.9:
                print("Number is too high")
              elif side < 0.1:
                print("Number is too low")
              else:
                valid_length = True
            except:
              print("Please enter a number")
          #ask for units
          valid_unit = False
          while valid_unit == False:
            units = input("mm, cm, or M? ").lower().strip()
            if units != "mm" and units != "cm" and units != "m":
              print("Please enter mm, cm or M")
            else:
              valid_unit = True
              #ask what units it should be converted to
              valid_unit2 = False
              while valid_unit2 == False:
                unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
                if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
                  print("Please enter mm, cm or M")
                else:
                  valid_unit2 = True
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif triangle_type == triangles[3]:
          valid_triangle = True
          #ask for base measurement
          valid_base = False
          while valid_base == False:
            try:
              base = float(input("What is the length of the base of the triangle? (Please enter only a number) "))
              if base > 999.9:
                print("Number is too high")
              elif base < 0.1:
                print("Number is too low")
              else:
                valid_base = True
            except:
              print("Please enter a number")

          #ask for height
          valid_height = False
          while valid_height == False:
            try:
              height = float(input("What is the height of the triangle? (Please enter only a number) "))
              if height > 999.9:
                print("Number is too high")
              elif height < 0.1:
                print("Number is too low")
              else:
                valid_height = True
            except:
              print("Please enter a number")

          #ask for the length of one side
          valid_length = False
          while valid_length == False:
            try:
              side = float(input("What is the length of one side of the triangle? (Please enter only a number) "))
              if side > 999.9:
                print("Number is too high")
              elif side < 0.1:
                print("Number is too low")
              else:
                valid_length = True
            except:
              print("Please enter a number")

          #ask for the length of the other side
          valid_length2 = False
          while valid_length2 == False:
            try:
              side2 = float(input("What is the length of the other side of the triangle? (Please enter only a number) "))
              if side2 > 999.9:
                print("Number is too high")
              elif side2 < 0.1:
                print("Number is too low")
              else:
                valid_length2 = True
            except:
              print("Please enter a number")
          #ask for units
          valid_unit = False
          while valid_unit == False:
            units = input("mm, cm, or M? ").lower().strip()
            if units != "mm" and units != "cm" and units != "m":
              print("Please enter mm, cm or M")
            else:
              valid_unit = True
              #ask what units it should be converted to
              valid_unit2 = False
              while valid_unit2 == False:
                unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
                if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
                  print("Please enter mm, cm or M")
                else:
                  valid_unit2 = True
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif triangle_type == triangles[4] or triangle_type == triangles[5]:
          valid_triangle = True
          #ask for base measurement
          valid_base = False
          while valid_base == False:
            try:
              base = float(input("What is the length of the base of the triangle? (Please enter only a number) "))
              if base > 999.9:
                print("Number is too high")
              elif base < 0.1:
                print("Number is too low")
              else:
                valid_base = True
            except:
              print("Please enter a number")

          #ask for height
          valid_height = False
          while valid_height == False:
            try:
              height = float(input("What is the height of the triangle? (Please enter only a number) "))
              if height > 999.9:
                print("Number is too high")
              elif height < 0.1:
                print("Number is too low")
              else:
                valid_height = True
            except:
              print("Please enter a number")

          #ask for the length of one side
          valid_length = False
          while valid_length == False:
            try:
              side = float(input("What is the length of one side of the triangle? (Please enter only a number) "))
              if side > 999.9:
                print("Number is too high")
              elif side < 0.1:
                print("Number is too low")
              else:
                valid_length = True
            except:
              print("Please enter a number")

          #ask for the length of the other side
          valid_length2 = False
          while valid_length2 == False:
            try:
              side2 = float(input("What is the length of the other side of the triangle? (Please enter only a number) "))
              if side2 > 999.9:
                print("Number is too high")
              elif side2 < 0.1:
                print("Number is too low")
              else:
                valid_length2 = True
            except:
              print("Please enter a number")
          #ask for units
          valid_unit = False
          while valid_unit == False:
            units = input("mm, cm, or M? ").lower().strip()
            if units != "mm" and units != "cm" and units != "m":
              print("Please enter mm, cm or M")
            else:
              valid_unit = True
              #ask what units it should be converted to
              valid_unit2 = False
              while valid_unit2 == False:
                unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
                if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
                  print("Please enter mm, cm or M")
                else:
                  valid_unit2 = True
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
              length = float(input("What is the length of the triangle? (Please enter only a number) "))
              if length > 999.9:
                print("Number is too high")
              elif length < 0.1:
                print("Number is too low")
              else:
                valid_length = True
              
            except:
              print("Please enter a number")

      #ask for width
      valid_width = False
      while valid_width == False:
        try:
          width = float(input("What is the width of the triangle? (Please enter only a number) "))
          if width > 999.9:
            print("Number is too high")
          elif width < 0.1:
            print("Number is too low")
          else:
            valid_width = True
        except:
          print("Please enter a number")
      #ask for units
      valid_unit = False
      while valid_unit == False:
        units = input("mm, cm, or M? ").lower().strip()
        if units != "mm" and units != "cm" and units != "m":
          print("Please enter mm, cm or M")
        else:
          valid_unit = True
          #ask what units it should be converted to
          valid_unit2 = False
          while valid_unit2 == False:
            unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
            if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
              print("Please enter mm, cm or M")
            else:
              valid_unit2 = True
              
      #convert length
      if units == "mm" and unit2 == "cm":
        length = length / 10
        print(length)

      elif units == "cm" and unit2 == "m":
        length = length / 100
        print(length)
        
      elif units == "mm" and unit2 == "m":
        length = length / 1000
        print(length)

      elif units == "m" and unit2 == "mm":
        length = length * 1000
        print(length)
        
      elif units == "m" and unit2 == "cm":
        length = length * 100
        print(length)
        
      elif units == "cm" and unit2 == "mm":
        length = length * 10
        print(length)
        
      #convert width
      if units == "mm" and unit2 == "cm":
        width = width / 10
        print(width)

      elif units == "cm" and unit2 == "m":
        width = width / 100
        print(width)
        
      elif units == "mm" and unit2 == "m":
        width = width / 1000
        print(width)

      elif units == "m" and unit2 == "mm":
        width = width * 1000
        print(width)
        
      elif units == "m" and unit2 == "cm":
        width = width * 100
        print(width)
        
      elif units == "cm" and unit2 == "mm":
        width = width * 10
        print(width)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif shape_selected == shapes[3]:
      valid_shape = True
      #ask for radius
      valid_radius = False
      while valid_radius == False:
        try: 
          radius = float(input("What is the radius of the circle? (Please enter only a number) "))
          if radius > 999.9:
            print("Number is too high")
          elif radius < 0.1:
            print("Number is too low")
          else:
            valid_radius = True
        except:
          print("Please enter a number")
      #ask for units 
      valid_unit = False
      while valid_unit == False:
        units = input("mm, cm, or M? ").lower().strip()
        if units != "mm" and units != "cm" and units != "m":
          print("Please enter mm, cm or M")
        else:
          valid_unit = True
          #ask what units it should be converted to
          valid_unit2 = False
          while valid_unit2 == False:
            unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
            if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
              print("Please enter mm, cm or M")
            else:
              valid_unit2 = True
      #convert radius
      if units == "mm" and unit2 == "cm":
        radius = radius / 10
        print(radius)

      elif units == "cm" and unit2 == "m":
        radius = radius / 100
        print(radius)
        
      elif units == "mm" and unit2 == "m":
        radius = radius / 1000
        print(radius)

      elif units == "m" and unit2 == "mm":
        radius = radius * 1000
        print(radius)
        
      elif units == "m" and unit2 == "cm":
        radius = radius * 100
        print(radius)
        
      elif units == "cm" and unit2 == "mm":
        radius = radius * 10
        print(radius)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif shape_selected == shapes[4]:
      valid_shape = True
      #ask for base length
      valid_base = False
      while valid_base == False:
        try:
          base = float(input("What is the length of the base of the parallelogram? (Please enter only a number) "))
          if base > 999.9:
             print("Number is too high")
          elif base < 0.1:
             print("Number is too low")
          else:
            valid_base = True
        except:
          print("Please enter a number")

      #ask for height
      valid_height = False
      while valid_height == False:
        try:
          height = float(input("What is the height of the parallelogram? (Please enter only a number) "))
          if height > 999.9:
            print("Number is too high")
          elif height < 0.1:
            print("Number is too low")
          else:
            valid_height = True
        except:
          print("Please enter a number")

        #ask for the length of the side
      valid_length = False
      while valid_length == False:
        try:
          side = float(input("What is the length of the side of the parallelogram? (Please enter only a number) "))
          if side > 999.9:
            print("Number is too high")
          elif side < 0.1:
            print("Number is too low")
          else:
            valid_length = True
        
        except:
          print("Please enter a number")
      #ask for units
      valid_unit = False
      while valid_unit == False:
        units = input("mm, cm, or M? ").lower().strip()
        if units != "mm" and units != "cm" and units != "m":
          print("Please enter mm, cm or M")
        else:
          valid_unit = True
          #ask what units it should be converted to
          valid_unit2 = False
          while valid_unit2 == False:
            unit2 = input("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ").lower().strip()
            if unit2 != "mm" and unit2 != "cm" and unit2 != "m":
              print("Please enter mm, cm or M")
            else:
              valid_unit2 = True
      #convert base
      if units == "mm" and unit2 == "cm":
        base = base / 10
        print(base)

      elif units == "cm" and unit2 == "m":
        base = base / 100
        print(base)
        
      elif units == "mm" and unit2 == "m":
        base = base / 1000
        print(base)

      elif units == "m" and unit2 == "mm":
        base = base * 1000
        print(base)
        
      elif units == "m" and unit2 == "cm":
        base = base * 100
        print(base)
        
      elif units == "cm" and unit2 == "mm":
        base = base * 10
        print(base)

      #convert height
      if units == "mm" and unit2 == "cm":
        height = height / 10
        print(height)

      elif units == "cm" and unit2 == "m":
        height = height / 100
        print(height)
        
      elif units == "mm" and unit2 == "m":
        height = height / 1000
        print(height)

      elif units == "m" and unit2 == "mm":
        height = height * 1000
        print(height)
        
      elif units == "m" and unit2 == "cm":
        height = height * 100
        print(height)
        
      elif units == "cm" and unit2 == "mm":
        height = height * 10
        print(height)

      #convert side
      if units == "mm" and unit2 == "cm":
        side = side / 10
        print(side)

      elif units == "cm" and unit2 == "m":
        side = side / 100
        print(side)
        
      elif units == "mm" and unit2 == "m":
        side = side / 1000
        print(side)

      elif units == "m" and unit2 == "mm":
        side = side * 1000
        print(side)
        
      elif units == "m" and unit2 == "cm":
        side = side * 100
        print(side)
        
      elif units == "cm" and unit2 == "mm":
        side = side * 10
        print(side)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
      print("That shape is not in the list. Please enter a different shape or  check your spelling of the shape")


#Lists go under functions
shapes = ["square", "triangle", "rectangle", "circle", "parallelogram"]
triangles = ["right angle", "equilateral", "isosceles", "acute", "scalene", "obtuse"]

#Use the function
shape_picker("Choose a shape: ")

