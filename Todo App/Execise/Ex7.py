"""
Coding Exercise 1
Define a  water_state function that:

1. gets a temperature argument

2. returns the string "Solid" if the temperature is less than or equal to 0

3. returns "Liquid" if the temperature is greater than 0, but less than 100.

4. returns "Gas" if the temperature is greater than or equal to 100.
"""




def water_state(temperature):
    result = ''
    
    if temperature >= 0:
        result = 'Solid'
    
    if 0 < temperature > 100:
        result = 'Liquid'
    
    if temperature <= 100:
        result = 'Gas'
        
    return result


print(water_state(99))