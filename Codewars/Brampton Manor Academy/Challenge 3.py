try:
    print(f"We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!")
    answer = int(input("*You* This will be the answer. Select a number between 10-49: "))
    factor = 99 - answer
    friend_number = int(input("*Player* Pick any number 50-99: "))
    total = friend_number + factor
    change_digits = (total//100) + (total - 100)
    result = friend_number - change_digits
    print(f"I said the answer was {result} and the calculation result is {result}")
except ValueError:
    print("The input includes non-numerical values.")