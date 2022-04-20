def print_hello_world():
    
    while True:
        print("Hello world")
        get_input = True

        while get_input == True:

            repeat = input("Should I keep printing Hello World? (y/n): ")

            if repeat.lower() == "n":
                return

            if repeat.lower() == "y":
                get_input = False
                pass

            else:
                print("This is not a valid answer.\n")

print_hello_world()