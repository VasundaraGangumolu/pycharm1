import json
import urllib2
weater_api = 'f3c6210c408127ca4890462823157e89'
url = 'http://api.openweathermap.org/data/2.5/weather?zip=534199,in&APPID=f3c6210c408127ca4890462823157e89'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
print data