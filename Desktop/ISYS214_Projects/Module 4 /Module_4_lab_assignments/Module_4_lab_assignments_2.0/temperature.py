from microbit import *
import utime

# Initialize variables to store the highest and lowest temperatures
highest_temp = None
lowest_temp = None

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to update the highest and lowest temperatures
def update_temperature_records(current_temp):
    global highest_temp, lowest_temp
    if highest_temp is None or current_temp > highest_temp:
        highest_temp = current_temp
    if lowest_temp is None or current_temp < lowest_temp:
        lowest_temp = current_temp

while True:
    # Get the current temperature in Celsius
    current_temp_celsius = temperature()
    # Convert the temperature to Fahrenheit
    current_temp_fahrenheit = celsius_to_fahrenheit(current_temp_celsius)
    
    # Update the highest and lowest temperature records
    update_temperature_records(current_temp_fahrenheit)
    
    # Display the current temperature in Fahrenheit
    display.scroll(str(current_temp_fahrenheit) + "F")
    
    # Check if button A is pressed to display the highest temperature
    if button_a.is_pressed():
        if highest_temp is not None:
            display.scroll("High: " + str(highest_temp) + "F")
        else:
            display.scroll("No data")
    
    # Check if button B is pressed to display the lowest temperature
    if button_b.is_pressed():
        if lowest_temp is not None:
            display.scroll("Low: " + str(lowest_temp) + "F")
        else:
            display.scroll("No data")
    
    # Wait for one minute before taking the next reading
    utime.sleep(60)