import json

fd=open('products.json','r')
t=fd.read()
try:
    prd=json.loads(t)
except:
    prd={}


pid=input('enter the product id')
pname=input('enter the product name')
pcost=input('enter the product cost')
quantity=int(input('enter the product quntity'))
block=input('enter the product block')
weight=input('enter the product weight')
c=0
for i in prd:
    if prd[i]['name']==pname:
        c=prd[i]['quantity']
        break
    
quantity+=c
print(quantity)
temp={'name':pname,'cost':pcost,'quantity':quantity,'block':block,'weight':weight}
prd[pid]=temp
fd.close()
fd=open('products.json','w')
t=json.dumps(prd)
fd.write(t)
fd.close()