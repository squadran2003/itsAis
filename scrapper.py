import sys
import requests
from bs4 import BeautifulSoup


def find_ais(imo,mmsi,name):
    """this function takes a imo,
    mmsi and name of a vessel and
    return basic ais info"""

    imo = imo
    mmsi = mmsi
    name = name
    data = []
    url = "https://www.vesselfinder.com/vessels/{}-IMO-{}-MMSI-{}"
    url=url.format(name, imo, mmsi)
    source = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(source, "html.parser")
    tables = soup.find_all('table', {'class': 'tparams'})
    trs = tables[1].find_all('tr')
    for row in trs:
        cells = row.find_all('td')
        try:
            data.append({cells[0].text: cells[1].text})
        except IndexError:
            pass
    return data


if __name__ == '__main__':
    imo = sys.argv[1]
    mmsi = sys.argv[2]
    name = sys.argv[3]
    data = find_ais(imo, mmsi, name)
    print(data)
