@echo off

set "list=file_sorter_list.txt"
set "src=L:\usr3\brendanw\Script"
set "dst=L:\usr3\brendanw\Script\bc804605_r0_sorted"

rem Check if the list file exists
if not exist %list% (
  echo List file %list% not found.
  exit /b 1
)

rem Check if the source folder exists
if not exist %src% (
  echo Source folder %src% not found.
  exit /b 1
)

rem Create the destination folder if it doesn't exist
if not exist %dst% (
  mkdir %dst%
)

rem Read the list file and sort the files (to include sort for folder remove /a-d)
for /f "delims=" %%a in (%list%) do (
  for /f "delims=" %%b in ('dir /b %src%^|find /i "%%a"') do (
    move "%src%\%%b" "%dst%\%%b"
  )
)

echo Sorting complete.
