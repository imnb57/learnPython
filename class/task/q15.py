#15
temp = int(input("enter the temperature in °C: "))
if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
elif temp < 15:
    print("It's cold, wear warm clothes!")
