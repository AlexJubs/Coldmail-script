# Coldmail-script

A python script for sending cold emails to recruiters - automate everything with python :D

This script is configured to send from a gmail account

`recruiter_emails.py` and `parse_mails.py` act as parsing agents to convert data from an excel sheet into a python dict - we loop through every column in the excel sheet and create an element in an array for them.

To use this script:

1. `git pull git@github.com:AlexJubs/Coldmail-script.git`
2. create an excel file, call it `Recruiter-Emails.xlsx`
3. In `Recruiter-Emails.xlsx` fill out each row with the 3 elements: <company_name> | <recruiter_email> | <recruiter_email> - optional
4. set environment variables: 