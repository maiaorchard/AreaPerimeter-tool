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