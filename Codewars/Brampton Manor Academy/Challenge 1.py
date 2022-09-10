def conversion_meters(rods):
    return rods * 5.0292


def conversion_feet(rods):
    return conversion_meters(rods) / 0.3048


def conversion_miles(rods):
    return conversion_meters(rods) / 1609.34


def conversion_furlongs(rods):
    return rods/40


def conversion_minutes(rods):
    return (conversion_miles(rods) / 3.1) * 60


def getinput():
    rods = float(input("Input rods: "))
    print(f"You input {rods} rods")
    return rods


def giveoutput():
    print(f"\nConversions:\nMeters: {conversion_meters(rods)}\nFeet: {conversion_feet(rods)}\nMiles: {conversion_miles(rods)}\nFurlongs: {conversion_furlongs(rods)}")
    print(f"Minutes to walk {rods} rods: {conversion_minutes(rods)}")


rods = getinput()
giveoutput()
