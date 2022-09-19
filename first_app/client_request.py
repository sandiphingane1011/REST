from email import header
import json
from urllib import request
import requests





# client Application -paytm
# requests -API consume
# pip install requests 




# GET_SIGNAL_DATA_URL ="http://127.0.0.1:8000/get-stud/"


# def get_signal_date():
#     response = requests.get(GET_SIGNAL_DATA_URL + str(id) + '/')
#     print(response.json())


# # get_signal_date(1)   


# GET_ALL_URL = "http://127.0.0.1:8000/get-all-stud/" 
# def get_all_data():
#     response = requests.get(GET_ALL_URL)
#     print(response.content)
#     print(response.json()) # python data

# get_all_data()

#API_URL = "http://127.0.0.1:8000/student-api/"   # final


CLASS_API_URL = "http://127.0.0.1:8000/stud-class-api/"  # final




def get_single_or_alldata(sid=None):
    data = {}  # empty dict - json 
    if sid:
         data = {"id": sid}
    json_data = json.dumps(data)
    resp = requests.get(CLASS_API_URL, data=json_data)
    print(resp.json())

# get_single_or_alldata() 

def post_data(d):
    response = requests.post(CLASS_API_URL, json=d)
    print(response.json())

d = {"name": "Ranchoddas", "age": 20, "city": "pune","marks":75}
post_data(d)


def put_data(data):
    resp = requests.put(CLASS_API_URL, json=data)
    print(resp.json)




# d = {"id":1,"name": "ABCD", "age": 21, "city": "Latur","marks": 87}
d = {"id": 20, "name": "silencer"}
put_data(d)


def delete_data(dat):
    resp = requests.delete(CLASS_API_URL, json=dat)
    print(resp.json())

# delete_data({'id': 1})

#########################################################################################################


API_URL = "http://127.0.0.1:8000/studentapi/"   # final

headers = {'content-Type': 'application/json'}

def get_single_or_alldata(sid=None):
    data = {}  # empty dict - json 
    if sid:
         data = {"id": sid}
    json_data = json.dumps(data)
    resp = requests.get(API_URL,headers=headers ,data=json_data)
    print(resp.json())

# get_single_or_alldata() 

def post_data(d):
    response = requests.post(API_URL, headers=headers, json=d)
    print(response.json())

# d = {"name": "Ranchoddas", "age": 20, "city": "pune","marks":75}
# post_data(d)


def put_data(data):
    resp = requests.put(API_URL,headers=headers, json=data)
    print(resp.json)




# d = {"id":1,"name": "HHH", "age": 21, "city": "Latur","marks": 87}
d = {"id": 25, "name": "silencer"}
put_data(d)


def delete_data(dat):
    resp = requests.delete(API_URL,headers=headers, json=dat)
    print(resp.json())

# delete_data({'id': 1})