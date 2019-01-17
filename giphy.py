import requests
import os
from pprint import pprint as pp

api_key = os.environ['giphy_key']

base_url = "http://api.giphy.com/v1/gifs/search?"

#python3으로 해야함!

def make_url(query):
    return base_url + "q={}&api_key={}&limit=20".format(query,api_key)
    
def request_and_parse(url):
    res = requests.get(url)
    return res.json()

def get_images(parsed_dic):
    #pp(parsed_dic.get('data')[0])
    images = [data.get('images').get('original').get('url') for data in parsed_dic.get('data')]
    #slugs = [data.get('slugs') for data in parsed_dic.get('data')]
    #url을 기준으로 파일다운로드를 한다.
    #다운로드: 커맨드 - wget
    return [images[5*x:5*(x+1)] for x in range(4)] #\[slugs[5*x:5*(x+1)] for x in range(4)]
 
if __name__ == "__main__":
    query = input()  
    cat_url = make_url(query)
    parsed_dic = request_and_parse(cat_url)
    images = get_images(parsed_dic)
    print(images)

