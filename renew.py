import requests

username = ""
password = ""

def authenticate():
	"""autorenew
	"""
	endpoint = "https://hetrixtools.com/"
	payload = {"username": username, "password": password, "remember": "0", "m": "1"}
	payload_2 = {"X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15", "Referer": "https://hetrixtools.com/login/"}
	sess = requests.Session()
	req_1 = sess.post(endpoint + "auth.php", data = payload, headers = payload_2)
	if "Welcome" in req_1.text:
		print("[STATUS] Authenticated, renewing account...")
		req_2 = sess.get(endpoint + "dashboard/", headers = payload_2)
		if "Last Activity" in req_2.text:
			print("[STATUS] Account renewed")
		else:
			print("[STATUS] Failed to renew account")
	else:
		print("[STATUS] Authentication failed")

authenticate()
