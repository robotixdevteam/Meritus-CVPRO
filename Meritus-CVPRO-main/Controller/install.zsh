#!/bin/zsh

# Define ANSI color escape codes
RED='\033[0;31m' # Red color
GREEN='\033[0;92m' # Green color
BLUE='\033[38;5;74m' # Light blue color
NC='\033[0m'     # No color (reset)

echo -ne "\033]0;Installation of Libraries\007"

userProfile="$HOME"

checkInternetConnection() {
    ping -c 1 8.8.8.8 >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "${RED}Please connect to the internet and try again.${NC}"
        return 1
    fi
}

main() {
    checkInternetConnection

    echo "Do you have a valid Internet Connection? - '${BLUE}y${NC}' or '${BLUE}n${NC}': "
    read userInput
    if [[ "$userInput" == "y" ]]; then
        echo "${BLUE}Installing dependencies...................${NC}"

        cd "$userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Controller"

        "$userProfile/miniconda3/envs/cvpro/bin/python" -m pip install --upgrade pip

        # Uncomment the following lines if needed
        # conda install cudatoolkit -y
        # conda install cudnn -y
        conda install -c apple tensorflow-deps -y
        pip install tensorflow-macos~=2.9.0

        cd "$userProfile/Meritus-CVPRO-Mac/Meritus-CVPRO-main/Environment_Setup"
        
        pip install -r requirements.txt

        if [ $? -ne 0 ]; then
            echo ""
            echo "${RED}Installation failed!${NC}"
            echo ""
            echo "${BLUE}Check for the following:${NC}"
            echo ""
            echo "1. Please ensure your Internet Connectivity is Stable."
            echo "2. Please ensure you have activated the 'cvpro' Environment."
            echo "3. Please ensure you have followed the execution steps in the order given."
            echo ""
            
        else
            echo ""
            echo "${GREEN}Installation is Completed!${NC}"
            echo ""
            echo "${BLUE}For Data Collection Process:${NC}"
            echo "----------------------------"
            echo ""
            echo "1. Please Disconnect the Internet, and connect the Bot with the System. Ensure the Connected IPv4 Address is: ${BLUE}192.168.4.2${NC}"
            echo "2. Type '${BLUE}launch_server${NC}' to Launch the MQTT Server to run the Bot!"
            echo "3. Type '${BLUE}run_cvpro${NC}' to begin the Data Collection Process!"
            echo ""
            echo "${BLUE}For Training Process:${NC}"
            echo "---------------------"
            echo ""
            echo "1. Ensure your Bot is disconnected from the System as well as the Application."
            echo "2. Type '${BLUE}train_cvpro${NC}' to begin the Training Process!"
            echo ""
        fi
    elif [[ "$userInput" == "n" ]]; then
        echo "${BLUE}Please do have a valid Internet Connection for the Installation Process.${NC}"
    else
        echo "${RED}Invalid command. Please enter '${BLUE}y${RED}' or '${BLUE}n${RED}'.${NC}"
        echo ""
        main
    fi
}

main


    
