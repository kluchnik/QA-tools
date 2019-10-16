import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test ():
	return ('ok')

def get (protocol_, host_, port_, urn_, login_, password_, timeout_):
	try:
		r_ = requests.get(protocol_ + '://' + host_ + ':' + port_ + urn_, \
		verify=False, auth=(login_, password_), timeout=int(timeout_))
		return (r_)
	except:
		return ('error')

def post (protocol_, host_, port_, urn_, login_, password_, timeout_, data_):
	try:
		r_ = requests.post(protocol_ + '://' + host_ + ':' + port_ + urn_, \
		verify=False, auth=(login_, password_), timeout=int(timeout_), \
		headers={'referer':protocol_ + '://' + host_ + ':' + port_ + urn_}, \
		data=data_)
		return (str(r_.status_code))
	except:
		return ('error')
