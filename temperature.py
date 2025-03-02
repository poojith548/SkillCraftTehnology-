def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("Choose the input temperature scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    input_choice = int(input("Enter your choice: "))

    input_temp = float(input("Enter the temperature value: "))

    print("Choose the output temperature scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    output_choice = int(input("Enter your choice: "))

    converted_temp = 0

    if input_choice == 1:
        if output_choice == 1:
            converted_temp = input_temp
        elif output_choice == 2:
            converted_temp = celsius_to_fahrenheit(input_temp)
        elif output_choice == 3:
            converted_temp = celsius_to_kelvin(input_temp)
    elif input_choice == 2:
        if output_choice == 1:
            converted_temp = fahrenheit_to_celsius(input_temp)
        elif output_choice == 2:
            converted_temp = input_temp
        elif output_choice == 3:
            converted_temp = fahrenheit_to_kelvin(input_temp)
    elif input_choice == 3:
        if output_choice == 1:
            converted_temp = kelvin_to_celsius(input_temp)
        elif output_choice == 2:
            converted_temp = kelvin_to_fahrenheit(input_temp)
        elif output_choice == 3:
            converted_temp = input_temp
    else:
        print("Invalid input choice.")
        return

    scales = ["Celsius", "Fahrenheit", "Kelvin"]
    print(f"Converted temperature: {converted_temp:.2f} {scales[output_choice - 1]}")

if __name__ == "_main_":
    main()