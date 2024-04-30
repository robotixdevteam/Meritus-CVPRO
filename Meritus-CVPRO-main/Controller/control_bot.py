"""
CVPRO v1.0.0. 
Code Developed by Augustin Rajkumar, Suresh Balaji, E.V.V Thrilok kumar, and Meritus R & D Team -  August 31, 2023.
Copyright © 2023 Meritus R & D Team. All rights reserved.
This program is the intellectual property of Meritus AI, and may not be distributed 
or reproduced without explicit authorization from the copyright holder.
-------------------------------------------------------------------------------------------------------------------
This script helps in Controlling the bot with keyboard keybinding.
Such as:
   w       - forward
   s       - backward
 w + a     - left
 w + d     - right
   b       - bot
   f       - flashlight
   c       - camera swapping
 spacebar  - login on\off
  esc      - quit
"""

# Import Packages
import sys
import socket
import argparse
import pygame
from paho.mqtt import client as mqtt_client
from pygame.locals import (
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_b,
    K_f,
    K_c
)

# screen color
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)
red = (200, 0, 0)

# Mqtt Server connection
BROKER = "192.168.4.2" #"broker.hivemq.com" #"192.168.168.94"  # "broker.emqx.io"
PORT = 1883
TOPIC = "cvpro"
# generate client ID with pub prefix randomly
CLIENT_ID = "python-mqtt"
USERNAME = "cvpro"
PASSWORD = "cvpro"

def speed_input():
    global x
    user_input = input("Enter a valid Speed Limit (170-255):")
    
    if not user_input:
        print("No input provided. Please enter a valid speed limit.")
        speed_input()
        return
    
    x = int(user_input)
 
    if x > 255:
        print("High speed! You should maintain a value under 255! Default is 220.")
        speed_input()
    elif x < 200:
        print("Low speed! You should maintain a value above 200! Default is 220.")
        speed_input()
    else:
        print("Your Speed limit 🏎️ --> ", x)

# Instructions
def caution():
    """
    Display the content in Terminal window 
    """
    name= r"""
                     --- ---- ---- ---- ---- ---- ---- ---- ---- ----
                    | Note:                                          |
                    |     If you want to stop ?                      |
                    |     Click the 'X' on pygame window             |
                    |               or                               |
                    |     Press 'esc' to Quit the pygame window      |
                     --- ---- ---- ---- ---- ---- ---- ---- ---- ----

                   _________   ___            ___   _________      __________         ________
                 /  ________|  \  \          /  /  |   ____  \    |   _____  \      /  ______  \
                /  /            \  \        /  /   |  |    \  \   |  |     \  \    /  /      \  \
                |  |             \  \      /  /    |  |     |  |  |  |_____/  /   |  |        |  |
                |  |              \  \    /  /     |  |____/  /   |  |_______/    |  |        |  |
                |  |               \  \  /  /      |  |______/    |  |   \  \     |  |        |  |
                \  \________        \  \/  /       |  |           |  |    \  \     \  \ _____/  /
                 \ _________|        \____/        |__|           |__|     \__\     \ ________ /

                    """
    print(name)

def usage():
    """
    Display the control keys in Pygame window
    """
    usage_str = """
    Make sure to keep the pygame window in focus!\r

    Use the following keys to drive the robot:\r

    \tw         :   Go forward\r
    \ts         :   Go backward\r
    \tw + a     :   Turn slightly left (while driving)\r
    \tw + d     :   Turn slightly right (while driving)\r
    \tb         :   To Drive turn the bot on/off\r
    \tf         :   Turn on/off Flashlight\r
    \tc         :   Camera Swapping Mode\r
    \tspace-bar :   Data Collection Start/End\r
    \tesc       :   Quit\r
    """
    return usage_str

class Screen:
    """
    Pygame Window Screen 
    """
    screen = None
    font = None
    y_pos = 0
    x_pos = 0

    def setup_screen(self):
        """
        Display the Font-size and resolution for screen
        """
        pygame.display.set_caption("CVPRO Keyboard Controller")
        self.font = pygame.font.Font(None, 26)  # Use system font
        self.screen = pygame.display.set_mode([800, 600], pygame.RESIZABLE)
        self.screen.fill(white)
        text = usage()
        print(text)
        lines = text.strip().split("\r")
        self.x_pos = 50
        self.y_pos = 50
        delimiter = ":"
        for line in lines:
            # create a text suface object
            if delimiter in line:
                space = "         " if "\t" in line else ""
                elements = line.strip().split(delimiter)
                text = self.font.render(
                    space + elements[0].strip() + delimiter, True, blue
                )
                self.screen.blit(text, (self.x_pos, self.y_pos))
                text = self.font.render(elements[1].strip(), True, black)
                self.screen.blit(text, (self.x_pos + 200, self.y_pos))
            else:
                text = self.font.render(line, True, red)
                self.screen.blit(text, (self.x_pos, self.y_pos))
            pygame.display.update()
            self.y_pos += 40

screen = Screen()

def connect_mqtt():
    """
    Connection for MQTT server
    """
    def on_connect(client, userdata, flags, return_code):
        if return_code == 0:
            print("Connected to MQTT Broker 🔗 ")
        else:
            print("Failed to connect, return code %d\n", return_code)
    client = mqtt_client.Client(CLIENT_ID)
    #client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    try:
        client.connect(BROKER, PORT)

    except ConnectionError as connectionerror:
        print(f"Error connecting to MQTT broker: {connectionerror}")
        return None
    except socket.timeout:
        print("Connection Time-out to MQTT broker ⌛️ ")
        return None
    return client

def publish(client):
    """
    To Publish the keys for controlling the bot.
    """
    running = True
    login = False
    bot = False
    camera = False
    flashlight = False
    msg = None
    try:
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN: # control the keys
                    if event.key in (K_UP, K_w): # moving forward
                        msg = f"{x}, {x}"

                    elif event.key in (K_DOWN, K_s): # moving backward
                        msg = f"{-x}, {-x}"

                    elif event.key in (K_LEFT, K_a):  # moving left
                        # Check if the UP key or W key is pressed for diagonal movement
                        if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_w]:
                            msg = f"{-int(x * 0.75)}, {x}"

                    elif event.key in (K_RIGHT, K_d): # moving right
                        # Check if the UP key or W key is pressed for diagonal movement
                        if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_w]:
                            msg = f"{x}, {-int(x * 0.75)}"

                    elif event.key == K_SPACE: # Data collection
                        if not login:
                            msg = "login_on"
                            # print("login start")
                            login = True
                
                        elif login == True:
                            msg = "login_off"
                            # print("login stop")
                            login = False
                            if bot == True: # bot is turn-off when the login is off
                                print("Message Published as bot_off")
                                bot = False
                    
                    elif event.key == K_b: # to turn-on/off the bot
                        if not bot:
                            msg = "bot_on"
                            # print("bot on")
                            bot = True
                        else:
                            msg = "bot_off"
                            # print("bot off")
                            bot = False

                    elif event.key == K_c: # camera swapping
                        if not camera:
                            msg = "front_camera"
                            # print("camera swap into Front-side")
                            camera = True
                        else:
                            msg = "back_camera"
                            # print("camera swap into Back-side")
                            camera = False

                    elif event.key == K_f: # flashlight
                        if not flashlight:
                            msg = "flashlight_on"
                            # print("flashlight on")
                            flashlight = True
                        else:
                            msg = "flashlight_off"
                            # print("flashlight off")
                            flashlight = False

                    elif event.key == K_ESCAPE: # to quit the pygame
                        running = False
                        print("Data Collection - Exit ❌")
                        break
                    if msg is not None:
                        print("Message Published -->",msg)
                        result = client.publish(TOPIC, msg)

                if event.type == KEYUP: # Releasing the Keys
                    # if event.key == K_SPACE or event.key == K_c or event.key == K_f or event.key == K_ESCAPE:
                    if event.key in (K_SPACE, K_c, K_f, K_ESCAPE):
                        if event.key == K_SPACE:
                            msg = None
                        elif event.key == K_c:
                            msg = None
                        elif event.key == K_f:
                            msg = None
                        elif event.key == K_b:
                            msg = None
                        elif event.key == K_ESCAPE:
                            msg = None
                        
                    elif event.key == K_w:
                        msg = f"{0}, {0}"
                    elif event.key in [K_a, K_d]:
                        if pygame.key.get_pressed()[K_w]:
                            msg = f"{x}, {x}"
                        elif pygame.key.get_pressed()[K_s]:
                            msg = f"{-x}, {-x}"
                        else:
                            msg = f"{0}, {0}"
                    elif event.key == K_s:
                        msg = f"{0}, {0}"

                    elif event.key == K_UP:
                        msg = f"{0}, {0}"
                    elif event.key in [K_LEFT, K_RIGHT]:
                        if pygame.key.get_pressed()[K_UP]:
                            msg = f"{x}, {x}"
                        elif pygame.key.get_pressed()[K_DOWN]:
                            msg = f"{-x}, {-x}"
                        else:
                            msg = f"{0}, {0}"
                    elif event.key == K_DOWN:
                        msg = f"{0}, {0}"    
                    # print(msg)
                    if msg is not None:
                        print("Message published in KeyUP ",msg)
                        result = client.publish(TOPIC, msg)

                if event.type == QUIT: # close the pygame window
                    running = False
                    print("Data Collection - Quit 🚪")
                    sys.exit()
                    # result = client.disconnect()

            if not running:
                break  # Break the outer loop
            
    except Exception as exception:
        print(f"Exception in Publish: {exception}")

def run():
    """
    To Run the client, calling the Mqtt Connection
    """
    client = connect_mqtt() # calling the Mqtt Connection

    if client is None: #  the client is not connected
        print("MQTT connection failed. Exiting... 🚪")
        return

    client.loop_start()
    publish(client)

# Main
if __name__ == "__main__":
    speed_input()
    caution()
    pygame.init()
    screen.setup_screen()
    run()