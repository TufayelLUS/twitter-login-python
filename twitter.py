import requests
import re

username = ""
password = ""

s = requests.Session()
headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
s_code = s.post('https://mobile.twitter.com/i/nojs_router?path=%2Flogin', data={}, headers=headers,allow_redirects=False).status_code
print(s_code)
resp = s.get('https://mobile.twitter.com/login',headers=headers).text
token = re.findall(r'authenticity_token" type="hidden" value="(.*?)"', resp)[0]
data = {
    'authenticity_token': token,
    'session[username_or_email]': username,
    'session[password]': password,
    'remember_me': '1',
    'wfa': '1',
    'commit': ' Log in ',
    'ui_metrics': ''
}
s_code = s.post('https://mobile.twitter.com/sessions',headers=headers,data=data,allow_redirects=False).status_code
print(s_code)
'''cookies = s.cookies.get_dict()
cookie_as_text = ""
for key, value in cookies.items():
    cookie_as_text += "{}={};".format(key,value)
'''
# you can now use s variable session to do anything as a logged in user.
