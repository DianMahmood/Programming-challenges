def richter_converter_joules(richter):
    energy = 10**((1.5*richter)+4.8)
    return energy


def richter_converter_tnt(richter):
    energy = 10**((1.5*richter)+4.8)
    tnt = energy / (4.184*10**9)
    return tnt


richter_values = [1.0, 5.0, 9.1, 9.2, 9.5]
for item in richter_values:
    joules = richter_converter_joules(item)
    tnt = richter_converter_tnt(item)
    print(f"""Richter:
{item}
Joules:
{joules}
TNT:
{tnt}
--------------------------""")






richter = float(input("Please enter a Richter scale value: "))
print(f"Richter value {richter}")
print(f"Equivalence in joules: {richter_converter_joules(richter)}")
print(f"Equivalence in tons of TNT: {richter_converter_tnt(richter)}")