def check_validity(num):
    if len(num) > 16:
        print("Too long")
    elif len(num) < 16:
        print("Too short")


def pan(num):
    number = num[6:15]
    return number


def checksum(num):
    number = num[-1]
    return number


def issuer(num):
    dictionary = {
        "34": "American Express",
        "37": "American Express",
        "3": "JCB",
        "4": "Visa",
        "51": "MasterCard",
        "52": "MasterCard",
        "53": "MasterCard",
        "54": "MasterCard",
        "55": "MasterCard",
    }
    if num[0:2] in dictionary:
        return dictionary[num[0:2]]
    elif num[0:1] in dictionary:
        return dictionary[num[0:1]]


while True:
    card_number = int(input("Enter card number: "))
    card_number = str(card_number)
    if check_validity(card_number):
        print(f"Personal Account Number: {pan(card_number)}\nChecksum Digit: {checksum(card_number)}\nIssuer: {issuer(card_number)}")
        break
