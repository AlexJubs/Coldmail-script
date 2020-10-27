# Coldmail-script

A python script for sending cold emails to recruiters - automate everything with python 🧠

This script is configured to send from a gmail account 📨

`recruiter_emails.py` and `parse_mails.py` act as parsing agents to convert data from an excel sheet into a python dict - we loop through every column in the excel sheet and create an element in an array for them. 📖

To use this script:

1. `git pull git@github.com:AlexJubs/Coldmail-script.git`
2. Create an excel file, call it `Recruiter-Emails.xlsx`
3. In `Recruiter-Emails.xlsx` fill out each row with the 3 elements: <company_name> | <recruiter_email> | <recruiter_name> - optional
4. Set environment variables by executing into your shell: `export gmail_email=<your gmail email>` and `export gmail_password=<your gmail password>` (unset these as SOON as you're done with this script)
5. Go to your gmail account settings, click "Manage Google Account", then go to "Security" and turn on "Less secure app access" (and turn this off as SOON as you're done with this script)
6. Make sure you have python3 installed and type `python3 coldmail.py` and watch your gmail "sent" page for the emails you just sent

PS: Unless you're me from summer 2020, please change the email message text 😉

Enjoy! please reach out to me if you have any suggestions at www.linkedin.com/in/alexjabbour
