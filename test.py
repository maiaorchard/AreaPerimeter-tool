valid = False
while valid == False:
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