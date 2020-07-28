# this script was created by Alex Jabbour on Nov 15, 2019
import smtplib
import os
from recruiter_emails import recruiter_emails

# recruiter_emails is a list of objects with structure {"name":<recruiter_name>, "email":<recruiter_email>, "company":<company_name>}

class coldmail:
    def __init__(self, recruiter_name, company_name, email_address):

        if (recruiter_name == None): recruiter_name = company_name + " hiring manager(s)"
        # compose email string
        message = """
Greetings {}, my name is Alex Jabbour.

I understand your time is valuable, I only have 3 things to say:

I've been developing object-oriented code and writing systematic python scripts since I was 13. I read a lot and not afraid to learn new technologies.

I have 1 year of experience working as a software engineer, managing cloud infrastructure, and developing microservices - 8 months of which in Silicon Valley.

I want to intern for {}. Can I forward my resume?

Warm regards,
Alex
        """.format(recruiter_name, company_name)

        subject = "My interest in a SWE internship at {}".format(company_name)

        # establish connection to outlook email
        self.FROM = os.environ["gmail_email"]
        self.TO = [email_address]

        # Prepare message wrapper
        self.full_mail = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

        %s
        """ % (self.FROM, ", ".join(self.TO), subject, message)

        self.send_mail()

    def send_mail(self):
        # Send the mail
        server.sendmail(self.FROM, self.TO, self.full_mail)

if __name__ == "__main__":
    # run the script
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(os.environ["gmail_email"], os.environ["gmail_password"])

    # go thru each recruiter, taking the name, company and email
    for recruiter in recruiter_emails:
        coldmail(recruiter["name"], recruiter["company"], recruiter["email"])

    server.quit()


