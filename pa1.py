#c represents celsius
#f represents fahrenheit

#1.1: Implementing the function to convert from Fahrenheit to Celsius
def fahrenheit_to_celsius(temp_in_f):
    temp_in_c = (temp_in_f-32) * (5/9)
    return temp_in_c

#1.2: Implement the interaction with the user
temp_in_f_str = input('Enter temperature in fahrenheit: ' )
temp_in_f = float(temp_in_f_str)
temp_in_c = fahrenheit_to_celsius(temp_in_f)
print('Temperature in celsius =', temp_in_c)


#1.3: Implement the function to convert from Celsius to Fahrenheit
def celsius_to_fahrenheit(temp_in_c):
    temp_in_f = (temp_in_c * (9/5)) + 32
    return temp_in_f

#1.4: Converting back to Fahrenheit
temp_in_f = celsius_to_fahrenheit(temp_in_c)
print('Temperature in converted back to fahrenheit =', temp_in_f)

