import requests
import json
from lxml import html

s = requests.session()

username = raw_input("Username:")
password = raw_input("Password:")
urlForPost = raw_input("URL:")

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
data = {'op':'login-main',
'user':username,
'passwd':password,
'api_type':'json'}
s.post("https://www.reddit.com/api/login/"+username, headers=headers, data=data)

page = s.get(urlForPost, headers=headers)
tree = html.fromstring(page.text)
Hashes = tree.xpath('//*[@id="config"]/text()')
Hashes = Hashes[0]
Hashes = Hashes[8:]
Hashes = Hashes[:-1]
Hashes = json.loads(Hashes)
print Hashes

data2 = {'uh': str(Hashes['modhash']),
'vh': str(Hashes['vote_hash']),
'id': str(Hashes['cur_link']),
'dir': "1", #-1 if downvote
'r': str(Hashes['post_site']),
'isTrusted':'true',
'renderstyle':'html'
}
print data2
s.post("https://www.reddit.com/api/vote", headers=headers, data=data2)
