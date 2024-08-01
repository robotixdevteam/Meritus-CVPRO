@echo off
set "userProfile=%USERPROFILE%"
set mosquittoProfile= C:\Program Files

echo.
echo [92mPre-Requisites:[0m
echo ---------------
echo 1. Download the Meritus-CVPRO from [38;5;74mhttps://github.com/robotixdevteam/Meritus-CVPRO/tree/Windows[0m and extract the same to the [38;5;74mUser-Profile Path[0m
echo.
echo 2. [38;5;74mMiniconda[0m should be installed in the [38;5;74mUser-Profile Path[0m
echo.
echo 3. [38;5;74mMosquitto[0m should be installed in [38;5;74m%mosquittoProfile%[0m
echo. 

echo [92mHierarchy of Execution:[0m
echo -----------------------
echo Type '[38;5;74mmy_conda[0m' - Create or Activate the Conda Environment
echo.
echo Type '[38;5;74minstall_cvpro[0m' - Installation of required libraries
echo.
echo --------------------------------------------------------------------
echo Please ensure to connect the Bot with the System
echo Type '[38;5;74mlaunch_server[0m' - Launch the MQTT Server
echo --------------------------------------------------------------------
echo.
echo Type '[38;5;74mrun_cvpro[0m' to move the Bot around for Data-Collection Process.
echo.
echo Type '[38;5;74mtrain_cvpro[0m' to train the Bot for Autonomous Process.

doskey my_conda="%userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Controller\activate_cvpro.bat"
doskey install_cvpro="%userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Controller\install.bat"
doskey launch_server=start cmd /K "%userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Controller\launch_mosquitto.bat"
doskey run_cvpro="%userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Controller\test_run.bat"
doskey train_cvpro="%userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Controller\train.bat"  