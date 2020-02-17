


def main():

    print ("PYTHON GUESSING GAME.")
    answer = "antelope"
    zero = 0
    while zero==0:
        print("I am thinking of an animal")
        guess = input("Guess what animal I am thinking of")
        if guess == answer:
            zero += 1
        else:
            print("Wrong answer, please guess again")
    print("Correct answer! Great job!")

main ()
