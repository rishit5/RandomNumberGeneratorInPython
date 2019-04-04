import http.client
import pprint
from time import sleep
import re
def foo(n):
    return eval(n)

def HttpGetResponse():
    num_of_randno = "1"
    minimum = "10"
    maximum = "100"
    col = "1"
    base = "10"
    form = "plain" 
    URL = "/integers/?" + "num=" + num_of_randno + "&min=" + minimum + "&max=" + maximum + "&col=" + col + "&base=" + base + "&format=" + form + "&rnd=new"
    connection = http.client.HTTPSConnection("www.random.org")
    connection.request("GET", URL)
    # print(URL)
    response = connection.getresponse()
    data1 = response.read().decode("utf-8")
    # print(eval(data1))
    # res = list(map(foo, data1.split('\n')))
    connection.close()
    return eval(data1)

if __name__ == "__main__":
    # data1 = [14, 11, 2, 6, 18, 23, 7, 21, 1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28, 22, 4, 12, 5, 15]
    seed = HttpGetResponse()
    # seed = 15
    print("Seed value from Random.org is:" + str(seed))
    data1 = [0] * 30
    data1[0] = seed*3 % 31
    for i in range(1,30):
        data1[i] = data1[i-1]*3 % 31
    print("Sequence of Random Numbers genrated are: " + str(data1))
    data1 = [x/31 for x in data1]
    # print(data1)
    data1.sort()
    data2 = data1.copy()
    # print(data2)
    for i in range(30):
        data1[i] = ((i+1)/30) - data1[i]
        data2[i] = data2[i] - ((i)/30)
    print("Tablulated Values for (j/n - xj) : ")
    pprint.pprint(data1, indent = 1) 
    print("Tablulated Values for (xj - j-1/n) :")
    pprint.pprint(data2) 
    print("Maximum Observed Value That was calcluated from the KS Test is :" + str(max(max(data1), max(data2))))
    # print(max(data2))
