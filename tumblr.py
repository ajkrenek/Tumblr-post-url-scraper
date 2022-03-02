from tumblpy import Tumblpy
import json
import re

ck = 'consumer key'
cs = 'consumer secret'
ot = 'oauth token'
os = 'oauth secret'

self = Tumblpy(ck, cs, ot, os)
#extracts posts from blog
url = ""
posts = self.get('posts',url)

#convert tumblr dictionary to string
post_string = json.dumps(posts)

#regex searches for urls
post_url = re.findall(r'''
#structure of post url : https://somename.tumblr.com/post/12094812094814/some-post-name
https?://                      # https part
(?:[-\w.]|(?:%[\da-fA-F]{2}))+ # name.tumblr part
/                              # forward slash
\w+                            #'post'
/                              # forward slash
\d+                            # the digits
/                              # forward slash
[\w-]*                         # some-post-name
''',post_string, re.VERBOSE)


#appends to a file
file = open("tumblr.txt", 'w')
with file as f:
    for url in post_url:
        f.write(url)
        f.write('\n')

file.close()
