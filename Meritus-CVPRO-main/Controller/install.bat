@echo off
title Installation of Libraries
set "userProfile=%USERPROFILE%"

:checkInternetConnection
ping 8.8.8.8 -n 1 -w 1000 >nul
if errorlevel 1 (
    echo [31mPlease connect to the internet and try again.[0m
    exit /b
)

:waitForInput
set /p userInput="Do you have a valid Internet Connection? - '[38;5;74my[0m' or '[38;5;74mn[0m': "
if /i "%userInput%"=="y" (
    echo [38;5;74mInstalling dependencies...................[0m

    cd "%userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Controller"

    call %userProfile%\miniconda3\envs\cvpro\python.exe -m pip install --upgrade pip
    REM call conda install cudatoolkit -y
    REM call conda install cudnn -y
    call pip install tensorflow~=2.9.0

    call cd %userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Environment_Setup
    
    call pip install -r requirements.txt


    
    if errorlevel 1 (

        call :echoredError Installation failed!
        echo.
        call :echoblueError Check for the following:
        echo.
        echo 1. Please ensure your Internet Connectivity is Stable.
        echo 2. Please ensure you have activated the 'cvpro' Environment.
        echo 3. Please ensure you have followed the execution steps in the order given.
        echo.
        
    ) else (
    
        echo.
        call :echogreenError Installation is Completed!
        echo.

        call :echoblueError For Data Collection Process:
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
        echo 2. Type ' [38;5;74mtrain_cvpro [0m' to begin the Training Process!
    )
    
) else if /i "%userInput%"=="n" (
    echo [38;5;74mPlease do have a valid Internet Connection for the Installation Process.[0m
) else (
    echo [31mInvalid command. Please enter '[38;5;74my[31m' or '[38;5;74mn[31m'.[0m
    echo.
    goto waitForInput
)


:echoredError
echo [31m%*[0m
exit /b

:echoblueError
echo [38;5;74m%*[0m
exit /b

:echogreenError
echo [92m%*[0m
exit /b

