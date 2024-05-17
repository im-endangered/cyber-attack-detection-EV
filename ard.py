import requests

# Replace with your ESP32's IP address
ESP32_IP = "192.168.225.203"

def turn_on_relay():
        url = f"http://{ESP32_IP}/?action=turn_on"
        response = requests.get(url)
        if response.status_code == 200:
            print("Relay turned on successfully")
        else:
            print("Failed to turn on relay")

def turn_off_relay():
        
        url = f"http://{ESP32_IP}/?action=turn_off"
        response = requests.get(url)
        if response.status_code == 200:
            print("Relay turned off successfully")
        else:
            print("Failed to turn off relay")


# while True:
#     user_input = input("Attack Detected !!!!!!! Type off to turn off alarm ")
    
#     if user_input == "on":
#         turn_on_relay()
#     elif user_input == "off":
#         turn_off_relay()
#     elif user_input == "quit":
#         print("Exiting the program...")
#         break
#     else:
#         print("Invalid input. Please enter 'on', 'off', or 'quit'.")