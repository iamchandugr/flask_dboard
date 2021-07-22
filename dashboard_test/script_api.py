import requests
listofendpoints = ['hello/','test1/', 'test2/', 'test3/', 'test4/']
for i in listofendpoints:
    s  = "http://localhost:5000/contact/"+i
    response = requests.get(s)
    print(response)
    #print("http://localhost:5000/contact/"+i)
    response = requests.get("http://localhost:5000/home/"+i)
