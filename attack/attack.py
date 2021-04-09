import requests


def request_pin(phone_number):
	response = requests.post(
		"https://quiet-spire-87888.herokuapp.com",
		data={
			"phone_number": phone_number
		}
	)
	if response.status_code == 200:
		print("Requested a PIN for {}".format(phone_number))
		return True
	else:
		print("Failed to request PIN for {} ({})".format(
			phone_number,
			response.status_code,
		))
		return False

def main():
	request_pin("123456789")

if __name__ == '__main__':
	main()
