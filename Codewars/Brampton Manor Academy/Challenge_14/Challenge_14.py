cond = True

while cond == True:
    try:
        op1, op2, calc = input("Enter your calculation: ").split()
        if calc == "+":
            answer = float(op1) + float(op2)
            print(int(answer))
        elif calc == "-":
            answer = float(op1) - float(op2)
            print(int(answer))
        elif calc == "*":
            answer = float(op1) * float(op2)
            prin(int(answer))
        elif calc == "/":
            answer = float(op1) / float(op2)
            print(answer)
        elif calc == "//":
            answer = float(op1) // float(op2)
            print(int(answer))
        elif calc == "%":
            answer = float(op1) % float(op2)
            print(int(answer))
        elif calc == "**":
            answer = float(op1) ** float(op2)
            print(int(answer))
        #elif op1.lower() == "q":
    except ValueError(op1):
        if op1.lower() == "q":
            cond = False




