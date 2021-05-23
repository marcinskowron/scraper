import sys

import requests
from bs4 import BeautifulSoup

# url = 'https://www.w3schools.com/tags/tag_meta.asp'


def get_keywords(url):
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    result = []
    for tag in soup.find_all("meta"):
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() == 'keywords':
            result.append(tag.attrs['content'])
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(get_keywords(sys.argv[1]))
    else:
        print('URL needed.')
