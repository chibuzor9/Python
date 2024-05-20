weight = input("Weight: ")

option = input ("(K)g or (L)bs: ")

kg = float(weight) * 0.45
lb = float(weight) / 0.45

if option == 'K' or option == 'k':  #if unit.upper() == "K":
    print("Weight in Kg: " + str(kg))
else:
    print("Weight in Lb: " + str(lb))