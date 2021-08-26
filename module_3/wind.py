from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

def get_cuisines(url):
    try:
        result = []
        r = requests.get(url, headers=headers)
        soup = bs(r.text, "lxml")
        if soup.find(class_="_13OzAOXO _34GKdBMV"):
            for i in soup.find(class_="_13OzAOXO _34GKdBMV"):
                if "$" not in i.text:
                    result.append(i.text)
        if not result:
            return np.NAN
        return result
    except:
        time.sleep(1)


def get_price_range(url):
    try:
        result = np.NAN
        r = requests.get(url, headers=headers)
        soup = bs(r.text, "lxml")
        if soup.find(class_="_13OzAOXO _34GKdBMV"):
            for i in soup.find(class_="_13OzAOXO _34GKdBMV"):
                if "$" in i.text:
                    result = i.text
                    break
        return result
    except:
        time.sleep(1)


def get_num_of_reviews(url):
    try:
        result = np.NAN
        r = requests.get(url, headers=headers)
        soup = bs(r.text, "lxml")
        if soup.find(class_="_10Iv7dOs"):
            result = int(soup.find(class_="_10Iv7dOs").text.split()[0])
        return result
    except:
        time.sleep(1)