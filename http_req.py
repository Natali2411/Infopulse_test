import requests

#url = "http://httpbin.org/get"
#headers = {'user-agent': 'my-app/0.0.1'}
#r = requests.get(url, headers=headers)

#print(r.url)
#print(r.status_code)
#print(r.headers)
#print(type(r.text))

#print(r.json()['headers']['User-Agent'])


url1 = 'http://pulse-rest-testing.herokuapp.com/books/'
'''
r = requests.post(url1,data={'title':'Book1', 'author':'Tiutiunnyk3'})
print(r.status_code)
print(r.text)'''

r1 = requests.delete(url1+'1587')
#print(r.status_code)