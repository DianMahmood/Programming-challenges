def richter_converter_joules(richter):
    return 10**((1.5*richter)+4.8)


def richter_converter_tnt(richter):
    return richter_converter_joules(richter) / (4.184*10**9)


def getinput():
    richter = float(input("Please enter a Richter scale value: "))
    print(f"Richter value {richter}")
    return richter


def giveoutput():
    print(f"Equivalence in joules: {richter_converter_joules(richter)}")
    print(f"Equivalence in tons of TNT: {richter_converter_tnt(richter)}")


print(f"""
Richter          Joules                              TNT
1                {richter_converter_joules(1)}       {richter_converter_tnt(1)}
5                {richter_converter_joules(5)}       {richter_converter_tnt(5)}
9.1              {richter_converter_joules(9.1)}     {richter_converter_tnt(9.1)}
9.2              {richter_converter_joules(9.2)}     {richter_converter_tnt(9.2)}
9.5              {richter_converter_joules(9.5)}     {richter_converter_tnt(9.5)}""")

richter = getinput()
giveoutput()
