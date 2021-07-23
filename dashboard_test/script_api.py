import requests
listofendpoints = ['hello/','test1/', 'test2/', 'test3/', 'test4/']
for _ in range(1, 2):
    for i in listofendpoints:
        s  = "http://localhost:5000/contact/"+i
        response = requests.get(s)

        #print("http://localhost:5000/contact/"+i)
        response = requests.get("http://localhost:5000/home/"+i)
        print(response)
