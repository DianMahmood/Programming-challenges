def wind_chill_temp_index(air_temp, air_speed):
    return 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16


temps = [10, 0, -10]
speeds = [15, 25, 35]
for x in range(1, 4):
    print(f"Temperature of {temps[x-1]} and speed of {speeds[x-1]} gives windchill of: {wind_chill_temp_index(temps[x-1], speeds[x-1])}")
temp = float(input("Temperature: "))
speed = float(input("Speed: "))
print(f"Windchill: {wind_chill_temp_index(temp, speed)}")