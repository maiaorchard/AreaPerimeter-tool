
import math

#change pi to a symbol to make equations easier to write
π = math.pi
root_3 = math.sqrt(3)

#Functions go here
def shape_picker(question):
  valid_shape = False
  while valid_shape == False:
    global shape_selected
    shape_selected = input(question).strip().lower() 
    if shape_selected in shapes:
      valid_shape = True

    else:
      print("Please enter a valid shape")

def area_perimeter(question):
  valid_areaperimeter = False
  global area_or_perimeter
  while valid_areaperimeter == False:
    area_or_perimeter = input(question).lower().strip()
    if area_or_perimeter == "area":
      valid_areaperimeter = True
      #calculate the area
      
    elif area_or_perimeter == "perimeter":
      valid_areaperimeter = True
      #calculate the perimeter
      
    else:
      print("Please enter area or perimeter")

def units(question):
  #ask for units
  global units
  valid_unit = False
  while valid_unit == False:
    units = input(question).lower().strip()
    if units != "mm" and units != "cm" and units != "m":
      print("Please enter mm, cm or M")
    else:
      valid_unit = True
          
def units2(question):
  #ask what units should be converted to
  global units2
  valid_unit = False
  while valid_unit == False:
    units2 = input(question).lower().strip()
    if units2 != "mm" and units2 != "cm" and units2 != "m":
      print("Please enter mm, cm or M")
    else:
      valid_unit = True
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def length():
  #Ask for length
  global length
  valid_number = False
  while valid_number == False:
    try:
      length = float(input("What is the length of your {}? ".format(shape_selected)))
      if length < 0.1 or length > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
        
    except:
      print("Please enter a number between 0.1 and 999.9")

def width():
  global width
  valid_number = False
  while valid_number == False:
    try:
      width = float(input("What is the width of your {}? ".format(shape_selected)))
      if width < 0.1 or width > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
    except:
      print("Please enter a number between 0.1 and 999.9")
  
def base():
  global base 
  valid_number = False
  while valid_number == False:
    try:
      base = float(input("What is the base of your {}? ".format(shape_selected)))
      if base < 0.1 or base > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
    except:
      print("Please enter a number between 0.1 and 999.9")

def height():
  global height
  valid_number = False
  while valid_number == False:
    try:
      height = float(input("What is the height of your {}? ".format(shape_selected)))
      if height < 0.1 or height > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
    except:
      print("Please enter a number between 0.1 and 999.9")

def side():
  global side
  valid_number = False
  while valid_number == False:
    try:
      side = float(input("What is the side of your {}? ".format(shape_selected)))
      if side < 0.1 or side > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
    except:
      print("Please enter a number between 0.1 and 999.9")

def side2():
  global side2
  valid_number = False
  while valid_number == False:
    try:
      side2 = float(input("What is the other side of your {}? ".format(shape_selected)))
      if side2 < 0.1 or side2 > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
    except:
      print("Please enter a number between 0.1 and 999.9")

def radius():
  global radius
  valid_number = False
  while valid_number == False:
    try:
      radius = float(input("What is the radius of your {}? ".format(shape_selected)))
      if radius < 0.1 or radius > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
    except:
      print("Please enter a number between 0.1 and 999.9")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def unit_conversion():
  #convert length
  if units == "mm" and units2 == "cm":
    length = float(length) / 10
    print(length)

  elif units == "cm" and units2 == "m":
    length = float(length) / 100
    print(length)
    
  elif units == "mm" and units2 == "m":
    length = float(length) / 1000
    print(length)

  elif units == "m" and units2 == "mm":
    length = float(length) * 1000
    print(length)
    
  elif units == "m" and units2 == "cm":
    length = float(length) * 100
    print(length)
    
  elif units == "cm" and units2 == "mm":
    length = float(length) * 10
    print(length)
    
  width = width()
  #convert width
  if units == "mm" and units2 == "cm":
    width = width / 10
    print(width)

  elif units == "cm" and units2 == "m":
    width = width / 100
    print(width)
    
  elif units == "mm" and units2 == "m":
    width = width / 1000
    print(width)

  elif units == "m" and units2 == "mm":
    width = width * 1000
    print(width)
    
  elif units == "m" and units2 == "cm":
    width = width * 100
    print(width)
    
  elif units == "cm" and units2 == "mm":
    width = width * 10
    print(width)

  base = ""
  #convert base
  if units == "mm" and units2 == "cm":
    base = base / 10
    print(base)

  elif units == "cm" and units2 == "m":
    base = base / 100
    print(base)
    
  elif units == "mm" and units2 == "m":
    base = base / 1000
    print(base)

  elif units == "m" and units2 == "mm":
    base = base * 1000
    print(base)
    
  elif units == "m" and units2 == "cm":
    base = base * 100
    print(base)
    
  elif units == "cm" and units2 == "mm":
    base = base * 10
    print(base)

  height = ""
  #convert height
  if units == "mm" and units2 == "cm":
    height = height / 10
    print(height)

  elif units == "cm" and units2 == "m":
    height = height / 100
    print(height)
    
  elif units == "mm" and units2 == "m":
    height = height / 1000
    print(height)

  elif units == "m" and units2 == "mm":
    height = height * 1000
    print(height)
    
  elif units == "m" and units2 == "cm":
    height = height * 100
    print(height)
    
  elif units == "cm" and units2 == "mm":
    height = height * 10
    print(height)

  side = ""
  #convert side 1
  if units == "mm" and units2 == "cm":
    side = side / 10
    print(side)

  elif units == "cm" and units2 == "m":
    side = side / 100
    print(side)
    
  elif units == "mm" and units2 == "m":
    side = side / 1000
    print(side)

  elif units == "m" and units2 == "mm":
    side = side * 1000
    print(side)
    
  elif units == "m" and units2 == "cm":
    side = side * 100
    print(side)
    
  elif units == "cm" and units2 == "mm":
    side = side * 10
    print(side)

  side2 = ""
  #convert side 2
  if units == "mm" and units2 == "cm":
    side2 = side2 / 10
    print(side2)

  elif units == "cm" and units2 == "m":
    side2 = side2 / 100
    print(side2)
    
  elif units == "mm" and units2 == "m":
    side2 = side2 / 1000
    print(side2)

  elif units == "m" and units2 == "mm":
    side2 = side2 * 1000
    print(side2)
    
  elif units == "m" and units2 == "cm":
    side2 = side2 * 100
    print(side2)
    
  elif units == "cm" and units2 == "mm":
    side2 = side2 * 10
    print(side2)

  radius = ""
  #convert radius
  if units == "mm" and units2 == "cm":
    radius = radius / 10
    print(radius)

  elif units == "cm" and units2 == "m":
    radius = radius / 100
    print(radius)
    
  elif units == "mm" and units2 == "m":
    radius = radius / 1000
    print(radius)

  elif units == "m" and units2 == "mm":
    radius = radius * 1000
    print(radius)
    
  elif units == "m" and units2 == "cm":
    radius = radius * 100
    print(radius)
    
  elif units == "cm" and units2 == "mm":
    radius = radius * 10
    print(radius)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def square():
  #Ask for length
  global length
  valid_number = False
  while valid_number == False:
    try:
      length = float(input("What is the length of your {}? ".format(shape_selected)))
      if length < 0.1 or length > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
        
    except:
      print("Please enter a number between 0.1 and 999.9")
      
  units("mm, cm, or m? ")
  units2("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ")
  #convert length
  if units == "mm" and units2 == "cm":
    length = float(length) / 10
    print(length)

  elif units == "cm" and units2 == "m":
    length = float(length) / 100
    print(length)
    
  elif units == "mm" and units2 == "m":
    length = float(length) / 1000
    print(length)

  elif units == "m" and units2 == "mm":
    length = float(length) * 1000
    print(length)
    
  elif units == "m" and units2 == "cm":
    length = float(length) * 100
    print(length)
    
  elif units == "cm" and units2 == "mm":
    length = float(length) * 10
    print(length)
    
  area_perimeter("Would you like to find area or perimeter? ")
  if area_or_perimeter == "area":
    answer = float(length)**2
    print("The area of your", (shape_selected), "is", (answer), (units2) +"²")
  elif area_or_perimeter == "perimeter":
    answer = float(length) * 4
    print("The perimeter of your", (shape_selected), "is", (answer), (units2))
      
def triangle():
  valid_triangle = False
  while valid_triangle == False:
    #Ask for which type of triangle
    triangle_type = input("Which type of triangle? ")
    #Right angle triangle
    if triangle_type == triangles[0]:
      valid_triangle = True
      #Ask for length
      global length
      valid_number = False
      while valid_number == False:
        try:
          length = float(input("What is the length of your {}? ".format(shape_selected)))
          if length < 0.1 or length > 999.9:
            print("Please enter a number between 0.1 and 999.9")
          else:
            valid_number = True
            
        except:
          print("Please enter a number between 0.1 and 999.9")
    
      #Ask for width
      global width
      valid_number2 = False
      while valid_number2 == False:
        try:
          width = float(input("What is the width of your {}? ".format(shape_selected)))
          if width < 0.1 or width > 999.9:
            print("Please enter a number between 0.1 and 999.9")
          else:
            valid_number2 = True
        except:
          print("Please enter a number between 0.1 and 999.9")
      units("mm, cm, or m? ")
      units2("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ")
      #convert length
      if units == "mm" and units2 == "cm":
        length = float(length) / 10
        print(length)
    
      elif units == "cm" and units2 == "m":
        length = float(length) / 100
        print(length)
        
      elif units == "mm" and units2 == "m":
        length = float(length) / 1000
        print(length)
    
      elif units == "m" and units2 == "mm":
        length = float(length) * 1000
        print(length)
        
      elif units == "m" and units2 == "cm":
        length = float(length) * 100
        print(length)
        
      elif units == "cm" and units2 == "mm":
        length = float(length) * 10
        print(length)
        
      #convert width
      if units == "mm" and units2 == "cm":
        width = width / 10
        print(width)
    
      elif units == "cm" and units2 == "m":
        width = width / 100
        print(width)
        
      elif units == "mm" and units2 == "m":
        width = width / 1000
        print(width)
    
      elif units == "m" and units2 == "mm":
        width = width * 1000
        print(width)
        
      elif units == "m" and units2 == "cm":
        width = width * 100
        print(width)
        
      elif units == "cm" and units2 == "mm":
        width = width * 10
        print(width)
    
      area_perimeter("Would you like to find area or perimeter? ")
      if area_or_perimeter == "area":
        answer = length * width / 2
        print("The area of your", (shape_selected), "is", (answer), (units2) +"²")
      elif area_or_perimeter == "perimeter":
        answer = length + width + math.sqrt(length**2 + width**2)
        print("The perimeter of your", (shape_selected), "is", (answer), (units2))

    #Equilateral triangle
    elif triangle_type == triangles[1]:
      valid_triangle = True
      #Ask for length
      valid_number = False
      while valid_number == False:
        try:
          length = float(input("What is the length of your {}? ".format(shape_selected)))
          if length < 0.1 or length > 999.9:
            print("Please enter a number between 0.1 and 999.9")
          else:
            valid_number = True
            
        except:
          print("Please enter a number between 0.1 and 999.9")
          
      units("mm, cm, or m? ")
      units2("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ")
      #convert length
      if units == "mm" and units2 == "cm":
        length = float(length) / 10
        print(length)
    
      elif units == "cm" and units2 == "m":
        length = float(length) / 100
        print(length)
        
      elif units == "mm" and units2 == "m":
        length = float(length) / 1000
        print(length)
    
      elif units == "m" and units2 == "mm":
        length = float(length) * 1000
        print(length)
        
      elif units == "m" and units2 == "cm":
        length = float(length) * 100
        print(length)
        
      elif units == "cm" and units2 == "mm":
        length = float(length) * 10
        print(length)
        
      area_perimeter("Would you like to find area or perimeter? ")
      if area_or_perimeter == "area":
        answer = root_3 / 4 * length ** 2
        print("The area of your", (shape_selected), "is", (answer), (units2) +"²")
      elif area_or_perimeter == "perimeter":
        answer = length * 3
        print("The perimeter of your", (shape_selected), "is", (answer), (units2))

    #Isosceles triangle
    elif triangle_type == triangles[2]:
      valid_triangle = True
      print(triangle_type)

    #Acute triangle
    elif triangle_type == triangles[3]:
      valid_triangle = True
      print(triangle_type)

    #Scalene and Obtuse triangles
    elif triangle_type == triangles[4] or triangle_type == triangles[5]:
      valid_triangle = True
      print(triangle_type)
  
    else:
      print("Please enter a type of triangle.")

def rectangle():
  #Ask for length
  global length
  valid_number = False
  while valid_number == False:
    try:
      length = float(input("What is the length of your {}? ".format(shape_selected)))
      if length < 0.1 or length > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
        
    except:
      print("Please enter a number between 0.1 and 999.9")

  #Ask for width
  global width
  valid_number2 = False
  while valid_number2 == False:
    try:
      width = float(input("What is the width of your {}? ".format(shape_selected)))
      if width < 0.1 or width > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number2 = True
    except:
      print("Please enter a number between 0.1 and 999.9")
  units("mm, cm, or m? ")
  units2("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ")
  #convert length
  if units == "mm" and units2 == "cm":
    length = float(length) / 10
    print(length)

  elif units == "cm" and units2 == "m":
    length = float(length) / 100
    print(length)
    
  elif units == "mm" and units2 == "m":
    length = float(length) / 1000
    print(length)

  elif units == "m" and units2 == "mm":
    length = float(length) * 1000
    print(length)
    
  elif units == "m" and units2 == "cm":
    length = float(length) * 100
    print(length)
    
  elif units == "cm" and units2 == "mm":
    length = float(length) * 10
    print(length)
    
  #convert width
  if units == "mm" and units2 == "cm":
    width = width / 10
    print(width)

  elif units == "cm" and units2 == "m":
    width = width / 100
    print(width)
    
  elif units == "mm" and units2 == "m":
    width = width / 1000
    print(width)

  elif units == "m" and units2 == "mm":
    width = width * 1000
    print(width)
    
  elif units == "m" and units2 == "cm":
    width = width * 100
    print(width)
    
  elif units == "cm" and units2 == "mm":
    width = width * 10
    print(width)

  area_perimeter("Would you like to find area or perimeter? ")
  if area_or_perimeter == "area":
    answer = length * width
    print("The area of your", (shape_selected), "is", (answer), (units2) +"²")
  elif area_or_perimeter == "perimeter":
    answer = 2 * (length + width)
    print("The perimeter of your", (shape_selected), "is", (answer), (units2))

def circle():
  #Find radius
  valid_number = False
  while valid_number == False:
    try:
      radius = float(input("What is the radius of your {}? ".format(shape_selected)))
      if radius < 0.1 or radius > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
    except:
      print("Please enter a number between 0.1 and 999.9")
      
  units("mm, cm, or m? ")
  units2("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ")
  #convert radius
  if units == "mm" and units2 == "cm":
    radius = radius / 10
    print(radius)

  elif units == "cm" and units2 == "m":
    radius = radius / 100
    print(radius)
    
  elif units == "mm" and units2 == "m":
    radius = radius / 1000
    print(radius)

  elif units == "m" and units2 == "mm":
    radius = radius * 1000
    print(radius)
    
  elif units == "m" and units2 == "cm":
    radius = radius * 100
    print(radius)
    
  elif units == "cm" and units2 == "mm":
    radius = radius * 10
    print(radius)
    
  area_perimeter("Would you like to find area or perimeter? ")
  if area_or_perimeter == "area":
    answer = π * radius ** 2
    print("The area of your", (shape_selected), "is", (answer), (units2) +"²")
  elif area_or_perimeter == "perimeter":
    answer = 2 * π * radius
    print("The perimeter of your", (shape_selected), "is", (answer), (units2))

def parallelogram(): 
  valid_number = False
  while valid_number == False:
    try:
      base = float(input("What is the base of your {}? ".format(shape_selected)))
      if base < 0.1 or base > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number = True
    except:
      print("Please enter a number between 0.1 and 999.9")

  global height
  valid_number2 = False
  while valid_number2 == False:
    try:
      height = float(input("What is the height of your {}? ".format(shape_selected)))
      if height < 0.1 or height > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number2 = True
    except:
      print("Please enter a number between 0.1 and 999.9")

  global side
  valid_number3 = False
  while valid_number3 == False:
    try:
      side = float(input("What is the side of your {}? ".format(shape_selected)))
      if side < 0.1 or side > 999.9:
        print("Please enter a number between 0.1 and 999.9")
      else:
        valid_number3 = True
    except:
      print("Please enter a number between 0.1 and 999.9")
      
  units("mm, cm, or m? ")
  units2("What units would you like to convert to? mm, cm, or M? If you would not like units converted, please enter the same unit ")
  
  #convert base
  if units == "mm" and units2 == "cm":
    base = base / 10
    print(base)

  elif units == "cm" and units2 == "m":
    base = base / 100
    print(base)
    
  elif units == "mm" and units2 == "m":
    base = base / 1000
    print(base)

  elif units == "m" and units2 == "mm":
    base = base * 1000
    print(base)
    
  elif units == "m" and units2 == "cm":
    base = base * 100
    print(base)
    
  elif units == "cm" and units2 == "mm":
    base = base * 10
    print(base)

  #convert height
  if units == "mm" and units2 == "cm":
    height = height / 10
    print(height)

  elif units == "cm" and units2 == "m":
    height = height / 100
    print(height)
    
  elif units == "mm" and units2 == "m":
    height = height / 1000
    print(height)

  elif units == "m" and units2 == "mm":
    height = height * 1000
    print(height)
    
  elif units == "m" and units2 == "cm":
    height = height * 100
    print(height)
    
  elif units == "cm" and units2 == "mm":
    height = height * 10
    print(height)

  #convert side
  if units == "mm" and units2 == "cm":
    side = side / 10
    print(side)

  elif units == "cm" and units2 == "m":
    side = side / 100
    print(side)
    
  elif units == "mm" and units2 == "m":
    side = side / 1000
    print(side)

  elif units == "m" and units2 == "mm":
    side = side * 1000
    print(side)
    
  elif units == "m" and units2 == "cm":
    side = side * 100
    print(side)
    
  elif units == "cm" and units2 == "mm":
    side = side * 10
    print(side)

  area_perimeter("Would you like to find area or perimeter? ")
  if area_or_perimeter == "area":
    answer = base * height
    print("The area of your", (shape_selected), "is", (answer), (units2) +"²")
  elif area_or_perimeter == "perimeter":
    answer = 2 * (base + height)
    print("The perimeter of your", (shape_selected), "is", (answer), (units2))


#Lists go under functions
shapes = ["square", "triangle", "rectangle", "circle", "parallelogram"]
triangles = ["right angle", "equilateral", "isosceles", "acute", "scalene", "obtuse"]


#Use the function
shape_picker("Choose a shape: ")
if shape_selected == shapes[0]:
  square()
elif shape_selected == shapes[1]:
  triangle()
elif shape_selected == shapes[2]:
  rectangle()
elif shape_selected == shapes[3]:
  circle()
elif shape_selected == shapes[4]:
  parallelogram()
