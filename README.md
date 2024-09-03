
# Temperature Conversion
![gbase](https://d20khd7ddkh5ls.cloudfront.net/fandctempconversion.jpg)


Hi!

The purpose of this program is to use the Micro:bit's platform which provides a block-based interface for programming the micro:bit

## Overview
This project uses the Micro:bit's built-in temperature sensor to continuously monitor the temperature, convert it from Celsius to Fahrenheit, and keep track of the highest and lowest recorded temperatures. The current, highest, and lowest temperatures can be displayed using the Micro:bit's LED display and buttons.

## Instructions

### To build this project using the Micro:bit blocks in the MakeCode editor, follow these detailed steps:

### Step-by-Step Guide

#### 1. Initialize Variables
1. Go to the **Variables** category.
2. Click on **Make a Variable** and create two variables: `highest_temp` and `lowest_temp`.
3. Set `highest_temp` to a very low value (e.g., -999) and `lowest_temp` to a very high value (e.g., 999).

#### 2. Convert Celsius to Fahrenheit Function
1. Go to the **Functions** category.
2. Click on **Make a Function** and name it `celsius_to_fahrenheit`.
3. Add a parameter named `celsius`.
4. Inside the function, use the **Math** blocks to calculate `(celsius * 9 / 5) + 32` and return the result.

#### 3. Update Temperature Records Function
1. Create another function named `update_temperature_records`.
2. Add a parameter named `current_temp`.
3. Inside the function, use **if** statements to update `highest_temp` and `lowest_temp` if `current_temp` is higher or lower than the current values.

#### 4. Main Loop
1. Use a **forever** loop to continuously read the temperature, convert it, update records, and display the current temperature.
2. Use `input.onButtonPressed(Button.A, function () { ... })` to display the highest temperature.
3. Use `input.onButtonPressed(Button.B, function () { ... })` to display the lowest temperature.
4. Use a **pause** block to wait for one minute (60000 milliseconds) before taking the next reading.

### Complete Block-Based Implementation
Here is the complete block-based implementation in the MakeCode editor:
#### Initialize Variables
```
highest_temp = -999
lowest_temp = 999

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def update_temperature_records(current_temp):
    global highest_temp, lowest_temp
    if highest_temp == -999 or current_temp > highest_temp:
        highest_temp = current_temp
    if lowest_temp == 999 or current_temp < lowest_temp:
        lowest_temp = current_temp

def main_loop():
    import time
    while True:
        current_temp = get_current_temperature()  # Placeholder for actual temperature reading function
        current_temp_fahrenheit = celsius_to_fahrenheit(current_temp)
        update_temperature_records(current_temp)
        show_number(current_temp_fahrenheit)  # Placeholder for actual display function
        time.sleep(60)

def on_button_pressed_a():
    show_string("High: ")  # Placeholder for actual display function
    show_number(highest_temp)  # Placeholder for actual display function

def on_button_pressed_b():
    show_string("Low: ")  # Placeholder for actual display function
    show_number(lowest_temp)  # Placeholder for actual display function

# Placeholder functions for temperature reading and display
def get_current_temperature():
    # This function should return the current temperature in Celsius
    return 25  # Example temperature

def show_number(number):
    print(number)

def show_string(string):
    print(string)
```
#### Questions
```
1 - What is the purpose of setting highest_temp to -999 and lowest_temp to 999 initially?
      -- This ensures that any real temperature reading will update these variables correctly._
 
2 - How does the celsius_to_fahrenheit function work?
     --  It converts a temperature from Celsius to Fahrenheit using the formula (celsius * 9 / 5) + 32.

3 - What happens when Button A is pressed?
      -- The highest recorded temperature is displayed on the Micro:bit's LED display .

4-  What happens when Button B is pressed?
      -- The lowest recorded temperature is displayed on the Micro:bit's LED display.

5 - Why is there a pause of 60000 milliseconds in the main loop?
      -- This pause ensures that the temperature is read and updated every minute.
```

 #### Conclusion


By following these steps, you can create a Micro:bit project that continuously monitors temperature, converts it to Fahrenheit, and keeps track of the highest and lowest temperatures. This project is a great way to learn about temperature conversion and data logging using the Micro:bit's block-based programming interface.
