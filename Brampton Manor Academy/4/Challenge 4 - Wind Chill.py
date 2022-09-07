def wind_chill_temp_index(air_temp, air_speed):
    calculation = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return calculation


print(f"Temperature of 10 and speed of 15 gives windchill of: {wind_chill_temp_index(10, 15)}")
print(f"Temperature of 0 and speed of 25 gives windchill of: {wind_chill_temp_index(0, 25)}")
print(f"Temperature of -10 and speed of 35 gives windchill of: {wind_chill_temp_index(-10, 35)}")

temp = float(input("Temperature: "))
speed = float(input("Speed: "))
print(f"Windchill: {wind_chill_temp_index(temp, speed)}")
