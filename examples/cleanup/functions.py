import pipulate as gs
from itertools import cycle
import requests
import re
import time

use_proxies = False
print("Use proxies: %s" % use_proxies)


if use_proxies:
    proxy_list = list()
    bad_blocks = list()
    with open('goodproxies.txt') as proxies:
        for line in proxies:
            proxy_list.append(line[:-1])
    with open('badproxies.txt') as proxies:
        for line in proxies:
            bad_blocks.append(line[:-1])
    proxy_cycler = cycle(proxy_list)
    

common_agents = list()
with open('useragents.txt') as agents:
    for line in agents:
        common_agents.append(line[:-1])
agent_cycler = cycle(common_agents)


def fu():
    return 'bar'


def serp(row):
    keyword = row[0]
    
    from urllib.parse import quote_plus
    global use_proxies, proxy_cycler, bad_blocks, agent_cycler
        
    rpp=20
    print("Keyword: %s" % keyword)
    search_url = 'https://www.google.com/search?num=%s&q=%s' % (rpp, quote_plus(keyword))
    pattern = re.compile('<h3 class="r"><a href="(http.*?)"')
    landing_pages = []
    proxied_retries = 3
    unproxied_retries = 1
    sleep_delay = 2
    try_proxies = 1000
    
    agent = next(agent_cycler)
    user_agent = {'User-agent': agent}
    # The preferred path if you have anonymous web proxies.
    # The light that burns twice as bright burns half as long.
    if use_proxies:
        for x in range(10):
            ip = next(proxy_cycler)
            if ip not in bad_blocks:
                break
            print("Couldn't find good proxy. Clear cache and try later.")
            raise SystemExit()
        block = '.'.join(ip.split('.')[:3])
        p = ip.rfind('.')
        hide = ('*' * len(ip))[:p]+ip[p:]
        proxy = {'http': 'http://'+ip, 'https': 'https://'+ip}
        print('Using proxy: %s' % hide)
        for i in range(proxied_retries):
            response = requests.get(search_url, proxies=proxy, headers=user_agent)
            landing_pages = re.findall(pattern, response.text)
            if len(landing_pages) == 0:
                ip = next(proxy_cycler)
                time.sleep.wait(sleep_delay)
                break
    else:
        for i in range(unproxied_retries):
            #try:
            response = requests.get(search_url, headers=user_agent)
            landing_pages = re.findall(pattern, response.text)
            break
            #except:
            #    agent = next(agent_cycler)
            #    user_agent = {'User-agent': agent}
        
    return landing_pages


def ga_url(gaid, start, end, path):
    """Return Google Analytics metrics for a URL."""
    #API Not adapted to Pipulate yet
    
    # OMG! How do I set all these parameters? Explore at:
    # https://ga-dev-tools.appspot.com/query-explorer/
    path = path.replace(',', r'\,')
    metrics = ['users', 
               'newUsers', 
               'sessions', 
               'bounceRate',
               'pageviewsPerSession', 
               'avgSessionDuration']
    metrics = ''.join(['ga:%s,' % x for x in metrics])[:-1]
    ga_request = gs.ga().data().ga().get(
        ids='ga:'+gaid,
        start_date=start,
        end_date=end,
        metrics=metrics,
        dimensions='ga:pagePath',
        sort='-ga:users',
        filters='ga:pagePath=='+path,
        segment='sessions::condition::ga:medium==organic',
        max_results=1
    )
    ga_response = ga_request.execute()
    return_value = []
    if 'rows' in ga_response:
        raw_rows = ga_response['rows'][0]
        return_value = raw_rows
    return return_value


def gsc_keyword(prop, start, end, query):
    """Return position, clicks & impressions from GSC for keyword."""
    #API Not adapted to Pipulate yet
    
    request = {
      "startDate": start,
      "endDate": end,
      "dimensions": [
        "query"
      ],
      "dimensionFilterGroups": [
        {
          "filters": [
            {
              "operator": "equals",
              "expression": query,
              "dimension": "query"
            }
          ]
        }
      ]
    }
    data = gs.gsc().searchanalytics().query(siteUrl='https://www.pcmag.com', body=request).execute()
    val = []
    if 'rows' in data:
        r = data['rows'][0]
        val = [start, end] + [r['keys'][0]] + [
            r['position']] + [r['clicks']] + [r['impressions']] + [r['ctr']]
    return val


def gsc_url(prop, start, end, url):
    """Return position, clicks & impressions from GSC for URL."""
    #API Not adapted to Pipulate yet

    request = {
      "startDate": start,
      "endDate": end,
      "dimensions": [
        "page"
      ],
      "dimensionFilterGroups": [
        {
          "filters": [
            {
              "operator": "equals",
              "expression": url,
              "dimension": "page"
            }
          ]
        }
      ]
    }
    data = gs.gsc().searchanalytics().query(siteUrl='https://www.pcmag.com', body=request).execute()
    val = []
    if 'rows' in data:
        r = data['rows'][0]
        val = [start, end] + [r['keys'][0]] + [
            r['position']] + [r['clicks']] + [r['impressions']] + [r['ctr']]
    return val


def gsc_url_keyword(prop, start, end, query, url):
    """Return position, clicks & impressions from GSC for keyword for URL."""
    #API Not adapted to Pipulate yet

    request = {
      "startDate": start,
      "endDate": end,
      "dimensions": [
        "query",
        "page"
      ],
      "dimensionFilterGroups": [
        {
          "filters": [
            {
              "operator": "equals",
              "expression": url,
              "dimension": "page"
            },
            {
              "operator": "equals",
              "expression": query,
              "dimension": "query"
            }
          ]
        }
      ]
    }
    data = gs.gsc().searchanalytics().query(siteUrl=prop, body=request).execute()
    val = []
    if 'rows' in data:
        r = data['rows'][0]
        val = [start] + [r['keys'][0]] + [r['keys'][1]] + [
            r['position']] + [r['clicks']] + [r['impressions']] + [r['ctr']]
    return val


def extract_pos(row):
    match_pattern = row[2]
    stuffed_serp = row[1]
    return_me = '--'
    alist = eval(stuffed_serp)
    for i, item in enumerate(alist):
        if item.find(match_pattern) != -1:
            return_me = i + 1
            break
    return return_me


def extract_url(row):
    match_pattern = row[2]
    #match_pattern = 'string literal'
    stuffed_serp = row[1]
    return_me = '--'
    alist = eval(stuffed_serp)
    for i, item in enumerate(alist):
        if item.find(match_pattern) != -1:
            return_me = item
            break
    return return_me