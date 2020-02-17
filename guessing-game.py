


def main():

    print ("PYTHON GUESSING GAME.")
    answer = "antelope"
    zero = 0
    while zero==0:
        print("I am thinking of an animal")
        guess = input("Guess what animal I am thinking of")
        if guess.lower() == answer:
            zero += 1
            antelopeScan = 0
            while antelopeScan == 0:
                response = input("Do you like this animal? Y/N: ")
                if response[0].lower() == "y":
                    print("Nice, it's a pretty sweet animal")
                    antelopeScan+=1
                elif response[0].lower() == "n":
                    print("Yeah, they're pretty overrated")
                    antelopeScan += 1
                else:
                    print("PLEASE ANSWER THE QUESTION")
            print("Correct answer! Great job!")
        elif guess[0].lower() == "q":
            zero += 1
        else:
            print("Wrong answer, please guess again")
    print("Done")

main ()
