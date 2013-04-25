from datetime import datetime
import urllib2, urllib
import json
import csv

# Open text file with links and make list of URLs
links = [line.strip() for line in open('bitly.txt')]

# Create CSV for results and write headers
f = open('metrics.csv', 'wb')
writer = csv.writer(f)
writer.writerow(["link","time","clicks"]) 

# Call bit.ly API for each link, extract data, and write to CSV

base_url = "https://api-ssl.bitly.com/v3/link/clicks?access_token=ACCESS_TOKEN&rollup=false&unit=hour&timezone=-5&link="

for link in links:
    if "bit.ly" not in link:
        continue
    url = base_url + urllib.quote_plus(link)
    result = urllib2.urlopen(url).read()
    data = json.loads(result)
    for item in data['data']['link_clicks']:
        print "Fetching data for %s" % link
        unix_date = item['dt']
        time = datetime.fromtimestamp(int(unix_date)).strftime('%Y-%m-%d %H:%M:%S')
        clicks = item['clicks']
        writer.writerow([link, time, clicks])

f.close()
