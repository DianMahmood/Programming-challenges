def check_validity(num):
    if len(num) > 16:
        return "Too long"
    elif len(num) < 16:
        return "Too short"
    else:
        return num.isnumeric()


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
    check = num[0:2], num[0:1]
    if check in dictionary:
        return f"Issuer is {dictionary[check]}"




card_number = input("Enter 16-digit card number: ")
#print(check_validity(card_number))
#print(pan(card_number))
#print(checksum(card_number))
print(issuer(card_number))