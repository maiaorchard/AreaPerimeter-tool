valid_areaperimeter = False
while valid_areaperimeter == False:
  area_perimeter = input(question).lower().strip()
  if area_perimeter == "area":
    valid_areaperimeter = True
    if shape_selected == shapes[0]:
     area = (length**2)

  elif area_perimeter == "perimeter":
    valid_areaperimeter = True
    if shape_selected == shapes[0]:
      perimeter = (4*length)

  else:
      print("Please enter area or perimeter")