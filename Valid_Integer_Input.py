while True:
    try:
        number = int(input("Enter an integer: "))
        print("Valid integer:", number)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
