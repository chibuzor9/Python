import random as rand


def givehall_arg(*tuple_arg):
    if tuple_arg[1]:
        choice = None

        if tuple_arg[0] == "male":
            print("Select your Hall\n")

            for hall in tuple_arg[3]:
                print(f'-{hall}', end="\n")

            choice = int(input(f"Pick with number (for e.g {tuple_arg[3][0]}, Enter 1) "))

            if choice is None:
                print("\nWelcome to " + rand.choice(tuple_arg[3]))
            else:
                print("\nWelcome to " + tuple_arg[3][choice - 1])
        elif tuple_arg[0] == "female":
            print("Select your Hall\n")

            for hall in tuple_arg[2]:
                print(f'-{hall}', end="\n")

            choice = int(input(f"Pick with number (for e.g {tuple_arg[3][0]}, Enter 1) "))

            if tuple_arg[4] is None:
                print("\nWelcome to " + rand.choice(tuple_arg[2]))
            else:
                print("\nWelcome to " + tuple_arg[2][choice - 1])
        else:
            print("Gender Unrecognized!!!")
    else:
        print("Go and Register!")


def givehall_keyword(**dict_kwarg):
    # for key,value in dict.items():
    #    print(f"Key: {key}, Value: {value}")

    if dict_kwarg['isRegistered']:
        choice = None

        if dict_kwarg['student'] == "male":
            print("Select your Hall\n")

            for hall in dict_kwarg['maleHalls']:
                print(f'-{hall}', end="\n")

            choice = int(input(f"Pick with number (for e.g {dict_kwarg['maleHalls'][0]}, Enter 1) "))

            if choice is None:
                print("\nWelcome to " + rand.choice(dict_kwarg['maleHalls']))
            else:
                print("\nWelcome to " + dict_kwarg['maleHalls'][choice - 1])
        elif dict_kwarg['student'] == "female":
            print("Select your Hall\n")

            for hall in dict_kwarg['femaleHalls']:
                print(f'-{hall}', end="\n")

            choice = int(input(f"Pick with number (for e.g {dict_kwarg['femaleHalls'][0]}, Enter 1) "))

            if choice is None:
                print("\nWelcome to " + rand.choice(dict_kwarg['femaleHalls']))
            else:
                print("\nWelcome to " + dict_kwarg['femaleHalls'][choice - 1])
        else:
            print("Gender Unrecognized!!!")
    else:
        print("Go and Register!")


givehall_arg("male",
             True,
             ["Ameyo", "Queen Esther", "FAD", "Diamond", "Havilah", "Platinum"],
             ["Samuel Akande", "Winslow", "TOPAZ", "Neil Wilson", "Nelson Mandela"])

givehall_keyword(student="male",
                 isRegistered=True,
                 femaleHalls=["Ameyo", "Queen Esther", "FAD", "Diamond", "Havilah", "Platinum"],
                 maleHalls=["Samuel Akande", "Winslow", "TOPAZ", "Neil Wilson", "Nelson Mandela"])
