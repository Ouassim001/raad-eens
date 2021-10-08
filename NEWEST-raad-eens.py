import random
randomding = random.randint(1, 9)
score = 0
for i in range(1, 21):
    x = int(input("voer een nummer in\n"))
    if randomding ==x:
        print("correct")
        vraag3 = input("wil je weer spelen? ")
        score = score + 1
        if vraag3 == "nee":
            break
    if randomding > x:
        print("probeer hoger te raden ")
        vraag1 = input("wil je weer spelen? ")
        if vraag1 == "nee":
            break
    else:
        print("probeer lager te raden")
        vraag2 = input("wil je weer spelen?\n ")
        if vraag2 == "nee":
            break

print("je score is ", score)