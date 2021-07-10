import requests
import json
import urllib.request

import csv
from time import sleep

API_KEY = "AIzaSyAY4NyT3Du5c9i9Vs26mnt6dTJn76tKnVw"
PS_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="

Values=[]




def page_speed(API_KEY, link_url, PS_URL, platform ):

    main_url = PS_URL + link_url + '&key='+API_KEY+'&strategy='+platform
    response = urllib.request.urlopen(main_url)
    result_json = json.loads(response.read())
    fcp = result_json["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]
    lcp = result_json["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]
    cls = result_json["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"]
    for item in fcp,lcp,cls:
        Values.append(item)



    return "done"
    sleep(0.8)


csv_input=open('content-landing-pages.csv', 'r')
csv_output=open('link.csv', 'w', newline='')
write_score = csv.writer(csv_output)
read_input=csv.reader(csv_input)
write_score.writerow(["LINKS","FCP","LCP","CLS"])
ul
for row in read_input:
    try:
        url = row[0]
        page_speed(API_KEY,url,PS_URL,"mobile")
        fcp_1=Values[0]
        lcp_1=Values[1]
        cls_1=Values[2]

        write_score.writerow([url,fcp_1,lcp_1,cls_1])
        print("done " + "for "+ url)
        Values.clear()

    except Exception as e:
        print(e)



csv_input.close()
csv_output.close()





