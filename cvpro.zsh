#!/bin/zsh

# Define ANSI color escape codes
RED='\033[0;31m' # Red color
GREEN='\033[0;92m' # Green color
BLUE='\033[38;5;74m' # Light blue color
NC='\033[0m'     # No color (reset)

userProfile=$HOME

chmod +x "$userProfile/Meritus-CVPRO-Mac/cvpro.zsh"
chmod +x "$userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/activate_cvpro.zsh"
chmod +x "$userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/install.zsh"
chmod +x "$userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/test_run.zsh"
chmod +x "$userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/train.zsh"
chmod +x "$userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/launch_mosquitto.zsh"

echo ""
echo "${GREEN}Pre-Requisites:${NC}"
echo "---------------"
echo "1. Download the Meritus-CVPRO from ${BLUE}https://github.com/robotixdevteam/Meritus-CVPRO/tree/Mac${NC} and extract the same to the ${BLUE}User-Profile Path${NC}"
echo ""
echo "2. ${BLUE}Miniconda${NC} should be installed in the ${BLUE}User-Profile Path${NC}"
echo ""
echo "3. ${BLUE}Mosquitto${NC} should be installed in ${BLUE}User-Profile Path${NC}"
echo ""

echo "${GREEN}Hierarchy of Execution:${NC}"
echo "-----------------------"
echo "Type '${BLUE}my_conda${NC}' - Create or Activate the Conda Environment"
echo ""
echo "Type '${BLUE}install_cvpro${NC}' - Installation of required libraries"
echo ""
echo --------------------------------------------------------------------
echo "Please ensure to connect the Bot with the System"
echo "Type '${BLUE}launch_server${NC}' - Launch the MQTT Server"
echo --------------------------------------------------------------------
echo ""
echo "Type '${BLUE}run_cvpro${NC}' to move the Bot around for Data-Collection Process."
echo ""
echo "Type '${BLUE}train_cvpro${NC}' to train the Bot for Autonomous Process."
echo ""

alias my_conda=". $userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/activate_cvpro.zsh"
alias install_cvpro=". $userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/install.zsh"
#alias launch_server="gnome-terminal --working-directory=$HOME/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Environment_Setup -- bash -c 'mosquitto -v -c mqtt_conf.conf; exec bash'"
alias launch_server=". $userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/launch_mosquitto.zsh"
alias run_cvpro=". $userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/test_run.zsh"
alias train_cvpro=". $userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller/train.zsh"
