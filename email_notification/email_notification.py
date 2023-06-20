 
	
	
	def send_html_email(self, message, image_list, attachment=None):
        strFrom = "noreply@<domain>.com"
        strTo = ", ".join(self.recipient)

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart("related")
        msgRoot["Subject"] = self.email_subject
        msgRoot["From"] = strFrom
        msgRoot["To"] = strTo
        msgRoot.preamble = "Nothing in plain view. Please switch to HTML view."
		
       # Send the email
        import smtplib

        smtp = smtplib.SMTP("smtp.<domain>.com")
        smtp.sendmail(strFrom, self.recipient, msgRoot.as_string())
        smtp.quit()
        return True