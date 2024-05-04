#!/bin/bash

# Define ANSI color escape codes
RED='\033[0;31m' # Red color
GREEN='\033[0;92m' # Green color
BLUE='\033[38;5;74m' # Light blue color
NC='\033[0m'     # No color (reset)

userProfile=$HOME

chmod +x "$userProfile/Meritus-CVPRO-Linux/cvpro.sh" 
chmod +x "$userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/activate_cvpro.sh" 
chmod +x "$userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/install.sh"
chmod +x "$userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/test_run.sh" 
chmod +x "$userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/train.sh"
chmod +x "$userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/launch_mosquitto.sh"


echo ""
echo -e "${GREEN}Pre-Requisites:${NC}"
echo "---------------"
echo -e "1. Download the Meritus-CVPRO from ${BLUE}https://github.com/robotixdevteam/Meritus-CVPRO/tree/Linux${NC} and extract the same to the ${BLUE}User-Profile Path${NC}"
echo ""
echo -e "2. ${BLUE}Miniconda${NC} should be installed in the ${BLUE}User-Profile Path${NC}"
echo ""
echo -e "3. ${BLUE}Mosquitto${NC} should be installed in ${BLUE}User-Profile Path${NC}"
echo ""

echo -e "${GREEN}Hierarchy of Execution:${NC}"
echo "-----------------------"
echo -e "Type '${BLUE}my_conda${NC}' - Create or Activate the Conda Environment"
echo ""
echo -e "Type '${BLUE}install_cvpro${NC}' - Installation of required libraries"
echo ""
echo --------------------------------------------------------------------
echo -e "Please ensure to connect the Bot with the System"
echo -e "Type '${BLUE}launch_server${NC}' - Launch the MQTT Server"
echo --------------------------------------------------------------------
echo ""
echo -e "Type '${BLUE}run_cvpro${NC}' to move the Bot around for Data-Collection Process."
echo ""
echo -e "Type '${BLUE}train_cvpro${NC}' to train the Bot for Autonomous Process."
echo ""



alias my_conda=". $userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/activate_cvpro.sh"
alias install_cvpro=". $userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/install.sh"
alias launch_server=". $userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/launch_mosquitto.sh"
alias run_cvpro=". $userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/test_run.sh"
alias train_cvpro=". $userProfile/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller/train.sh"
