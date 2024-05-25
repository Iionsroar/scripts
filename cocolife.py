# python3.12

from bs4 import BeautifulSoup
import requests
import pprint
import re 

URL = 'https://www.cocolife.com/wp-content/uploads/2019'

get_soup = lambda url : BeautifulSoup(requests.get(url).text, 'html.parser')
get_links = lambda soup: [link.get('href') for link in soup.find_all('a')]

re_ignore = r'(jpe*g)|(gif)|(heic)|(png)|(svg)|(pdf)|(zip)|(mp4)|(wp-content/uploads/)|(\w=\w;\w=\w)'
is_ignorable = lambda file : False if re.search(re_ignore, file) else True
ignore_irrelevant = lambda files: list(filter(is_ignorable, files))

# re_dental = r'(\bdentist)|(\bdental)' # use word boundary
re_dental = r'(dentist)|(dental)' # use this as i might be missing some stuff
is_dental_file = lambda file : True if re.search(re_dental, file, re.IGNORECASE) else False
filter_dental_files = lambda files: list(filter(is_dental_file, files))

is_directory = lambda link : True if '/' in link else False
filter_directories = lambda links: list(filter(is_directory, links))

def print_dental_files():
  URL = 'https://www.cocolife.com/wp-content/uploads'
  YEAR_DIRECTORIES = ['2019', '2020', '2021', '2022', '2023', '2024']
  for year in YEAR_DIRECTORIES:
    url = f'{URL}/{year}/'
    
    soup = get_soup(url)
    links = get_links(soup)
    directories = ignore_irrelevant(filter_directories(links))
    
    for directory in directories:
      final_url = f'{url}/{directory}'
      
      soup = get_soup(final_url)
      links = get_links(soup)
      files = filter_dental_files(links)

      if files:
        print(final_url)
        pprint.pprint(files)
        print()

  


def print_databases():
  '''
  Search for database/ xlsx files or the like
  '''
  
  for i in range(6, 11):
    index = str(i).rjust(2, '0')
    url = f'{URL}/{index}/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(url)
    pprint.pprint(ignore_irrelevant(get_links(soup)))
    print()
    
print_dental_files()