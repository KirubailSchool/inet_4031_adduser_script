# inet_4031_adduser_script

## Program Description

This program is a Python script that automates the process of creating user accounts and assigning groups on a Linux system. Normally, a system administrator would manually create a user by running commands such as adduser, setting a password with passwd, and then assigning the user to groups.

This script performs those same tasks automatically by reading user information from an input file. Each line in the file contains the required details for a user, and the script processes each line to create the account, set the password, and assign group memberships. This reduces the need to manually enter multiple commands and helps avoid errors when creating many users.

## Program User Operation

This program is run from the command line and uses an input file that contains user information. The script reads each line of the file and processes it to create users and assign them to groups. It can also be run in a dry run mode to check the output without making any changes to the system.

### Input File Format
Each line in the input file represents one user and contains five fields separated by colons. The fields include username, password, last name, first name, and groups.

If a user does not belong to any groups, a dash is used in the groups field. Multiple groups can be listed by separating them with commas.

Lines that begin with a # symbol are treated as comments and are ignored by the script.

### Command Excuction
To run the script, the file may need permission to execute. Once executable, the script is run by passing the input file into it from the command line. The script will then read and process each line of the file.

### "Dry Run"
In dry run mode, the script will not make any actual changes to the system. Instead, it will display the commands that would have been executed. This allows the user to verify that the input file and script are working correctly before making any real changes.  
