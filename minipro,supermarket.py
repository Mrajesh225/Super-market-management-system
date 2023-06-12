# from datetime import datetime

# name=input('Enter your name:')
# # list of items

# list='''
# rice   Rs 30/kg
# oil    Rs 200/lit
# sugar  Rs 40/kg
# surf   RS 80/KG
# sampoo Rs 50/5g
# pen    Rs 40/pack
# '''
# price=0
# pricelist=[]
# totalprice=0
# finalprice=0
# itemlist=[]
# plist=[]
# qlist=[]
#  # rates of items
# items={'rice':30,'oil':200,'sugar':40,'surf':80,'sampoo':50,'pen':40}
# option=int(input('for list of item press 1:'))
# if option==1:
#    print(list)
# for i in range(len(items)):
#    inp1=int(input('to buy press 1 or 2 for bill:'))
#    if inp1==2:
#       break
#    if inp1==1:
#       item=input('enter your items:')
#       quantity=int(input('quantity of items:'))
#       if item in items.keys():
#           price=quantity*(items[item])
#           pricelist.append((item,quantity,items,price))
#           totalprice+=price
#           itemlist.append(item)
#           qlist.append(quantity)
#           plist.append(price)
#           gst=(totalprice*3)/100
#           finalamount=gst+totalprice
#    else:
#       print('not available')     
# else:
#    print('wrone one')
# inp=input('billing items yes or no:')
# if inp=='yes':
#    pass
#    if finalamount!=0:
#       print(20*'*','PR super market',20*'*')
#       print(25*' ','kodad',25*' ')
#       print('Name:',name)
#       print('date:',datetime.now())
#       print(60*'-')
#       print('sno',5*' ','items',10*' ','quantity',5*' ','price')
#       for i in range(len(pricelist)):
#            print(i,'',5*' ',itemlist[i],15*' ',qlist[i],10*' ',plist[i])
#       print(12*' ')     
#       print(25*' ','totalAmount:','Rs',totalprice)
#       print(25*' ','gst amount:','Rs',gst)
#       print(25*' ','finalAmount:','Rs',finalamount)
#       print(60*'-')
#       print(20*' ','**Thankyou**')
#       print(20*' ','wisit again')
#       print(60*'*')
