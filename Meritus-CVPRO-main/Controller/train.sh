#!/bin/bash

# Define ANSI color escape codes
RED='\033[0;31m' # Red color
GREEN='\033[0;92m' # Green color
BLUE='\033[38;5;74m' # Light blue color
NC='\033[0m'     # No color (reset)

echo -ne "\033]0;Training Process\007"

userProfile="$HOME/Meritus-CVPRO-Linux/Meritus-CVPRO-main/Training_Process"
cd "$userProfile"

clear

while true; do
    echo -e "Is your Bot Disconnected from the Application and System? - '${BLUE}y${NC}' or '${BLUE}n${NC}': "
    read userInput
    if [[ "$userInput" == "y" ]]; then
        echo -e "${GREEN}Initializing the Training Process!${NC}"
        break
    elif [[ "$userInput" == "n" ]]; then
        echo -e "${BLUE}Please disconnect the Bot from your Application and the System!${NC}"
        return 1
    else
        echo -e "${RED}Invalid command. Please enter '${BLUE}y${RED}' or '${BLUE}n${RED}'.${NC}"
        echo ""
    fi
done

echo "Give me a valid Batch Size [16, 32, 64, 128]: "
read batchSize
batchSize="${batchSize:-32}"
echo -e "${BLUE}My Batch Size:${NC} $batchSize"
echo ""

echo "Give me a valid Epoch Value [5, 10, 20, 25, 50, 100]: "
read epochValue
epochValue="${epochValue:-5}"
echo -e "${BLUE}My Epoch Value:${NC} $epochValue"
echo ""

echo "Give me a valid Learning Rate [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]: "
read learningRate
learningRate="${learningRate:-0.0001}"
echo -e "${BLUE}My Learning Rate:${NC} $learningRate"
echo ""

echo "Please enter your Password for deleting the Garbage Files, that are not required for Training Process."
sudo find . -name 'gitkeep' -type f -delete

echo""
echo "Garbage Files are Deleted"
echo""

python main.py -b "$batchSize" -e "$epochValue" -lr "$learningRate"

