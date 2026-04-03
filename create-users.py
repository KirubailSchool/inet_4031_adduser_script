#!/usr/bin/python3

# INET4031
# Kirubail
# 03-26-2026
# 03-02-2026

# Import os is for system level commands from within python
# Import re is used for regular expression matching 
# sys is used for acces to stdin that is used below which means standard input which is used for reading input 

import os
import re
import sys


def main():
    for line in sys.stdin:

        #This expression matching is checking if the line starts with a "#".
        #The purpose is to skip the lines that are commented out meaning the do not want that user to be processed or changed at the moment. 

        match = re.match("^#",line)

        #This is to split up the line based of where the colon is which is what splits up the password from group..ect
        fields = line.strip().split(':')

        #The if Contion checks if the line is a comment which starts with # or does nto contain exactly 5 fields
        # If either condition is true then the line will be skipped 
        # This will help prevent errors that are from incorrect inputs 
        # This code requires all 5 inputs to create and add the user so if one is missing it would cause a issue
        
        if match or len(fields) != 5:
            continue

	# These three lines store the username password and user information for identity. It is takign them from the parsed lines.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This split is done incase the user is meant to be added to mutiple groups since they are seperated by commas.
        groups = fields[4].split(',')

        # This simply shows the user the account is being created for the specific user 
        print("==> Creating account for %s..." % (username))
        # This is creating the linux command to create a new user account, the disabled password stops password login at first and gecos adds teh user identity information like full name..
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

	# These lines were commented out for dry run mode ensuring that when the code was ran at first we were able to just print the code outputs but not run then to make the users incase the code was incorrect.
        print(cmd)
        os.system(cmd)

	# This prints a message to the user showing them the password is being set.
        print("==> Setting the password for %s..." % (username))
	# This builds a command that echoes the password twice for confirmation 
	# It then pipes it into the password command to set the users password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

	# This would execute the password setting command if it was it was left uncommented 
        print(cmd)
        os.system(cmd)

        for group in groups:
            # It looks for the "-" sign as a  way to indicate that the person should not be added to any groups therefore if it is not there then to continue 
	    # to add the person to the listed groups.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
