import json,re,os,glob
from datetime import date
from collections import Counter
C=json.load(open('faza5/date/shopify/candidati_grupe.json'))
T={'gpsr':date(2024,12,13),'eaa':date(2025,6,28),'retragere':date(2026,6,19),'garantie':date(2026,9,27)}
EXCL=re.compile(r'(?i:trust badge|trust icon|warranty claim|warranty registration|shipping protection|order editing|customer accounts|profit analytics|warranties|insurance|product files|serial|extended warrant|warranty upsell|warranty management)|\bRMA\b')
def prim(h,v):
    t=v['title']
    if h=='gpsr': return 'gpsr'
    if EXCL.search(t): return None
    if re.search(r'alt text',t,re.I) and not re.search(r'accessib',t,re.I): return None
    if re.search(r'withdraw|widerruf|rétractation|retract|recesso|elállási|revok|revoc',t,re.I): return 'retragere'
    if re.search(r'garan|gewährleist|gewahrleist|guarantee|warranty',t,re.I): return 'garantie'
    if re.search(r'gpsr|product safety',t,re.I): return 'gpsr'
    if re.search(r'accessib|barrierefrei|wcag|\bada\b|\beaa\b|a11y',t,re.I): return 'eaa'
    return None
def ym(d): return d[:7]
def months(t,a,b):
    y,m=t.year,t.month; out=[]
    for k in range(a,b+1):
        mm=m+k; yy=y+(mm-1)//12; mm=(mm-1)%12+1; out.append(f'{yy}-{mm:02d}')
    return out
res={}
for h,v in C.items():
    g=prim(h,v)
    if not g: continue
    f=f'faza5/date/shopify/recenzii/{h}.json'
    revs=json.load(open(f)) if os.path.exists(f) else None
    res.setdefault(g,[]).append((h,v,revs))
out={}
for g,apps in res.items():
    t=T[g]; ms=months(t,-6,6); last=['2026-08','2026-09','2026-10']
    tot=Counter(); rows=[]
    for h,v,revs in sorted(apps,key=lambda x:-x[1]['reviews']):
        if revs is None: continue
        c=Counter(ym(r['date']) for r in revs); tot.update(c)
        la=date.fromisoformat(v['launched']) if v['launched'] else None
        rows.append({'handle':h,'titlu':v['title'][:60],'dezvoltator':v['developer'],'partner':v['partner'],'lansat':v['launched'],
          'zile_fata_de_termen':(la-t).days if la else None,'recenzii':v['reviews'],'descarcate':len(revs),'pret':v['pricing'],'planuri':v['plans'],
          'lunar':{m:c.get(m,0) for m in ms},'aug_oct_2026':sum(c.get(m,0) for m in last)})
    out[g]={'termen':t.isoformat(),'aplicatii_in_grup':len(apps),'cu_recenzii_descarcate':len(rows),
            'total_lunar':{m:tot.get(m,0) for m in ms},'total_aug_oct_2026':sum(tot.get(m,0) for m in last),
            'total_toate':sum(tot.values()),'aplicatii':rows}
json.dump(out,open('faza5/date/shopify/valuri_shopify.json','w'),ensure_ascii=False,indent=1)
for g,o in out.items():
    print('==',g,o['termen'],'apps',o['aplicatii_in_grup'],'cu rec',o['cu_recenzii_descarcate'],'total',o['total_toate'],'aug-oct',o['total_aug_oct_2026'])
    print(' total lunar:',' '.join(f"{k[2:]}:{v}" for k,v in o['total_lunar'].items()))
    for r in o['aplicatii'][:6]: print('  ',r['recenzii'],r['descarcate'],r['lansat'],r['zile_fata_de_termen'],r['handle'],'|',r['dezvoltator'],'|',(r['pret'] or '')[:40],'| aug-oct',r['aug_oct_2026'],'|',' '.join(str(x) for x in r['lunar'].values()))
