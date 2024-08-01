@echo off

title Conda Environment - Build and Activate

set "userProfile=%USERPROFILE%"

:checkInternetConnection
ping 8.8.8.8 -n 1 -w 1000 >nul
if errorlevel 1 (
    echo [31mPlease connect to the internet and try again.[0m
    exit /b
)

:waitForInput
echo Hi! Please Ensure Internet Connection! 
set /p userInput="Give me a command - '[38;5;74mbuild[0m' or '[38;5;74mactivate[0m' or '[38;5;74mdeactivate[0m': "
if /i "%userInput%"=="build" (
    echo Creating a Virtual Environment:- cvpro ...
    call  "%userProfile%\miniconda3\Scripts\activate.bat" "%userProfile%\miniconda3"
    call conda create -n cvpro python=3.9 -y
    echo [38;5;74mBuilding the Environment...[0m
    
    if errorlevel 1 (
        echo [31mBuild failed.[0m
    ) else if errorlevel 0 (
        echo [92mBuild is Successful.[0m
        echo.
        echo [38;5;74mActivating the Environment[0m
        call conda activate cvpro
        echo [92mcvpro Environment is Built and Activated...[0m
        echo.
        echo Now you are ready for Installation Process.
        echo.
        echo Type '[38;5;74minstall_cvpro[0m' to Install the Dependencies
        )

) else if /i "%userInput%"=="activate" (
    call "%userProfile%\miniconda3\Scripts\activate.bat" "%userProfile%\miniconda3"
    REM Check if environment exists before activating
    call conda info --envs | findstr /C:"cvpro" > nul
    if errorlevel 1 (
        echo [38;5;74mEnvironment cvpro not found.[0m
        echo [31mActivation failed.[0m
    ) else (
        call conda activate cvpro
        echo [92mcvpro Environment is Activated...[0m
        echo. 
        echo [38;5;74mFor Data Collection Process:[0m
        echo ----------------------------
        echo.
        echo 1. Please Disconnect the Internet, and connect the Bot with the System. Ensure the Connected IPv4 Address is: [38;5;74m192.168.4.2[0m
        echo 2. Type '[38;5;74mlaunch_server[0m' to Launch the MQTT Server to run the Bot!
        echo 3. Type '[38;5;74mrun_cvpro[0m' to begin the Data Collection Process!
        echo.  
        echo [38;5;74mFor Training Process:[0m
        echo ---------------------
        echo.
        echo 1. Ensure your Bot is disconnected from the System as well as the Application.
        echo 2. Type '[38;5;74mtrain_cvpro[0m' to begin the Training Process!
        echo.

    )
) else if /i "%userInput%"=="deactivate" (
    call  "%userProfile%\miniconda3\Scripts\activate.bat" "%userProfile%\miniconda3"
    REM Check if environment exists before activating
    call conda info --envs | findstr /C:"cvpro" > nul
    if errorlevel 1 (
        echo [38;5;74mEnvironment cvpro not found.[0m
        echo [31mDe-Activation failed.[0m
    ) else (
        call conda activate cvpro
        call conda.bat deactivate
        echo.
        echo [92mcvpro Environment is De-Activated[0m
    )
    
) else (
    echo [31mInvalid command. Please enter '[38;5;74mbuild[31m' or '[38;5;74mactivate[31m' or '[38;5;74mdeactivate[31m'.[0m
    echo.
    goto waitForInput
)
