"""
CVPRO v1.0.0. 
Code Developed by Augustin Rajkumar, Suresh Balaji, E.V.V Thrilok kumar, and Meritus R & D Team -  August 31, 2023.
Copyright © 2023 Meritus R & D Team. All rights reserved.
This program is the intellectual property of Meritus AI, and may not be distributed 
or reproduced without explicit authorization from the copyright holder.
-------------------------------------------------------------------------------------------------------------------
This script helps in Controlling the bot with keyboard keybinding.
Such as:
 w  - forward
 s  - backward
 a  - Move sideways left
 d  - Move sideways right
 z  - Move diagonal left\r
 x  - Move diagonal right\r
 c  - Move around a blend left\r
 v  - Move around a blend right\r
 e  - Rotation left\r
 r  - Rotation right\r
 f  - Rotation around the central point of one axle in left\r
 g  - Rotation around the central point of one axle in right\r
esc - quit
"""

# Import Packages
import sys
import socket
import argparse
import pygame
from paho.mqtt import client as mqtt_client
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    K_w, K_a, K_s, K_d,
    K_z, K_x, K_c, K_v,
    K_e, K_r, K_f, K_g,
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

parser = argparse.ArgumentParser(description="Control the Bot.")
parser.add_argument(
    "-c", type=int, default=255, help="integer values to send to bot"
)

args = parser.parse_args()
x = args.c

if x > 255:
    print("High speed! You should maintain a value under 255.")
    # pygame.quit()
    sys.exit()
elif x < 200:
    print("Low speed! You should maintain a value above 200.")
    # pygame.quit()
    sys.exit()
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


 ____      ____    ____________      __________          ____         _____      __    __         __    ____      ____ 
|    \    /    |  |   _________|    /  ________|        /    \       |     \    |  |  |  |       |  |  |    \    /    |
|     \  /     |  |  |             /  /                /  /\  \      |  |\  \   |  |  |  |       |  |  |     \  /     |
|  |\  \/  /|  |  |  |_________   |  |                /  /  \  \     |  | \  \  |  |  |  |       |  |  |  |\  \/  /|  |
|  | \____/ |  |  |   _________|  |  |               /  /____\  \    |  |  \  \ |  |  |  |       |  |  |  | \____/ |  |
|  |        |  |  |  |            |  |              /  _______   \   |  |   \  \|  |  \  \       /  /  |  |        |  | 
|  |        |  |  |  |_________    \  \_________   /  /        \  \  |  |    \  |  |   \  \_____/  /   |  |        |  |
|__|        |__|  |____________|    \ __________| /__/          \__\ |__|     \ ___|    \_________/    |__|        |__|        


                    """
    print(name)

def usage():
    """
    Display the control keys in Pygame window
    """
    usage_str = """
    Make sure to keep the pygame window in focus!\r

    Use the following keys to drive the robot:\r

    \tw    :   Go forward\r
    \ts    :   Go backward\r
    \ta    :   Move sideways left\r
    \td    :   Move sideways right\r
    \tz    :   Move diagonal left\r
    \tx    :   Move diagonal right\r
    \tc    :   Move around a blend left\r
    \tv    :   Move around a blend right\r
    \te    :   Rotation left\r
    \tr    :   Rotation right\r
    \tf    :   Rotation around the central point of one axle in left\r
    \tg    :   Rotation around the central point of one axle in right\r
    \tesc  :   Quit \r
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
        pygame.display.set_caption("CVPRO Mecanum Keyboard Controller")
        self.font = pygame.font.Font(None, 22)  # Use system font
        self.screen = pygame.display.set_mode([900, 650], pygame.RESIZABLE)
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
                    if event.key == K_w: # moving forward
                        msg = f"{x}, {x}"
                    
                    elif event.key == K_s: # moving backward
                        msg = f"{-x}, {-x}"
                    
                    elif event.key == K_a: # moving sideways left
                        msg = f"{-30}, {30}"

                    elif event.key == K_d: # moving sideways right
                        msg = f"{30}, {-30}"
                    
                    elif event.key == K_z: # moving diagonal left
                        msg = f"{-15}, {15}"

                    elif event.key == K_x: # moving diagonal right
                        msg = f"{15}, {-15}"
                    
                    elif event.key == K_c: # moving around blend left
                        msg = f"{-60}, {60}"
                    
                    elif event.key == K_v: # moving around blend right
                        msg = f"{60}, {-60}"
                    
                    elif event.key == K_e: # Rotation left
                        msg = f"{-360}, {360}"

                    elif event.key == K_r: # Rotation right
                        msg = f"{360}, {-360}"
                    
                    elif event.key == K_f: # Rotation around the central point of one axle in left
                        msg = f"{-120}, {120}"
                    
                    elif event.key == K_g: # Rotation around the central point of one axle in right
                        msg = f"{120}, {-120}"

                    elif event.key == K_ESCAPE: # to quit the pygame
                        running = False
                        print("Control Screen - Quit🚪")
                        break
                    if msg is not None:
                        print("Message Published -->",msg)
                        result = client.publish(TOPIC, msg)

                if event.type == KEYUP: # Releasing the Keys
                    if event.key == K_ESCAPE:
                        msg = None
                    elif event.key == K_w:
                        msg = f"{0}, {0}"
                    elif event.key == K_s:
                        msg = f"{0}, {0}"
                    elif event.key == K_a:
                        msg = f"{0}, {0}"
                    elif event.key == K_d:
                        msg = f"{0}, {0}"
                    elif event.key == K_e:
                        msg = f"{0}, {0}"
                    elif event.key == K_r:
                        msg = f"{0}, {0}"
                    elif event.key == K_f:
                        msg = f"{0}, {0}"
                    elif event.key == K_g:
                        msg = f"{0}, {0}"
                    elif event.key == K_z:
                        msg = f"{0}, {0}"
                    elif event.key == K_x:
                        msg = f"{0}, {0}"
                    elif event.key == K_c:
                        msg = f"{0}, {0}"
                    elif event.key == K_v:
                        msg = f"{0}, {0}"                   
                    # print(msg)
                    if msg is not None:
                        print("Message published in KeyUP ",msg)
                        result = client.publish(TOPIC, msg)

                if event.type == QUIT: # close the pygame window
                    running = False
                    print("Control Screen - Exit ❌")
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
    caution()
    pygame.init()
    screen.setup_screen()
    run()
