# Example phone number: 415-930-2045

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(3):    # The first three characters of the string
        if text[i].isdigit():
            continue
        else:
            return False
    if text[3] == '-':    # The fourth character of the string
        pass
    else:
        return False
    for i in range(4,7):  # Characters five through seven (inclusive) of the string
        if text[i].isdigit():
            continue
        else:
            return False
    if text[7] == '-':    # The eigth character of the string
        pass
    else:
        return False
    for i in range(8,12): # Characters nine through twelve (inclusive) of the string
        if text[i].isdigit():
            continue
        else:
            return False
    return True
