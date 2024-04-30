"""
CVPRO v1.0.0. 
Code Developed by Augustin Rajkumar, Suresh Balaji, E.V.V Thrilok kumar, and Meritus R & D Team - August 31, 2023.
Copyright © 2023 Meritus R & D Team. All rights reserved.
This program is the intellectual property of Meritus AI, and may not be distributed 
or reproduced without explicit authorization from the copyright holder.
---------------------------------------------------------------------------------------
This script helps in Video-Streaming and Controlling the bot with keyboard keybinding.
Such as:
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
import cv2
import uuid
import base64
import pygame
import socket
import argparse
import numpy as np
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

# MQTT broker and TOPIC
BROKER = "192.168.4.2" #"broker.hivemq.com"
PORT = 1883
TOPIC = "cvpro"
TOPIC2 = "video"

# generate client ID with pub prefix randomly
# CLIENT_ID = "python-mqtt"
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

def main():
        
    # Instructions
    def caution():
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

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker 🔗 ")
        else:
            print("Failed to connect, return code %d\n", rc)

    # Callback function for MQTT message
    def on_message(client, userdata, msg):
        print("Message was received")
        if msg.payload is None:
            print("Received an empty message payload.")
        frame_data = base64.b64decode(msg.payload)
        
        if len(frame_data) == 0:
            print("Received empty frame data.")

        frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
        
        if frame is None:
            print("Failed to decode frame.")
        # Flip the frame horizontally
        # frame = cv2.flip(frame, 1)
        # Convert the OpenCV frame to a Pygame surface
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame, k=2)  # Rotate 180 degrees counter-clockwise
        frame = np.fliplr(frame)  # Flip the frame horizontally
        frame = pygame.surfarray.make_surface(frame)
        # Update the video frame
        video_frame.blit(frame, (0, 0))

    # Set up the display
    screen_width = 930
    screen_height = 600
    control_width = screen_width // 2
    video_width = screen_width - control_width
    #screen-size
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("CVPRO Keyboard Controller")

    # Define the left and right display surfaces
    control_display = pygame.Surface((control_width, screen_height))
    video_display = pygame.Surface((video_width, screen_height))
    # print("video_width: ", video_width)
    # print("screen_height: ", screen_height)

    def display_text():
        # Render and blit the usage text on the control display
        usage_text = """
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
        lines = usage_text.strip().split("\r")
        line_height = 30
        # Render and blit the usage text on the control display
        x_pos = 50
        y_pos = 50
        delimiter = ":"
        for line in lines:
            if delimiter in line:
                space = "         " if "\t" in line else ""
                elements = line.strip().split(delimiter)
                text = font.render(space + elements[0].strip() + delimiter, True, blue)
                control_display.blit(text, (x_pos, y_pos))
                text = font.render(elements[1].strip(), True, black)
                control_display.blit(text, (x_pos + 200, y_pos))
            else:
                text = font.render(line, True, red)
                control_display.blit(text, (x_pos, y_pos))
            y_pos += line_height
        

    # Initalize the pygame screen
    pygame.init()
    caution()
    # Font for usage information
    font = pygame.font.Font(None, 20)

    # Initialize video frame
    video_frame = pygame.Surface((465, 600))

    # Generate a UUID version 4
    uuid_obj = uuid.uuid4()

    # Convert the UUID to a string
    uuid_string = str(uuid_obj)

    # MQTT client setup
    client = mqtt_client.Client(f"VideoReceiver-{uuid_string}")
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect(BROKER, PORT)
    except ConnectionError as connectionerror:
        print(f"Error connecting to MQTT broker: {connectionerror}")
    except socket.timeout:
        print("Connection Time-out to MQTT broker ⌛️ ")
    # subscribe 
    client.subscribe(TOPIC2, qos=2)
    client.loop_start()

    # Declare
    running = True
    login = False
    bot = False
    camera = False
    flashlight = False
    msg = None
    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:  # control the keys
                if event.key in (K_w,K_UP):  # moving forward
                    msg = f"{x}, {x}"

                elif event.key in (K_s,K_DOWN):  # moving backward
                    msg = f"{-x}, {-x}"

                elif event.key in (K_a,K_LEFT):  # moving left
                    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] :
                        msg = f"{-int(x * 0.75)}, {x}"

                elif event.key in (K_d,K_RIGHT):  # moving right
                    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
                        msg = f"{x}, {-int(x * 0.75)}"

                elif event.key == K_SPACE:  # Data collection
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
                        
                elif event.key == K_b:  # to turn-on/off the bot
                    if not bot:
                        msg = "bot_on"
                        # print("bot on")
                        bot = True
                    else:
                        msg = "bot_off"
                        # print("bot off")
                        bot = False

                elif event.key == K_c:  # camera swapping
                    if not camera:
                        msg = "front_camera"
                        # print("camera swap into Front-side")
                        camera = True
                    else:
                        msg = "back_camera"
                        # print("camera swap into Back-side")
                        camera = False

                elif event.key == K_f:  # flashlight
                    if not flashlight:
                        msg = "flashlight_on"
                        # print("flashlight on")
                        flashlight = True
                    else:
                        msg = "flashlight_off"
                        # print("flashlight off")
                        flashlight = False

                elif event.key == K_ESCAPE:  # to quit the pygame
                    running = False
                    print("Data Collection - Exit ❌")
                    break
                if msg is not None:
                    print("Message Published -->", msg)
                    result = client.publish(TOPIC, msg)

            if event.type == KEYUP:  # Releasing the Keys
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
                # print(msg)
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
                if msg is not None:
                    print("Message published in KeyUP ", msg)
                    result = client.publish(TOPIC, msg)

            if event.type == QUIT:  # close the pygame window
                running = False
                print("Data Collection - Quit 🚪")
                sys.exit()

        # Clear the screens
        control_display.fill(white)
        video_display.fill(white)
        display_text()
        # Blit the video frame on the video display
        video_display.blit(video_frame, (0, 0))

        # Blit the control and video displays onto the main screen
        screen.blit(control_display, (0, 0))
        screen.blit(video_display, (control_width, 0))

        pygame.display.update()

    # Clean up resources
    cv2.destroyAllWindows()
    client.disconnect()
    #pygame.quit()
    sys.exit()

if __name__ == '__main__':
    speed_input()
    main()