import sys, re
input = sys.stdin.readline

[main] = re.findall('<main>(.*)</main>', input().rstrip())
splited = re.findall('<div title="(.*?)">(.*?)</div>', main)

for title_name, div in splited:
    print('title :', title_name)
    p = re.findall('<p>(.*?)</p>', div)
    for paragraph in p:
        paragraph = re.sub('(<.*?>)', '', paragraph)
        paragraph = re.sub('\s+', ' ', paragraph.strip())
        print(paragraph)
