def get_emails():
	emails = {}
	try:
		email_file = open("email.txt", 'r')
		for line in email_file:
			(email, name) = line.split(',')
			emails[email] = name.strip()

	except FileNotFoundError as err:
		print(err)

	return emails