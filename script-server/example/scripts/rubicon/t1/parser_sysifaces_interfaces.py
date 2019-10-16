from bs4 import BeautifulSoup
import re

def test():
	return ('test')

def parsing (data_):
	result_ = []
	tmp_ = []
	soup_ = BeautifulSoup(data_, "html.parser")
	ma_ = re.compile("<interface>.*?</interface>", re.MULTILINE|re.DOTALL)
	tmp_ = ma_.findall(str(soup_.find_all('interface')))
	
	for i_ in tmp_:
		# Заменяем значения в html для более простого парсинга страниц
		i_ = i_.replace('name="COLOR" type="hidden" value="', 'COLOR=')
		i_ = i_.replace('name="NUMBER" type="hidden" value="', 'NUMBER=')
		i_ = i_.replace('name="ADDRESS" title="XXX.XXX.XXX.XXX" type="text" value="', 'ADDRESS=')
		i_ = i_.replace('name="NETMASK" title="YYY.YYY.YYY.YYY" type="text" value="', 'NETMASK=')
		i_ = i_.replace('name="MAC" title="ZZ:ZZ:ZZ:ZZ:ZZ:ZZ" type="text" value="', 'MAC=')
		i_ = i_.replace('name="MTU" title="1500" type="text" value="', 'MTU=')
		# Парсинг элементов
		try:
			name_ = re.findall('color:*\w[A-Z]+;">((\w+\W+\w+)|(\W+\w+)|(\w+\W)|(\w+))<', i_, re.MULTILINE|re.DOTALL)[1][0]
		except:
			name_ = 'NONE'
		#print (name_)
		try:
			color_ = re.findall('COLOR=(\w[A-Z]+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			color_ = 'NONE'
		#print (color_)
		try:
			number_ = re.findall('NUMBER=(\w+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			number_ = 'NONE'
		#print (number_)
		try:
			address_ = re.findall('ADDRESS=(\w+.\w+.\w+.\w+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			address_ = 'NONE'
		#print (address_)
		try:
			netmask_ = re.findall('NETMASK=(\w+.\w+.\w+.\w+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			netmask_ = 'NONE'
		#print (netmask_)
		try:
			mac_ = re.findall('MAC=(\w+:\w+:\w+:\w+:\w+:\w+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			mac_ = 'NONE'
		#print (mac_)
		try:
			mtu_ = re.findall('MTU=(\w+)', i_, re.MULTILINE|re.DOTALL)[0]
		except:
			mtu_ = 'NONE'
		#print (mtu_)
		result_.append({"name":name_, "color":color_, "number":number_, "address":address_, "netmask":netmask_, "mac":mac_, "mtu":mtu_})

	return result_
