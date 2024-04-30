#!/bin/zsh

# Define ANSI color escape codes
RED='\033[0;31m' # Red color
GREEN='\033[0;92m' # Green color
BLUE='\033[38;5;74m' # Light blue color
NC='\033[0m'     # No color (reset)

echo -ne "\033]0;Conda Environment - Build and Activate\007"

userProfile="$HOME"

# Main function
main() {
    echo -e "${BLUE}Checking internet connection...${NC}"
    retries=3
    while [ $retries -gt 0 ]; do
        # Ping Google's DNS server (8.8.8.8) with one packet and wait for a response.
        # Redirect output to /dev/null to suppress any output.
        ping -c 1 8.8.8.8 >/dev/null 2>&1

        # Check the exit status of the ping command.
        if [ $? -eq 0 ]; then
            echo "${GREEN}Internet connection is available.${NC}"

            echo "Hi! Please Ensure Internet Connection!"
            echo "Give me a command - '${BLUE}build${NC}' or '${BLUE}activate${NC}' or '${BLUE}deactivate${NC}': "
            read userInput
            
            if [[ "$userInput" == "build" ]]; then
                echo "Creating a Virtual Environment:- cvpro ..."
                source "$userProfile/miniconda3/bin/activate" "$userProfile/miniconda3"
                
                conda create -n cvpro python=3.9 -y
                echo "${BLUE}Building the Environment...${NC}"
                
                if [ $? -ne 0 ]; then
                    echo "${RED}Build failed.${NC}"
                
                elif ! conda info --envs | grep -q "cvpro"; then
                        echo "${BLUE}Build failed.${NC}"
                
                else
                    echo "${GREEN}Build is Successful.${NC}"
                    echo ""
                    echo "${BLUE}Activating the Environment${NC}"
                    conda activate cvpro
                    echo "${GREEN}cvpro Environment is Built and Activated...${NC}"
                    echo
                    echo "Now you are ready for Installation Process."
                    echo
                    echo "Type '${BLUE}install_cvpro${NC}' to Install the Dependencies"
                    return 1
                fi
            elif [[ "$userInput" == "activate" ]]; then
                source "$userProfile/miniconda3/bin/activate" "$userProfile/miniconda3"
                if conda info --envs | grep -q "cvpro"; then
                
                    conda activate cvpro
                    echo "${GREEN}cvpro Environment is Activated...${NC}"
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
                    
                    return 1
                else
                    echo "${BLUE}Environment cvpro not found.${NC}"
                    echo "${RED}Activation failed.${NC}"
                    return 1
                fi
            elif [[ "$userInput" == "deactivate" ]]; then
                source "$userProfile/miniconda3/bin/activate" "$userProfile/miniconda3"
                if conda info --envs | grep -q "cvpro"; then
                    conda activate cvpro
                    conda deactivate
                    echo "${GREEN}cvpro Environment is De-Activated${NC}"
                    return 1
                else
                    echo "${BLUE}Environment cvpro not found.${NC}"
                    echo "${RED}De-Activation failed.${NC}"
                    return 1
                fi
            else
                echo "${RED}Invalid command. Please enter '${BLUE}build${RED}' or '${BLUE}activate${RED}' or '${BLUE}deactivate${RED}'.${NC}"
                echo ""
            fi
        else
            echo "${RED}Attempt failed. Retrying...${NC}"
            ((retries--))
        fi
    done
    echo "${BLUE}Failed to establish internet connection after multiple attempts.${NC}"
    return 1  # Failure
}

# Call main function
main
