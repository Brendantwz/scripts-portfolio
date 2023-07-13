==========================================
Script Creator: Teo, Brendan Wei Zhi
Documentation Writer: brendan.codes
Script developed date: 14th May 2022
===========================================

The script is currently under development with the purpose of how to sort out key signature words from files from folder with tremendous files that has different extension and namings (consisting the key words) to a desired file for revision.

This script is created by ChatGPT based on this prompt (small adjustment made manually with assistance of ChatGPT):
Can you write me a batch script that is able to sort out all types of file in the directory from looking at the key words or signature and move those file with the signature into a designated folder. That designated folder will be created upon the execution of script. That script will have to show what file has been moved and number of files moved.
	
Last updated:
13th July 2023:
+Improved version of file_sort version 2 is tested in Testing Environment file that are able to check into subdirectory
+Script able to create a destination directory after reviewing the signature/keywords from the different file type

=================
== How to Deploy ===
=================
[1] Make sure your these 3 are set to your desired path and keywords

set "source_directory=C:\*\scripts-portfolio\File sorter\Testing Env"
set "destination_directory=C:\*\scripts-portfolio\File sorter\Testing Env\Signature-sorted"
set "keywords=bc804605 r0"

Modify source_directory to the path of the directory where you want to search for files.
Modify destination_directory to the path of the directory where you want to move the matching files. Note that if the directory doesn't exist, the script will create it.
Modify keywords to include the specific keywords or signatures you want to match. Separate multiple keywords with spaces.