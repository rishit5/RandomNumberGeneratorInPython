import http.client
from time import sleep
import re
if __name__ == "__main__":
    num_of_randno = "1"
    minimum = "1"
    maximum = "100"
    col = "1"
    base = "10"
    form = "plain" 
    URL = "/integers/?" + "num=" + num_of_randno + "&min=" + minimum + "&max=" + maximum + "&col=" + col + "&base=" + base + "&format=" + form + "&rnd=new"
    connection = http.client.HTTPSConnection("www.random.org")
    connection.request("GET", URL)
    print(URL)
    response = connection.getresponse()
    data1 = response.read().decode("utf-8")
    # print(type(data1))
    # x = re.findall("[0-9]+", data1)
    print("The random number generated from Random.org is:"+data1)
    connection.close()