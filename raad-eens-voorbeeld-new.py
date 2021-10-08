import random
number  = random.randrange(1, 50)
guess = int(input("raad een nummer tussen 1 en 50: "))


while guess != number:
    if guess < number:
      print("je moet hoger raden. probeer het opnieuw: ")
      guess = int(input("\nraad een nummer tussen 1 en 50: "))
      guess = input("wil je weer spelen? ")
    else:
        guess = int(input("\nraad een nummer tussen 1 en 50: "))
        print("je moet lager raden. probeer het opnieuw: ")
        guess = int(input("\nraad een nummer tussen 1 en 50: "))
        guess = input("wil je weer spelen? ")
print("je hebt het nummer geraden! ")