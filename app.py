import weather
import send_email
import get_schedule
import email_list

def main():
	emails = get_emails()
	# print(emails)
	schedule = get_schedule()
	# print(schedule)
	forecast = weather.get_weather()
	# print(forecast)
	send_email.send_emails(emails, schedule, forecast)

main()