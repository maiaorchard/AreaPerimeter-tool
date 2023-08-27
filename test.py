
valid_areaperimeter = False
while valid_areaperimeter == False:
  area_or_perimeter = input("Would you like to calculate area or perimeter? ").lower().strip()
  if area_or_perimeter == "area":
    #valid_areaperimeter = True
    print(area_or_perimeter)
  elif area_or_perimeter == "perimeter":
    #valid_areaperimeter = True
    print(area_or_perimeter)
  else:
    print("Please enter area or perimeter")