import os
from urllib2 import urlopen, URLError, HTTPError
import json

INTEL_URL = 'http://home.dishwishy.com/tofuIntel.json'

def dlfile(url):
    # Open the url
    try:
        f = urlopen(url)

        # Open our local file for writing
        intelJSON = json.load(f)
        if u'intelList' in intelJSON:
            intel = intelJSON[u'intelList']
            for i in intel:
                print "%s" % json.dumps(i)

    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


def main():
    # Iterate over image ranges
    url = INTEL_URL
    dlfile(url)

if __name__ == '__main__':
    main()