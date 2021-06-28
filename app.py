import requests
import json
import urllib.request

import csv
from time import sleep

API_KEY = "AIzaSyAY4NyT3Du5c9i9Vs26mnt6dTJn76tKnVw"
PS_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="





def page_speed(API_KEY, link_url, PS_URL, platform ):

    main_url = PS_URL + link_url + '&key='+API_KEY+'&strategy='+platform
    response = urllib.request.urlopen(main_url)
    result_json = json.loads(response.read())
    fcp = result_json["originLoadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]
    lcp = result_json["originLoadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]
    cls = result_json["originLoadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"]


    avg= (fcp+lcp+cls)/3
    # print(type(result_json))
    # print(fcp)
    # print(lcp)
    # print(cls)
    print(avg)
    return avg
    sleep(0.8)

    # lighthouseResult = result_json["lighthouseResult"]
    # category = lighthouseResult["categories"]
    # perfm = category["performance"]
    # score = perfm["score"]
    # print(score*100)
# for ur in url:
#     page_speed(API_KEY, ur, PS_URL, "mobile")

csv_input=open('content-landing-pages.csv', 'r')
csv_output=open('link.csv', 'w', newline='')
write_score = csv.writer(csv_output)
read_input=csv.reader(csv_input)

for row in read_input:
    try:
        url = row[0]
        write_score.writerow([url,page_speed(API_KEY,url,PS_URL,'mobile')])
    except Exception as e:
        print(e)
csv_input.close()
csv_output.close()










