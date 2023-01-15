import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
import time
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
  }


banner = r"""{}
   _____           _               
  / ____|         | |              
 | |  __ _ __ __ _| |__   _____  __
 | | |_ | '__/ _` | '_ \ / _ \ \/ /
 | |__| | | | (_| | |_) |  __/>  < 
  \_____|_|  \__,_|_.__/ \___/_/\_\
   *Simple Tools For Grab Domains By Keyword.
   [!] Made With Love By indofans <3
""".format(Fore.GREEN)

def domains():
  os.system("clear")
  print(banner)
  search = str(input(Fore.BLUE+"KeywordDomains : "))
  max = str(input(Fore.RED+"Max Results Domains: "))
  url = "https://domains.tntcode.com/?domain_name_box={}&domain_name_box_2=&whois_status_box=&whois_email_box=&min_rank_box=&max_rank_box=&maximum_records_box={}&maximum_characters_box=&availability_box=any&sort=&order=".format(search,max)
  page = requests.get(url, verify=False, headers=headers)

  html_soup = BeautifulSoup(page.text, 'html.parser')

  dom = html_soup.find_all('textarea')

  print(Fore.WHITE + "Please Wait....")

  print(Fore.GREEN + "Saving Result..")
  time.sleep(5)
  file = open("result.txt", "a+")
  file.write(str(dom))
  print(Fore.GREEN + "Success Saving File, Check result.txt")
  time.sleep(3)

  how = input(str("Grab More Domain? Y/n : "))

  cek = ["Y","y"]

  if how in cek:
    os.system("python grab.py")
  else:
    return False


  print("Result ")
    
if __name__ == "__main__":
  domains()
