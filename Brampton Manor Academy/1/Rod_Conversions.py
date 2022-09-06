def conversion_meters(rods):
    meters = rods * 5.0292
    return meters


def conversion_feet(rods):
    meters = rods * 5.0292
    feet = meters/0.3048


def conversion_miles(rods):
    meters = rods * 5.0292
    miles = meters/1609.34


def conversion_furlongs(rods):
    furlongs = rods/40


def conversion_minutes(rods):
    pass





rods = float(int(input("Input rods: ")))
print(f"You input {rods} rods")

