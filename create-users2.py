#!/usr/bin/python3




# These imports provide access to system commands, regular expressions, and command-line input.

#INET 4031
#Kirubail Yenew
# 03-28-26
# 04-02-26

import os
import re
import sys

def main():

    # Prompt the user to choose dry-run mode
    response = input("Run in Dry Run mode? (Y/N): ")

    # Set a boolean flag based on user input
    if response == "Y":
        dry_run = True
    else:
        dry_run = False

    for line in sys.stdin:

        # Check if the line starts with '#' to identify commented/disabled lines
        match = re.match("^#", line)

        # Split the line into fields using ':' as the delimiter
        fields = line.strip().split(':')

        # Skip lines that are commented out or do not have exactly 5 fields
        # This ensures only properly formatted and active lines are processed
        if match or len(fields) != 5:
            if dry_run:
                print("Skipping invalid line:", line.strip())
            continue

        # Assign each field to a variable for easier use
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the groups field into a list of individual groups
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % (username))

        # Command to create a new user account with no password and user info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Execute or print the command depending on dry-run mode
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        print("==> Setting the password for %s..." % (username))

        # Command to set the user's password using echo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        for group in groups:

            # Only process valid groups (ignore '-' meaning no group)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))

                # Command to add the user to a group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)


if __name__ == "__main__":
    main()
