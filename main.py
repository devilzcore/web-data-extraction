import requests
from bs4 import BeautifulSoup as bs

def get_name(soup):
    name_tag = soup.find('span', {'class': 'p-name vcard-fullname d-block overflow-hidden'})
    if name_tag:
        return name_tag.get_text(strip=True)
    return 'Name not found.'

def get_profile_image(soup):
    img = soup.find('img', {'alt': 'Avatar'})['src']
    if img:
        return img
    return 'Image not found.'

def get_description(soup):
    description_tag = soup.find('div', {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'})
    if description_tag:
        return description_tag.get_text(strip=True)
    return 'Description not found.'

def get_repository_count(soup):
    repo_count_tag = soup.find('span', {'class': 'Counter'})
    if repo_count_tag:
        return repo_count_tag.get_text(strip=True)
    return 'Repositories not found.'

git_user = input("Github user: ")
url = 'https://github.com/'+git_user
res = requests.get(url)
soup = bs(res.content, 'html.parser')

name = get_name(soup)
profile_image = get_profile_image(soup)
description = get_description(soup)
repository_count = get_repository_count(soup)

print('Name:', name)
print('Profile Image:', profile_image)
print('Description:', description)
print('Total repositories published:', repository_count)
