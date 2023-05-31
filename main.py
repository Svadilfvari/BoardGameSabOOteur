import SabOOteurInterf
import SabOOteurText

def main():
    print("\nVersion 1 -> text-only version")
    print("Version 2 -> graphic version\n")

    choice = "  "

    while len(choice) != 1 and ord(choice[0]) != 49 and ord(choice[0]) != 50:
        print("? Which version do you want to play with ?")
        choice = input("Version : ")

        if len(choice) == 1:
            if ord(choice) == 49 :
                SabOOteurText.welcome()
            elif ord(choice) == 50:
                SabOOteurInterf.welcome()
            else :
                print("\nLooking for bugs ?\n")
                choice = "  "
        else:
            print("\nLooking for bugs ?\n")
            choice = "  "

main()