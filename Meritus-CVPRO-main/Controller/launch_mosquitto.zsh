#!/bin/zsh

# Start Mosquitto with the specified configuration file

osascript -e 'tell application "Terminal" to do script "printf \"\\e]1;MQTT Server\\a\"; mosquitto -v -c $HOME/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Environment_Setup/mqtt_conf.conf"'
