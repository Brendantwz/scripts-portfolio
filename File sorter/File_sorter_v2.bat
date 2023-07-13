@echo off
setlocal enabledelayedexpansion

rem Set the directory path and keywords/signatures
set "source_directory=C:\Users\brend\OneDrive\Documents\GitHub\scripts-portfolio\File sorter\Testing Env"
set "destination_directory=C:\Users\brend\OneDrive\Documents\GitHub\scripts-portfolio\File sorter\Testing Env\Signature-sorted"
set "keywords=bc804605 r0"

rem Create the destination directory if it doesn't exist
if not exist "%destination_directory%" (
    mkdir "%destination_directory%"
)

rem Initialize the counter for moved files
set /a "count=0"

rem Loop through the files in the source directory and its subdirectories
for /r "%source_directory%" %%F in (*) do (
    set "filename=%%~nxF"

    rem Check if the filename contains any of the keywords
    for %%K in (%keywords%) do (
        echo "!filename!" | findstr /i "%%K" >nul
        if not errorlevel 1 (
	rem Check if the file exists in the source directory
            	if exist "%%F" (
            		rem Move the file to the destination directory
            		move "%%F" "%destination_directory%\!filename!"
            		set /a "count+=1"
            		echo Moved: !filename!
	)
        )
    )
)

rem Display the files in the destination directory
echo Files in destination directory:
dir /b "%destination_directory%"

rem Display the number of files in the destination directory
rem echo Number of files in destination directory: %file_count%

pause
endlocal
