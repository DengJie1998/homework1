import xml.dom.minidom as xm
import re
dom = xm.parse('blocklist.xml') #get file object
root = dom.documentElement      #get element object
bb = root.getElementsByTagName('emItem')  #get sub label
blockID=[]
for i in bb:
    blockID.append(i.getAttribute('blockID'))

for j in blockID:
    b=re.match('^i.*\d$|^g.*\d$',j)  #regular expression of requirement
    if b:
        n = blockID.index(j)  #get position
        print(bb[n].toxml().split('\n')[0])
