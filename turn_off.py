import ard

while True:
    user_input = input("Attack Detected !!!!!!! Type off to turn off alarm ")
    
    if user_input == "on":
        ard.turn_on_relay()
    elif user_input == "off":
        ard.turn_off_relay()
    elif user_input == "quit":
        print("Exiting the program...")
        break
    else:
        print("Invalid input. Please enter 'on', 'off', or 'quit'.")