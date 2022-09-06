def conversion_meters(rods):
    meters = rods * 5.0292
    return meters


def conversion_feet(rods):
    meters = rods * 5.0292
    feet = meters/0.3048
    return feet


def conversion_miles(rods):
    meters = rods * 5.0292
    miles = meters/1609.34
    return miles


def conversion_furlongs(rods):
    furlongs = rods/40
    return furlongs


def conversion_minutes(rods):
    meters = rods * 5.0292
    miles = meters/1609.34
    minutes = (miles/3.1) * 60
    return minutes





rods = float(int(input("Input rods: ")))
print(f"You input {rods} rods")
print(f"Conversions:\nMeters: {conversion_meters(rods)}\nFeet: {conversion_feet(rods)}\nMiles: {conversion_miles(rods)}\nFurlongs: {conversion_furlongs(rods)}")
print(f"Minutes to walk {rods} rods: {conversion_minutes(rods)}")











             






