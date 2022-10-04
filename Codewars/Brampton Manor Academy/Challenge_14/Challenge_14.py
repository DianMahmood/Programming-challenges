cond = True
while cond:
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
            print(int(answer))
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
        elif op1 == "q" or op2 == "q" or calc == "q":
            cond = False
    except ValueError:
        print("Expected three input values")
