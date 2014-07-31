# coding=utf8
import requests
from BeautifulSoup import BeautifulSoup
import time
import json

roots = {}
left = 0

# 得到词根列表 page 1-11
for page in range(1, 11):
    print 'get page', page
    while True:
        try:
            ret = requests.get('http://cgdict.com/cigen/list/page-%s' % page,
                               headers={'user-agent': 'Mozilla/5.0'}, timeout=3).content
            break
        except requests.Timeout:
            print 'Timeout'
        except:
            pass
    bs = BeautifulSoup(ret)
    h2 = bs.find('h2', {'class': 'clh2'})
    print 'done', page, 'get', len(h2), 'roots'
    left += len(h2)
    for i in h2.findAll('a'):
        roots[i['href'].replace('http://cgdict.com/cigen/word/w-', '')] = ''


def text_process(text):
    bs = BeautifulSoup(text)
    meaning = [i.text for i in bs.findAll('strong')]
    examples = []

    for i in bs.find('div', {'class': 'wdef'}).findAll('li'):
        try:
            examples.append(i.find('a').text)
        except:
            pass

    return {'meaning': meaning, 'examples': examples}

print 'start to download entries'
for k in roots:
    print 'current root:[%s]' % k
    while True:
        try:
            content = requests.get('http://cgdict.com/cigen/word/w-' + k,
                                   headers={'user-agent': 'Mozilla/5.0'}, timeout=3).content
            break
        except requests.Timeout:
            print 'Timeout'
        except:
            pass
    roots[k] = text_process(content)
    print 'left', left
    left -= 1
    time.sleep(0.5)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open('roots_formated_output.txt', 'w') as f:
    for k, v in sorted(roots.items()):
        f.write('%s\t%s\n\t\t%s' % (
            k, '||'.join(v['meaning']), '\n\t\t'.join(list(set(v['examples'])))) + '\n')

with open('roots.json', 'w') as f:
    f.write(json.dumps(roots))
