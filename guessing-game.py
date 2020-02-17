


def main():

    print ("PYTHON GUESSING GAME.")
    answer = "antelope"
    zero = 0
    while zero==0:
        print("I am thinking of an animal")
        guess = input("Guess what animal I am thinking of")
        if guess.lower() == answer:
            zero += 1
            print("Correct answer! Great job!")
        elif guess.lower() == "quit":
            zero += 1
        else:
            print("Wrong answer, please guess again")
    print("Done")

main ()
