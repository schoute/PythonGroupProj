# # Use the Request library
import requests
# # Set the target webpage
url = 'https://brickset.com/sets/year-2001'
r = requests.get(url)
# # This will get the full page
print(r.text)

# # This will get the status code
print("Status code:")
print("\t *", r.status_code)

# # This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# # This will just get just the headers
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
# # This will modify the headers user-agent
headers = {
    'User-Agent' : 'Mobile'
}
# # Test it on an external site
url2: str = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text, )



# line 29 for some reason will fetch the whole website all over again
# need to figure out how to output the user agent part only
# Use the Request library
# import requests
# # Set the target webpage
# url = 'https://brickset.com/sets/year-2001'
# r = requests.get(url)
# # This will get the full page
# print(r.text)
# # This will modify the headers user-agent
# headers = {
# 'User-Agent' : 'Mobile'
# }
# # Test it on an external site
# url2 = 'https://brickset.com/sets/year-2001'
# rh = requests.get(url2, headers=headers)
# print(rh.text)

