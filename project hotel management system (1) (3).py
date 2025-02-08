import math
rd={
    'R001':{'Type':'single bed non AC','Charges':600},
    'R002':{'Type':'double bed non AC','Charges':900},
    'R003':{'Type':'single bed with AC','Charges':1200},
    'R004':{'Type':'double bed with AC','Charges':1500},
    'R005':{'Type':'suite','Charges':2000}
    }
rno={
    'R001':[101,103,106],
    'R002':[102,107],
    'R003':[104,108],
    'R004':[105,109,112],
    'R005':[110,111]
    }
rno1={
    'R001':[101,103,106],
    'R002':[102,107],
    'R003':[104,108],
    'R004':[105,109,112],
    'R005':[110,111]
    }
ef=[
    {
        'Basic':['Room Service', 'Child day Care'],
        'price':'1300'
    },
    {
        'Classic':['Room Service', 'Child day Care','Gym'],
        'price':'1800'
    },
    {
        'Premium':['Room Service', 'Child day Care','Gym','Swimming pool', 'Playzone for kids'],
        'price':'2500'
    }
    ]
detailsList=[]
m=[31,28,31,30,31,30,31,31,30,31,30,31]
while True:
    print("                          __::WELCOME TO THE IDEAL HOTEL::__                                      ")
    print(' ')
    print('Main Menu')
    print(' ')
    print("1.Guest details ")
    print("2.Booking")
    print("3.Report")
    print("0.Exit")
    print(' ')
    ch=int(input("Enter your choice:"))
    if ch==1:
        print(' ')
        print('__::GUEST DETAILS::__')
        print(' ')
        name=input("Enter name:")
        while name.isalpha() != True:
             name=input("Enter valid name:")
        age=input("Enter age:")
        while age.isdigit() != True:
             age=input("Enter valid age:")
        address=input("Enter address:")
        phno=input("Enter phone no.:")
        if len(phno)<10 or len(phno)>10:
             print('invalid number: Please enter a valid 10 digit number')
             phno=input("Enter valid phone no.:")
             while phno.isdigit() != True or len(phno)<10 or len(phno)>10:
                  phno=input("Enter valid phone no.:")
        email=input("Enter email address:")
        gd={
            'cId':len(detailsList)+1,
            'cName':name,
            'cAge':age,
            'cAddress':address,
            'cPhone':phno,
            'cEmail':email,
            'allotedRoom': '',
            'roomType':'',
            'checkinDate':'',
            'checkoutDate':'',
            'nosOfDays':'',
            'facilityType':'',
            'amount':''
            }
        detailsList.append(gd)
    elif ch==2:
        print(' ')
        print('__::BOOKING::__')
        print(' ')
        if len(detailsList)==0:
            print('Please fill the guest form first')
            print(' ')
            continue
        else:
            for i in range(len(detailsList)):
                print('Enter '+ str(i+1) + ' for customer named ' + str(detailsList[i]['cName']))
            print(' ')
            print('Please select the guest from the list to proceed forward:')
            print(' ')
            guestIndex=int(input("Enter your choice of guest:"))
            print(' ')
            while guestIndex>len(detailsList):
                guestIndex=int(input("Enter a valid choice of guest:"))
                print(' ')
        count=1
        for n in rd.keys():
            if len(rno[n]) >0:
                print(str(count) + "." + rd[n]['Type'] + " ==> Charges: "+ str( rd[n]['Charges']))
                count+=1
        rt=int(input("Enter choice of room:"))
        while rt <0 or rt> len(rd):
            rt=int(input('Enter a valid choice of room:'))
        while True:
            print(' ')
            checkinDate=input("Enter the date of checkin(example-DD/MM/YYYY) :")
            print(' ')
            cidd=int(checkinDate[0:2])
            cimm=int(checkinDate[3:5])
            ciyy=int(checkinDate[6:])
            if ciyy%400==0:#leap year check
                m[1]=29
            elif cimm>=1 and cimm<=12:
                if cidd>=1 and cidd<=m[cimm-1]:
                    break
                else:
                    print("Invalid day")
            else:
                print("Invalid month")
        while True:
            print(' ')
            checkoutDate=input("Enter the date of checkout(example-DD/MM/YYYY) :")
            print(' ')
            codd=int(checkoutDate[0:2])
            comm=int(checkoutDate[3:5])
            coyy=int(checkoutDate[6:])
            if coyy%400==0:#leap year check
                m[1]=29
            elif comm>=1 and comm<=12:
                if codd>=1 and codd<=m[comm-1]:
                    break
                else:
                    print("Invalid day")
            else:
                print("Invalid month")
        days_in_year = 365.2425  # average number of days in a year, including leap years
        epoch = "1970-01-01"
        
        days_since_epoch1 = (ciyy - int(epoch[:4])) * days_in_year
        days_since_epoch2 = (coyy - int(epoch[:4])) * days_in_year
        
        days_since_epoch1 += cimm * 30.5
        days_since_epoch2 += comm * 30.5
        
        days_since_epoch1 += cidd
        days_since_epoch2 += codd
        
        nosOfDays = abs(days_since_epoch1 - days_since_epoch2)
        math.ceil(nosOfDays)

        print('__::PACKAGE CHOICE::__')
        print(' ')
        print('1. Basic Package includes: room service, child day care--> Rs 1300')
        print('2.Classic Package includes: Basic Package + gym--> Rs 1800')
        print('3 .Premium Package includes: Classic Package + swimming pool,Playzone for kids--> Rs 2500')
        print(' ')
        selectedPackage=int(input("Enter your choice of package:"))
        detailsList[guestIndex-1]['checkinDate']=checkinDate
        detailsList[guestIndex-1]['nosOfDays']=nosOfDays
        detailsList[guestIndex-1]['checkoutDate']=checkoutDate
        detailsList[guestIndex-1]['facilityType']= ef[selectedPackage-1]
        initialRoomcharges = ((int(rd['R00' +str(rt)]['Charges']) * nosOfDays))
        initialAmt= int(ef[selectedPackage-1]['price']) + initialRoomcharges
        detailsList[guestIndex-1]['amount']= initialAmt + ((18/100)* initialAmt)
        print('Press 1 to Confirm:')
        print('Press 0 to Cancel')
        print(' ')
        confirmation= int(input('Enter your choice: '))
        if confirmation==1:
            print(' ')
            print('\t\t\t\t','_::THE IDEAL HOTEL::_')
            print(' ')
            print('\t\t\t\t\t','_::BILL::_','\t\t')
            print(' ')
            print('\t','Name:',detailsList[guestIndex-1]['cName'],'\t\t','Phone No:',detailsList[guestIndex-1]['cPhone'],'\t\t','Age:',detailsList[guestIndex-1]['cAge'])
            print('\t','Address:',detailsList[guestIndex-1]['cAddress'],'\t\t','Email Id:',detailsList[guestIndex-1]['cEmail'])
            print('\t','Room Number:',rno['R00'+str(rt)][0])
            print('\t','_::PARTICULARS::__','\t\t','__::AMOUNT::__')
            print('\t','Room Charges@','\t\t\t',initialRoomcharges)
            print('\t','Facilities:','\t\t\t',detailsList[guestIndex-1]['facilityType']['price'])
            print('\t','Add:18% GST','\t\t\t',(18/100)* initialAmt)
            print('\t','Total Amount:','\t\t\t',detailsList[guestIndex-1]['amount'])
            print(' ')
            print('__::PAYMENT::__')
            print(' ')
            print('Payment Successful')
            ar=rno['R00'+str(rt)].pop()
            detailsList[guestIndex-1]['allotedRoom']=ar
            detailsList[guestIndex-1]['roomType']=rd['R00' +str(rt)]['Type']
        elif confirmation==0:
            print('Payment Cancelled')
            print('Thank you for your time,Hope to see you soon')
            continue
        else:
            print('Enter a valid choice')
    elif ch==3:
        print(' _::REPORT::_')
        print(' ')
        print('1.Room Types')
        print('2.Room Number of Particular Type')
        print('3.Facalities Available')
        print('4.Guest details')
        print('5.Booking details')
        print('6.Return to Main Menu')
        print(' ')
        rep=int(input('Enter your choice:'))
        if rep==1:
            print('__::ROOM TYPES::__')
            print(' ')
            romtyCount=1
            for romty in rd:
                 print(romtyCount,'.',rd['R00'+str(romtyCount)]['Type'])
                 romtyCount+=1
        elif rep==2:
            print('__::ROOM NUMBER OF PARTICULAR TYPE::__')
            print(' ')
            romnoCount=1
            for romno in rd:
                print(romnoCount,'.',rd['R00'+str(romnoCount)]['Type'],':',rno1['R00'+str(romnoCount)])
                romnoCount+=1
        elif rep==3:
            print('__::FACALITIES AVAILABLE::__')
            print(' ')
            print('1. Basic Package includes: room service, child day care')
            print('2.Classic Package includes: Basic Package + gym')
            print('3 .Premium Package includes: Classic Package + swimming pool,Playzone for kids')
            print(' ')
        elif rep==4:
            guestdCount=1
            for i in range(len(detailsList)):
              if detailsList[i]['amount'] != ' ':
                print('Customer No.',guestdCount)
                print('Name:', detailsList[i]['cName'] ,'\t', 'Age: ', detailsList[i]['cAge'])
                print('Address:',detailsList[i]['cAddress'],'\t','Phone No.:',detailsList[i]['cPhone'])
                print('Email Address:',detailsList[i]['cEmail'])
                guestdCount+=1
        elif rep==5:
            guestbCount=1
            for j in range(len(detailsList)):
              if detailsList[j]['amount'] != ' ':
                   print('Customer No.',guestbCount)
                   print('Room Type:', detailsList[j]['roomType'] ,'\t', 'Room No.: ', detailsList[j]['allotedRoom'])
                   print('Check in Date:',detailsList[j]['checkinDate'],'\t','Check out Date.:',detailsList[j]['checkoutDate'])
                   print('Facalities:',detailsList[j]['facilityType'],'\t','Total Amount.:',detailsList[j]['amount'])
                   guestbCount+=1
        elif rep==6:
            print('__::THANK YOU::__')
            continue
    elif ch==0:
        print('Thank you for choosing us')
        break
else:
    print('Please enter correct option from the list')
    
       



