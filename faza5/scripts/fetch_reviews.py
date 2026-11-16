# usage: fetch_reviews.py outdir handle [handle...]  -> outdir/<handle>.json [{id,date,rating,country}]
import re,sys,json,time,html,urllib.request,os
from datetime import datetime
D=r'(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (20\d\d)'
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode('utf-8','ignore')
        except Exception as e: time.sleep(3*(i+1))
    return ''
for h in sys.argv[2:]:
    out=os.path.join(sys.argv[1],h+'.json')
    if os.path.exists(out): continue
    revs={};p=1
    while True:
        s=get(f'https://apps.shopify.com/{h}/reviews?page={p}')
        parts=s.split('data-review-content-id="')[1:]
        new=0
        for seg in parts:
            rid=seg[:seg.find('"')]
            if rid in revs: continue
            t=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',seg[:20000]);t=re.sub(r'<[^>]+>',' ',t);t=re.sub(r'\s+',' ',html.unescape(t))
            m=re.search(D,t); st=re.search(r'aria-label="(\d) out of 5 stars"',seg)
            if not m: continue
            d=datetime.strptime(' '.join(m.groups()),'%B %d %Y').date().isoformat()
            revs[rid]={'id':rid,'date':d,'rating':int(st.group(1)) if st else None}
            new+=1
        if new==0: break
        p+=1; time.sleep(0.7)
    json.dump(sorted(revs.values(),key=lambda r:r['date']),open(out,'w'))
    print(h,len(revs),flush=True)
