#!/bin/bash

# Start Mosquitto with the specified configuration file

gnome-terminal -- bash -c 'echo -en "\033]0;MQTT Server\007"; mosquitto -v -c $HOME/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Environment_Setup/mqtt_conf.conf; sleep 999999'

