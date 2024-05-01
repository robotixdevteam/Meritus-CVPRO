@echo off
title Data Collection Process
set "userProfile=%USERPROFILE%"
cd "%userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Controller"

call cls

:waitForChoice
set /p userInput="Enter your choice - '[38;5;74mcontrol[0m' or '[38;5;74mvideostream[0m': "

if /i "%userInput%"=="control" (
    call :run_bot control_bot.py
) else if /i "%userInput%"=="videostream" (
    call :run_bot videostream_control_bot.py
) else (
    echo [31mInvalid choice. Please enter '[38;5;74mcontrol[31m' or '[38;5;74mvideostream[31m'.[0m
    echo.
    goto waitForChoice
)

goto :eof

:run_bot
:waitForInput
set /p userInput="Is your Bot connected with the Application? - '[38;5;74my[0m' or '[38;5;74mn[0m': "
if /i "%userInput%"=="y" (
    echo [92mRunning the Bot.......[0m
) else if /i "%userInput%"=="n" (
    echo [38;5;74mPlease connect the bot with your Application![0m
    exit /b
) else (
    echo [31mInvalid command. Please enter '[38;5;74my[31m' or '[38;5;74mn[31m'.[0m
    echo.
    goto waitForInput
)
call python %1
echo.
echo Type '[38;5;74mrun_cvpro[0m' or '[38;5;74mtrain_cvpro[0m' according to your requirement!
goto :eof
