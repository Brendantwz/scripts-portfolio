import os
import re
import sys
path = sys.argv[-1]

cafe_info_xml = os.path.join(path, "Collect", "CafeFiles", "cafe_info.xml")

for file in os.listdir(os.path.join(path, "Collect")):
    if file.endswith("_ErrorInfo.log"):
        ErrorInfo_log = os.path.join(path, "Collect", file)
        break

# Reading .rpt from either regen or Regenerate directory
if os.path.exists(os.path.join(path, "regen")):
    for file in os.listdir(os.path.join(path, "regen")):
        if file.endswith(".rpt"):
            report_file = os.path.join(path, "regen", file)
            print("Report Path: regen")

            break
else:
    for file in os.listdir(os.path.join(path, "Regenerate")):
        if file.endswith(".rpt"):
            report_file = os.path.join(path, "Regenerate", file)
            print("Report Path: Regenerate")
            break

# Reading .a_e from either regen or Regenerate directory
if os.path.exists(os.path.join(path, "regen")):
    for file in os.listdir(os.path.join(path, "regen")):
        if file.endswith(".a_e"):
            a_e_file = os.path.join(path, "regen", file)
            print("A_E Path: regen")
            break

else:
    for file in os.listdir(os.path.join(path, "Regenerate")):
        if file.endswith(".a_e"):
            a_e_file = os.path.join(path, "Regenerate", file)
            print("A_E Path: Regenerate")
            break


#command_line = 'C:\Strawberry\perl\bin\perl.exe L:\Cafepub\Cafe_QA\PrintErrorInfoScript\AdjustArchsimEvents.pl' + ' -E' + ' ' + ErrorInfo_log + ' -X' + cafe_info_xml + ' -R' + report_file + ' -A' + a_e_file

command_line = 'L:\Cafepub\Cafe_QA\PrintErrorInfoScript\AdjustArchsimEvents.pl -E {} -X {} -R {} -A {}'.format(ErrorInfo_log, cafe_info_xml, report_file, a_e_file)

#command_line = 'C:\Strawberry\perl\bin\perl.exe L:\Cafepub\Cafe_QA\PrintErrorInfoScript\AdjustArchsimEvents.pl'

print(command_line)

'''
# Define the directories to search for text files
directories = ['/path/to/directory1', '/path/to/directory2', '/path/to/directory3']

# Initialize an empty list to store the file names
file_names = []

# Loop through each directory and extract the names of text files
for directory in directories:
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_names.append(os.path.join(directory, filename))

# Combine the file names into a single command line

command_line = '-R '.join(directory)

# Print the command line to the command prompt
print(command_line)
'''