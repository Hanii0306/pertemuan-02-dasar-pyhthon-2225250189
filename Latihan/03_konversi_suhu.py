KELVIN_OFFSET = 273.15

print("KONVERSI SUHU")

celsius = float(input("Suhu Celsius: "))

fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print()
print(f"Celsius    = {celsius:.2f} °C")
print(f"Fahrenheit = {fahrenheit:.2f} °F")
print(f"Kelvin     = {kelvin:.2f} K")