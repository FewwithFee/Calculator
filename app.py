# Weight converter
user_weight = input("Please enter your weight: ")
user_unit = input("Pounds (L) or Kilograms (K) :")
if user_unit == "L" or "l":
    weight_in_kg = float(user_weight) / 2.2
    print (f"Your weight is {weight_in_kg} Kg")
elif user_unit == "K" or "k":
    weight_in_kg = float(user_weight) * 2.2
    print (f"Your weight is {weight_in_kg} Kg")