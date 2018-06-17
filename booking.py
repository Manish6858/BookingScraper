import sys
sys.path.insert(0, "./lib/python3.5/site-packages")


import os
os.system('pip install -r ./requirements.txt')

import requests
from bs4 import BeautifulSoup


def get_booking_page(offset):
      url = 'https://www.booking.com/searchresults.en-gb.html?aid=304142&label=gen173nr-1DCAEoggJCAlhYSDNYBGiTAYgBAZgBLsIBCndpbmRvd3MgMTDIAQzYAQPoAQGSAgF5qAID&' \
            'sid=716ea5d78c4043fd78b7a1410d639e3d&checkin_month=6&checkin_monthday=8&checkin_year=2018&checkout_month=6&checkout_monthday=11&checkout_year=2018' \
            '&class_interval=1&dest_id=125&dest_type=country&dtdisc=0&from_sf=1&genius_rate=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef' \
            '&no_rooms=1&postcard=0&raw_dest_type=country&room1=A%2CA&sb_price_type=total&src=searchresults&src_elem=sb&ss=Macedonia&ss_all=0&ssb=empty&sshis=0&ssne=Macedonia' \
            '&ssne_untouched=Macedonia&rows=15&offset=' + str(offset)
      r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/48.0'})
      html = r.content
      parsed_html = BeautifulSoup(html, "lxml")
      return parsed_html



if __name__ == "__main__":
    get_data()
