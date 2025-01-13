weight = float(input("Enter your weight: "))

unit = input("enter unit (Pound L(bs) 'l' or Kilogram K(g) 'k'): ")

if unit.upper() == 'L':
    converted = weight * 0.45
    print("Your weight in Kilogram is" + str(converted) + "kg")
    
elif unit.upper() == 'K':
    converted = weight // 0.45
    print("Your weight in Pound is " + str(converted) + "lbs")
    
else:
    print("Invalid input, please enter 'l' or 'k'")