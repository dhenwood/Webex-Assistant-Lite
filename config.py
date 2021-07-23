privateKeyLocation = "id_rsa"


def logic(textQuery) -> str:
    textResponse = ""
    if "Mars" in textQuery:
        textResponse = "Mars is 379 million kilometers away"
    elif "Jupiter" in textQuery:
        textResponse = "Jupiter is 617 million kilometers away"
    else:
        textResponse = "Sorry, I can only help with distances to Mars and Jupiter"

    return textResponse
