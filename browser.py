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
print("Mobile")
# # This will just get just the headers
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
# # This will modify the headers user-agent
# headers = {
#     'User-Agent' : 'Mobile'
# }
# # Test it on an external site
# #
# url2: str = 'https://brickset.com/sets/year-2001'
# rh = requests.get(url2, headers=headers)
# print(rh.text)
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
# its the website that refuses to output properly
# msaybe want just start diff part??
# ok i go ask my friend
# maybe can ask our classmates first, cher might expect us to modify to code a little to get it to work ty
# since this part cannot do for now, lets go do the other parts
#part 10c need to install pyton3-pip, ayt ill do it now
#I think if still cannot get the result we expected,just ss what we have to cher.
# isnt it a presentation?
#Need to do presentation?Cause i know that monday last day of submission. If im not wrong yea we need to present if not
# if not then good i guess