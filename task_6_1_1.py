import requests
import pyodbc

#-----------------------------------------------------------
def FIRST_STEP():
    URL_1='https://invictusfitness.perfectgym.com/Api/oauth/authorize'
    headers_1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'username':'apiuser', 'password':"h7lR.'M8xA", 'grant_type':'password'}
    r = requests.post(URL_1, headers=headers_1,data = payload )
    rr=r.json()
    global tokens
    tokens=('Bearer' +  ' ' + rr['access_token'])
#-----------------------------------------------------------------------------------------------
def SECOND_STEP(tokens):
    URL_2='https://invictusfitness.perfectgym.com/Api/Classes/Classes/1'
    headers_2 = {'Authorization':'NOne'}
    headers_2['Authorization']= tokens
    r_2 = requests.post(URL_2, headers=headers_2)
    # print(r_2.text)

#-----------------------------------------------------------------------------------------------
a=0
def Request_visits(tokens,a):
    sett = []
    # Connecting -----------------
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};' 
                          'Server=LAPTOP-QHTHN2FI\MSSQLSERVER01;' 'Database=master;''Trusted_Connection=yes;',
                          autocommit=True)
    # Making request --------------------
    URL_3 = 'http://invictusfitness.perfectgym.com/Api/Users/ClubVisits/All?timestamp=0'
    headers_3 = {'Authorization': 'Bearer  $ACCESS_TOKEN'}
    headers_3['Authorization'] = tokens
    r_3 = requests.get(URL_3, headers=headers_3)
    r_3 = r_3.json()
    ele = r_3['elements']
    # Inserting data -----------
    for i in ele:
        sett.append(i['timestamp'])
        query = 'insert into Invictus_Fitness_Astana_1(EnterDate, ExitDate, Club_name, Club_shortname, Club_symbol, Club_number , Club_email , Club_Phone_Number , Club_latitude , Club_longitude, Club_timeone, Club_open_date, Club_adress_line_1, Club_adress_line_2, Club_adress_city, Club_adress_postalCode, Club_adress_country, Club_adress_country_symbol,Club_adress_stateSymbol, Club_type, Club_isHidden, Club_clubPhotoUrl, Club_ID, Club_timestamp, Club_isDelated,UserId,id,Timestamp_,isDeleted) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        args = (i['enterDate'], i['exitDate'], i['club']['name'], i['club']['shortName'], i['club']['symbol'],
                i['club']['number'], i['club']['email'], i['club']['phoneNumber'], i['club']['latitude'],
                i['club']['longitude'], i['club']['timeZone'], i['club']['openDate'], i['club']['address']['line1'],
                i['club']['address']['line2'], i['club']['address']['city'], i['club']['address']['postalCode'],
                i['club']['address']['country'], i['club']['address']['countrySymbol'],
                i['club']['address']['stateSymbol'], i['club']['type'], i['club']['isHidden'],
                i['club']['clubPhotoUrl'], i['club']['id'], i['club']['timestamp'], i['club']['isDeleted'], i['userId'],
                i['id'], i['timestamp'], i['isDeleted'])
        conn.execute(query, args)
    a = sett[-1]
    #------------------------------------
    while len(sett)!=0:
        URL_3='http://invictusfitness.perfectgym.com/Api/Users/ClubVisits/All?timestamp='+str(a)
        headers_3={'Authorization': 'Bearer  $ACCESS_TOKEN'}
        headers_3['Authorization'] = tokens
        r_3=requests.get(URL_3, headers = headers_3)
        r_3=r_3.json()
        ele=r_3['elements']
        sett.clear()
        #Inserting data -----------
        for i in ele:
            sett.append(i['timestamp'])
            query = 'insert into Invictus_Fitness_Astana_1(EnterDate, ExitDate, Club_name, Club_shortname, Club_symbol, Club_number , Club_email , Club_Phone_Number , Club_latitude , Club_longitude, Club_timeone, Club_open_date, Club_adress_line_1, Club_adress_line_2, Club_adress_city, Club_adress_postalCode, Club_adress_country, Club_adress_country_symbol,Club_adress_stateSymbol, Club_type, Club_isHidden, Club_clubPhotoUrl, Club_ID, Club_timestamp, Club_isDelated,UserId,id,Timestamp_,isDeleted) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
            args=(i['enterDate'], i['exitDate'], i['club']['name'],i['club']['shortName'],i['club']['symbol'],i['club']['number'], i['club']['email'], i['club']['phoneNumber'], i['club']['latitude'], i['club']['longitude'], i['club']['timeZone'], i['club']['openDate'],i['club']['address']['line1'], i['club']['address']['line2'],i['club']['address']['city'],i['club']['address']['postalCode'],i['club']['address']['country'], i['club']['address']['countrySymbol'],i['club']['address']['stateSymbol'], i['club']['type'],i['club']['isHidden'], i['club']['clubPhotoUrl'], i['club']['id'],i['club']['timestamp'],i['club']['isDeleted'],i['userId'],i['id'],i['timestamp'],i['isDeleted'])
            conn.execute(query, args)
            a=sett[-1]
        print(a)
    else:
        print('End of iteration')
# while len(sett) != 0:
FIRST_STEP()
SECOND_STEP(tokens)
Request_visits(tokens,a)
print('The end')
# while len(sett) != 0:
#     Pagination(tokens)
#     Request_visits(tokens, timestamp)




