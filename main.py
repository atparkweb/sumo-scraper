import requests
import shutil
from bs4 import BeautifulSoup

# IMAGE PATTERN: /img/sumo_data/rikishi/270x474/20002320.jpg

profile_ids = [
  2320, 2416, 3521, 3682, 3582, 3321, 3265, 3620, 3376,
  2775, 3150, 3434, 3630, 3761, 3337, 3415, 3622, 3206,
  3464, 2759, 2629, 3498, 2895, 3255, 3661, 3594, 2938,
  3842, 3743, 2890, 3325, 3840, 3056, 3208, 3278, 3207,
  3012, 3504, 3683, 3417, 2950, 3665, 3148
]

base_url = 'http://sumo.or.jp/EnSumoDataRikishi/profile/?id='
headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}

for pid in profile_ids:
    url = base_url + str(pid)
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        results = soup.find(id='mainContent')
        images = results.find_all('img', class_='col1')

        for img in images:
            src = img.attrs['src']

            r = requests.get('http://sumo.or.jp/' + src, stream=True, headers=headers)
            if r.status_code == 200:
                with open('images/' + str(pid) + '.jpg', 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
