import xml.dom.minidom as xm
import re
dom = xm.parse('blocklist.xml')  #get file object
root = dom.documentElement       #get element object
bb = root.getElementsByTagName('emItem') #get sub label
ID=[]
for i in bb:
    ID.append(i.getAttribute('id'))

for j in ID:
    b=re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.(gov|edu|int|mil|org|at|au|ca|de|dk|es|fr|uk|us|ch|com|cn|net){1,3}$',j)  # regular expression of requirement
    if b:
        n = ID.index(j) #get position
        print(bb[n].toxml().split('\n')[0])
