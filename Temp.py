temp = float(input("Enter today's temperature: "))
unit = input("Is it in Celsius or Fahrenheit (C/S) : ").lower()
if unit == "c":
    temp = round(temp * 9 / 5 + 32),2
    print (f"The temperature in Fahrenheit is {temp}°F")

elif unit == "f":
    temp = round((temp - 32)*5/9),2
    print (f"The temperature in Celsius is {temp}°C")

else:
  print ("Please enter a valid unit")



