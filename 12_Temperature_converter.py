class Temperatur_Converter:
     @staticmethod
     def celsius_to_fahrenheit(celsius):
          fahrenheit = (celsius * 9/5) + 32
          return fahrenheit
celsius = float(input("Enter temperature in Celsius: "))     
temp_1 = Temperatur_Converter.celsius_to_fahrenheit(celsius)
print(f'Temperature in Fahrenheit: {temp_1}')