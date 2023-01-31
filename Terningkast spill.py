import random
import time
import matplotlib.pyplot as plt

print("testbranch message")
print("Adding some new stuff here")
print("Hello. This is an edit made in branch 1")
print("..and this is an edit made in branch 2")
print("Here's and edit made on branch 3")

# init player score to 0
player1_score = 0
player2_score = 0
player1_sumscore = 0
player2_sumscore = 0
count = 0

print("let's git it")
print("tester mer git")

while True:
    count += 1
    print("RUNDE", count)

    # generate random numbers between 1 and 6 for each player
    player1_input = input("Er du klar for å spille?: (j) (n): ")
    if (player1_input == "j"):
        print("La oss spille...")
        time.sleep(1)
    elif (player1_input == "n"):
        print("Du har avsluttet spillet")
        break
    print("Datamaskin sier: Jeg er klar for å spille.")
    time.sleep(1)

    print("Spillere kaster terningen...\n")
    time.sleep(1)

    player1_value = random.randint(1, 6)
    player2_value = random.randint(1, 6)

    # display the values
    print("Du fikk:", player1_value, "poeng")
    print("Datamaskinen fikk:", player2_value, "poeng\n")

    # display values in pyplot
    x = ['player one', 'player two']
    y = [player1_value, player2_value]
    plt.bar(x, y)
    plt.show()

    # keep score ..
    player1_score = player1_score + player1_value
    player2_score = player2_score + player2_value
    player1_sumscore += player1_score
    player2_sumscore += player2_score

    # hva ble resultatet?
    if player1_value > player2_value:
        print("Du vant denne runden!\n")
    elif player1_value < player2_value:
        print("Datamaskinen vant denne runden.\n")
    else:
        print("Det ble uavgjort.\n")

    if player1_sumscore > player2_sumscore & player1_sumscore >= 50:
        print("Du vant spillet!")
        break
    elif player2_sumscore >= 50:
        print("Datamaskinen vant spillet...")
        break

print("RESULTAT:\nDu fikk:", player1_sumscore,
      "poeng \n" "Datamaskinen fikk:", player2_sumscore, "poeng")

# display final result in pyplot
x = ['player one', 'player two']
y = [player1_sumscore, player2_sumscore]
plt.bar(x, y)
plt.show()
