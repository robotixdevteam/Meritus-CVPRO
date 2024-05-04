# Meritus-CVPRO
Process Optimization on Integration of the Kit.


# CV_PRO – STANDARD OPERATING PROCEDURE
 
## Agenda:

- GitHub Repository

- Downloading and Installation of Sources

- Extraction to Root Directory

- Terminal Execution
 
## GitHub Repository:

- Go to [CVPRO GitHub Repository](https://github.com/robotixdevteam/Meritus-CVPRO/tree/Mac).

- Download the ZIP file.
 
## Downloading and Installation of Sources:

- Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) in the User Profile Path.

  - We recommend creating a conda environment for CVPRO. Instructions on installing conda can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Download and Install [Eclipse-Mosquitto](https://mosquitto.org/download/) in the User Profile Path.

  - Install MQTT on your local system. For macOS, use the following command to install Mosquitto using Homebrew:

    ```

    brew install mosquitto

    ```
 
## Extraction to Root Directory:

- Extract the ZIP to the User Profile Path.
 
## Terminal Execution:

### Step 1: Execute 'cvpro'

- **macOS:**

  - Right-click the extracted Folder and select 'New Terminal at Folder'. Or,

  - Open a Terminal App and type:

    ```

    cd Meritus-CVPRO-Mac

    ```

  - Execute the command `source cvpro.zsh`. This is your main or Working-Terminal.

  - Follow the instructions as per the execution.

    - Create and Activate the Environment.

    - Installation of Dependencies.

    - Launch the Server.

    - 'Run' or 'Train' the Bot.
 
### Step 2: Conda Environment Setup:

- Type `my_conda` and press `Enter`. This will prompt you for further options – 'build', 'activate', or 'deactivate'.

- Choose and type the required option:

   - Choose and Type 'build' to create and activate a new conda-environment named cvpro. Once after execution, the guide for installation of python libraries will be displayed.

   - Choose and Type 'activate' only if you have already built the cvpro environment and installed all the required python libraries in it. That is, the second time when you are integrating or erecting the kit.
  This will activate the conda environment (cvpro) and gives the guide for launching the MQTT Server and Data Collection Process/Training Process.

   - Choose and Type 'deactivate' only if you have already built the cvpro environment and also when required. This will deactivate the active environment and bring it to (base).
 
### Step 3: Installation of Python Libraries:

- After building the conda environment, install the python libraries by inputting the command `install_cvpro`.

- This will prompt you for an internet connection check.

- This includes upgrading pip, tensorflow installation, and required python libraries for data collection and training processes.

- After completing the installation, the guide for data collection process or training process will be displayed.
 
### Step 4: MQTT Server:

- Post installation, read the instructions carefully (displayed in the terminal window) before entering the command `launch_server`.

- This command will open/launch the MQTT Server in a separate terminal.

- Minimize or keep this terminal aside, as this is not the working/main terminal for data collection or training process.
 
### Step 5: Data Collection Process:

- The Data Collection Process should be carried out in the Working Terminal, by entering the command `run_cvpro`. This will take the user into the following three prompts:

  - Two further options upon execution of `run_cvpro` – 'control' or 'videostream'.

  - Prompt for connecting the bot with the application.

  - Prompt for speed input for the kit. The user can choose any range between the specified (170-255). The value '220' is more optimal.

- Please note that the terminal clears or refreshes the session while executing `run_cvpro`.
 
### Step 6: Training Process:

- The Training Process should be carried out in the Working Terminal, by entering the command `train_cvpro`. This will take the user into the following five prompts:

  - Prompt for disconnecting the bot from the application as well as the system.

  - Prompt for Batch Size required for the Training Process.

  - Prompt for Epoch Value required for the Training Process.

  - Prompt for Learning Rate required for the Training Process.

  - Prompt for 'User Password' required for permanently deleting the garbage files that are not required for the Training Process.

- Please note that the terminal clears or refreshes the session while executing `train_cvpro`.
