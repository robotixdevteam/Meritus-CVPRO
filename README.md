# Meritus-CVPRO
Process Optimization on Integration of the Kit.


## CV_PRO – STANDARD OPERATING PROCEDURE 

### Agenda: 

- Git-hub Repository. 
- Downloading and Installation of Sources. 
- Extraction to Root Directory. 
- Terminal Execution.

### GitHub Repository: 

- Go to https://github.com/robotixdevteam/Meritus-CVPRO/tree/Windows. 
- Download the ZIP file. 
### Downloading and Installation of Sources: 

- Download and install the Miniconda in the User Profile Path. 
- We recommend to create a conda environment for CVPRO. Instructions on installing conda can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).  
- The easiest way to create a new environment with all dependencies is to use one of the provided environment files.   
 
- Download and Install the Ecllipse-Mosquitto in C:\Program Files. 

### Here, are the step-by-step instructions for downloading mosquitto MQTT Broker: 
- Click [here](https://mosquitto.org/files/binary/win64/mosquitto-2.0.15-install-windows-x64.exe) for Windows 64-bit OS and [here](https://mosquitto.org/files/binary/win32/mosquitto-2.0.15-install-windows-x86.exe) for Windows 32-bit OS. (Note: Download the version that corresponds to your Windows build). 
 

 #### Extraction to Root Directory: 

   - Extract the ZIP to User Profile Path. 
 

### Terminal Execution: 

#### Step 1: Execute ‘cvpro’ 

Windows: 
- Open the Meritus-CVPRO-Windows (Extracted) and open the path in Windows-Command-Prompt, by typing ‘cmd’ in the Address Bar or Breadcrumb Bar. Or, Press ‘Win + R’ which opens the "Run" dialog, then type ‘cmd’ and press ‘Enter’. Now execute the command as follows:
- cd Meritus-CVPRO-Windows
- Execute the command ‘cvpro’. This is your main or Working-Terminal.
- Follow the instructions as per the execution.
- Create and Activate the Environment.
- Installation of Dependencies
- Launch the Server
- ‘Run’ or ‘Train’ the Bot. 
 
#### Step 2: Conda Environment Setup: 

- Type ‘my_conda’, and press ‘Enter’. This will prompt you for further options – ‘build’, ‘activate’ or ‘deactivate’.
- Choose and type the required option as follows:
- Choose and Type ‘build’ and press ‘Enter’. This will create and activate a new conda-environment in the name cvpro. Once after execution, the guide for installation of python libraries will be displayed.
- Choose and Type ‘activate’ and press ‘Enter’ only if you have already built the cvpro environment and installed all the required python libraries in it. That is, the second time when you are integrating or erecting the kit. This will activate the conda environment (cvpro) which is already created and gives the guide for launching the MQTT Server and Data Collection Process/Training Process.
- Choose and Type ‘deactivate’ and press ‘Enter’, only if you have already built the cvpro environment and also when required. This will deactivate the active environment and bring it to (base). 
  

#### Step 3: Installation of Python Libraries: 
- After building the conda environment, the next step is to install the python libraries, by inputting the command, ‘install_cvpro’
- This will prompt you for internet connection check.
- This includes upgradation of pip, tensorflow installation, and required python libraries for data collection and training processes.
- After completing the installation, the guide for data collection process or training process will be displayed. 
 

#### Step 4: MQTT Server: 

- Post installation, read the instructions carefully (displayed in the terminal window) before entering the command ‘launch_server’
- This command will open/launch the MQTT Server in a separate terminal.
- Minimize or keep this terminal aside, as this is not the working / main terminal for data collection or training process.
  
#### Step 5: Data Collection Process: 

- The Data Collection Process should be carried out in Working Terminal, by entering the command ‘run_cvpro’.
- This will take the user into following three prompts one after the other:
- Two further options upon execution of ‘run_cvpro’ – ‘control’ or ‘videostream’.
- Prompt for connecting the bot with the application will be displayed.
- Prompt for speed input for the kit. The user can choose any range between the specified (170-255). The value ‘220’ is more optimal.
- Please make a note that, the terminal clears or refreshes the session, while executing the ‘run_cvpro’.
   
#### Step 6: Training Process: 

- The Training Process should be carried out in Working Terminal, by entering the command ‘train_cvpro’. This will take the user into following five prompts one after the other:
- Prompt for disconnecting the bot from the application as well as system, will be displayed.
- Prompt for Batch Size required for the Training Process. The preset value will be automatically entered if you directly press ‘Enter’ without giving any input value.
- Prompt for Epoch Value required for the Training Process. The preset value will be automatically entered if you directly press ‘Enter’ without giving any input value.
- Prompt for Learning Rate required for the Training Process. The preset value will be automatically entered if you directly press ‘Enter’ without giving any input value.
- Prompt for ‘User Password’ required for the permanently deleting the garbage files, that are not required for the Training Process.
- Please make a note that, the terminal clears or refreshes the session, while executing the ‘train_cvpro’. 
 

## Important Notes : 
- The user who has downloaded the Updated CVPRO ZIP from GitHub, and is following the same, Please Ensure the following before implementing the process: 
- Delete the Meritus-CVPRO-Windows folder (Any Folder with Identical Name) in the User Profile Path, if exists.
- Re-Install the miniconda, (if it already exists and ensure that the entire miniconda3 folder is deleted and newly created in the user profile path while re-installing).
- Begining the process from my_conda -> build, and not my_conda -> activate.  ('my_conda -> activate' should be used only from the second time onwards). 
 
