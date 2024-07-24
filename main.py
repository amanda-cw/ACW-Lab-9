def encode(password):
    encoded_password = ""

    for i in range(len(password)):
        encoded_password += str((int(password[i]) + 3))


def main():
    encoded_password = ""
    decoded_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = int(input(("Please enter an option: ")))
        if option == 1:
            decoded_password = input("Please enter the password to encode: ")
            encoded_passord = encode(decoded_password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            continue
        elif option == 3:
            quit()
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
