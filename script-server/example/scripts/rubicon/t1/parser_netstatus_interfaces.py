from bs4 import BeautifulSoup
import re

def test():
	return ('test')

def parsing (data_):
	result_ = []
	tmp_ = []
	soup_ = BeautifulSoup(data_, "html.parser")
	soup_ = soup_.pre.get_text()
	tmp_ = re.split(r'\n\n', soup_)
	
	for i_ in tmp_:
		# Парсинг элементов
		#print (i_)
		try:
			name_ = re.findall('^\s?([^:]+).*?<([^>]+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			name_ = 'NONE'
		#print (name_)
		try:
			address_ = re.findall('inet (\S+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			address_ = 'NONE'
		#print (address_)
		try:
			netmask_ = re.findall('netmask (\S+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			netmask_ = 'NONE'
		#print (netmask_)
		try:
			mac_ = re.findall('ether (\S+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			mac_ = 'NONE'
		#print (mac_)
		try:
			mtu_ = re.findall('mtu (\S+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			mtu_ = 'NONE'
		#print (mtu_)
		result_.append({"name":name_[0], "status":name_[1], "address":address_, "netmask":netmask_, "mac":mac_, "mtu":mtu_})

	return result_
