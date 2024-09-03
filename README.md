
# Temperature Conversion
![gbase](https://d20khd7ddkh5ls.cloudfront.net/fandctempconversion.jpg)![gbase](https://projects-static.raspberrypi.org/projects/music-player/89cc4ed5bc97a43116eb06d3d090454b038dac79/en/images/banner.png) 

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
```blocks
let highest_temp = -999
let lowest_temp = 999
Copy
Insert
Convert Celsius to Fahrenheit Function
function celsius_to_fahrenheit(celsius: number): number {
    return (celsius * 9 / 5) + 32
}
Update Temperature Records Function
function update_temperature_records(current_temp: number) {
    if (highest_temp == -999 || current_temp > highest_temp) {
        highest_temp = current_temp
    }
    if (lowest_temp == 999 || current_temp < lowest_temp) {
        lowest_temp = current_temp
Main Loop
basic.forever(function () {
    let current_temp = input.temperature()
    let current_temp_fahrenheit = celsius_to_fahrenheit(current_temp)
    update_temperature_records(current_temp)
    basic.showNumber(current_temp_fahrenheit)
    basic.pause(60000)
})
input.onButtonPressed(Button.A, function () {
    basic.showString("High: ")
    basic.showNumber(highest_temp)
input.onButtonPressed(Button.B, function () {
    basic.showString("Low: ")
    basic.showNumber(lowest_temp)
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
```

By following these steps, you can create a Micro:bit project that continuously monitors temperature, converts it to Fahrenheit, and keeps track of the highest and lowest temperatures. This project is a great way to learn about temperature conversion and data logging using the Micro:bit's block-based programming interface.
