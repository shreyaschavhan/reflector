import requests
import fileinput
from urllib.parse import urlparse
from urllib.parse import parse_qs
from sys import argv

print("Output Saved in: ./output.txt \n\n")


keyword = "xssteststring"
output = open("output.txt", "a")

for url in fileinput.input(files = argv[1]):
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)

    url = url.split('?')[0]
    for i in params:
        r = requests.get(url+"?"+ i + "=" + keyword )
        if keyword in r.text:
            print(f"Status Code: {r.status_code} ==> Reflected : " + url+"?"+ i + "=" + keyword)
            output.write(url+"?"+ i + "=" + keyword + "\n")
        else:
            print(f"Status Code: {r.status_code} ==> Not Reflected: " + url+"?"+ i + "=" + keyword)

    

    
