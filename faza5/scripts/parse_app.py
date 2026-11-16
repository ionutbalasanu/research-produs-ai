import re,sys,gzip,html,json,glob,os
from datetime import datetime
def txt(s):
    s=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',s);s=re.sub(r'<[^>]+>',' ',s);return re.sub(r'\s+',' ',html.unescape(s))
res={}
for f in glob.glob(sys.argv[1]+'/*.html.gz'):
    h=os.path.basename(f)[:-8]
    raw=gzip.open(f,'rt',errors='ignore').read()
    if len(raw)<20000: res[h]={'error':'gol'};continue
    t=txt(raw)
    m=re.search(r'Launched ([A-Z][a-z]+ \d{1,2}, \d{4})',t)
    la=datetime.strptime(m.group(1),'%B %d, %Y').date().isoformat() if m else None
    mt=re.search(r'<title>(.*?)</title>',raw,re.S); title=html.unescape(mt.group(1)).strip() if mt else ''
    mr=re.search(r'Rating ([\d.]+) \(([\d,]+)(?: Reviews?)?\)',t)
    dev=re.search(r'Developer (.{2,80}?) (?:Install|Log in to install)',t)
    pr=re.search(r'Pricing (.{0,120}?) Rating',t)
    plans=re.findall(r'\$\s?([\d,.]+) ?/ ?(month|year|one-time|monat)',t,re.I)
    cats=re.findall(r'apps.shopify.com/categories/([a-z0-9-]+)',raw)
    devurl=re.search(r'apps.shopify.com/partners/([a-z0-9-]+)',raw)
    intro=re.search(r'<meta name="description" content="([^"]*)"',raw)
    res[h]={'title':title,'launched':la,'rating':float(mr.group(1)) if mr else None,'reviews':int(mr.group(2).replace(',','')) if mr else 0,
            'developer':dev.group(1) if dev else None,'partner':devurl.group(1) if devurl else None,'pricing':pr.group(1) if pr else None,
            'plans':sorted(set(f'{a}/{b}' for a,b in plans)),'desc':html.unescape(intro.group(1)) if intro else ''}
json.dump(res,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
print(len(res),sum(1 for v in res.values() if 'error' in v))
