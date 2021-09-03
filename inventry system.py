import json
import time
import sys
import random
def sales(x,y,z,d,phone):
    tid=random.randint(0,100000000000)
    name=input('your name ')
    print("here is your bill\n")
    print("###########################\ntransaction id:",tid,
          "\t",time.ctime(),"\nNAME:",name,"\nproduct:",x,"\nquantity:",y,"\nTotal:",y*z-y*z*d*.05,
          "\n##########################")
    fd=open('sales.json','r')
    try:
        p=json.loads(fd.read())
    except:
        p={}
    fd.close()
    fd=open('sales.json','w')
    temp={'name':name,'cost':y*z,'date':time.ctime()}
    p[tid]=temp
    txt=json.dumps(p)

    fd.write(txt)
    fd.close()
    fd=open('customer_detail.json','r+')
    try:
        p=json.loads(fd.read())
    except:
        p={}
    fd.close()
    fd=open('customer_detail.json','w')
    temp={'name':name,'phone number':phone}
    p[tid]=temp
    txt=json.dumps(p)
    fd.write(txt)
    fd.close()
    
fd=open('products.json','r')
prd=json.loads(fd.read())
fd.close()
c=int(input("################ WELECOME ##################\n1 for owner\n2 for customer"))
if(c==1):
    ch=int(input("1 for sales of day\n2 for customer details"))
    if(ch==1):
        fd=open('sales.json','r')
        try:
            txt=fd.read()        
            print('##################todays sales deatial ##########################')
            txt=json.loads(txt)
            for i in txt:
                print("transaction id:",i," name:",txt[i]['name'],'cost:',txt[i]['cost'],"date:",
                      txt[i]['date'])
        except:
            print("no data still")
            sys.exit()
        
        fd.close()
    elif(ch==2):
        fd=open('customer_detail.json','r')
        try:
            txt=fd.read()
            print('################### customer details ##########################')
            txt=json.loads(txt)
            for i in txt:
                print("transaction id:",i," name:",txt[i]['name'],'phone number:',txt[i]['phone number'])
        except:
            print("no data still")
            sys.exit()
        
        fd.close()
else:
    print("We are having these many items select any one")
    for j,i in enumerate(prd.items()):
        print(j+1,"-",i[1]['name'])
    choice=int(input('enter respective number to purchase'))
    print('selected item is',prd[list(prd.keys())[choice-1]]['name'])
    hm=int(input("HOW MUCH? "))
    dis=int(input("give phone number to avail 5% discount(response 1 or 0)"))
    if dis:
        phone=input('phone number:')
    else:
        phone=0
    prd[list(prd.keys())[choice-1]]['quantity']=prd[list(prd.keys())[choice-1]]['quantity']-hm
    sales(prd[list(prd.keys())[choice-1]]['name'],hm,prd[list(prd.keys())[choice-1]]['cost'],dis,phone)
    fd=open('products.json','w')
    t=json.dumps(prd)
    fd.write(t)
    fd.close()
    

