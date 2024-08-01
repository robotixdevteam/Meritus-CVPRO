@echo off
title Training Process
set "userProfile=%USERPROFILE%"
cd "%userProfile%\Meritus-CVPRO-Windows\Meritus-CVPRO-main\Training_Process"

call cls

:waitForInput
set /p userInput="Is your Bot Disconnected from the Application and System? - '[38;5;74my[0m' or '[38;5;74mn[0m': "
if /i "%userInput%"=="y" (
    echo [92mInitializing the Training Process![0m
) else if /i "%userInput%"=="n" (
    echo [38;5;74mPlease disconnect the Bot from your Application and the System![0m
    exit /b
) else (
    echo [31mInvalid command. Please enter '[38;5;74my[31m' or '[38;5;74mn[31m'.[0m
    echo.
    goto :waitForInput
)

set /p batchSize="Give me a valid Batch Size [16, 32, 64, 128]: "
if "%batchSize%"=="" set "batchSize=32"
echo [38;5;74mMy Batch Size:[0m %batchSize%
echo.


set /p epochValue="Give me a valid Epoch Value [5, 10, 20, 25, 50, 100]: "
if "%epochValue%"=="" set "epochValue=5"
echo [38;5;74mMy Epoch Value:[0m %epochValue%
echo.


set /p learningRate="Give me a valid Learning Rate [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]: "
if "%learningRate%"=="" set "learningRate=0.0001"
echo [38;5;74mMy Learning Rate:[0m %learningRate%
echo.

echo Deleting the Garbage Files, that are not required for Training Process..........  

call :delFiles
timeout /t 2 >nul

echo Garbage Files are Deleted

call python main.py -b %batchSize% -e %epochValue% -lr %learningRate%

:delFiles
for /r %%i in (gitkeep) do (
    if exist "%%i" (
        del "%%i" /q /f
    )
)