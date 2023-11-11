x = input("where's input house? ")

match x:
    case "harry" | "hermoine":
        print("norwood")
    case _:
        print("who?")