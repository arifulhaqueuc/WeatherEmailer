import smtplib

def send_emails(emails, schedule, forecast):
	server = smtplib.SMTP('smtp.gmail.com', '587')

	server.starttls()
	password = input("What's your password: ")
	from_email = "naharhossain2010@gmail.com"
	server.login(from_email, password)
	# to_email = "arifulhaque2010@live.com"

	for to_email, name in emails.items():
		message = 'Subject: Welcome to the circus'
		message += 'Hi' + name + 'welcome to the show'
		message += forecast
		message += schedule
		server.sendmail(from_email, to_email, message)


	server.quit()
