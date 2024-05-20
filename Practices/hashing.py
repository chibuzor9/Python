def input_passkey(pass_key):
    hashed_passkey = pass_key.__hash__()
    return hashed_passkey


def main():
    pass_key_ = input("What is your Password: ").lower()

    print("Would you like to see the hashed passkey? : (Y) or (N)")
    response = input().lower()

    if response == "y":
        print(input_passkey(pass_key_))
    else:
        print("Thanks for your time!!")
        exit()


main()
