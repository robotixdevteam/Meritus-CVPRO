#!/bin/bash

# Define ANSI color escape codes
RED='\033[0;31m' # Red color
GREEN='\033[0;92m' # Green color
BLUE='\033[38;5;74m' # Light blue color
NC='\033[0m'     # No color (reset)

echo -ne "\033]0;Data Collection Process\007"

userProfile="$HOME/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Controller"
cd "$userProfile"

clear

main(){


echo -e "Enter your choice - '${BLUE}control${NC}' or '${BLUE}videostream${NC}': "
read userInput

run_bot() {
    local script="$1"
    while true; do
        echo -e "Is your Bot connected with the Application? - '${BLUE}y${NC}' or '${BLUE}n${NC}': " 
        read userInput
        if [[ "$userInput" == "y" ]]; then
            echo -e "${GREEN}Running the Bot.......${NC}"
            break
        elif [[ "$userInput" == "n" ]]; then
            echo -e "${BLUE}Please connect the bot with your Application!${NC}"
            return 1
        else
            echo -e "${BLUE}Invalid command. Please enter 'y' or 'n'.${NC}"
            echo ""
        fi
    done
    python "$script"
    echo
    echo -e "Type '${BLUE}run_cvpro${NC}' or '${BLUE}train_cvpro${NC}' according to your requirement!"
}

if [[ "$userInput" == "control" ]]; then
    run_bot "control_bot.py"
elif [[ "$userInput" == "videostream" ]]; then
    run_bot "videostream_control_bot.py"
else
    echo -e "${RED}Invalid choice. Please enter '${BLUE}control${RED}' or '${BLUE}videostream${RED}'.${NC}"
    echo ""
    main
fi
}
main
