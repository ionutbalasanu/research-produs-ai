import json,os
from datetime import date
from collections import Counter
T={'gpsr':date(2024,12,13),'eaa':date(2025,6,28),'retragere':date(2026,6,19),'garantie':date(2026,9,27)}
G={'gpsr':['gpsr-for-woocommerce','gpsr-ce-ukca-for-woocommerce','woocommerce-germanized'],
   'eaa':['accessibility-onetap','pojo-accessibility','accessibility-widget','userway-accessibility-widget','wp-accessibility','accessibility-checker','accessibe'],
   'retragere':['eu-order-withdrawal-button-for-woocommerce','eu-withdrawal-compliance','wt-eu-withdrawal-button','wpify-woo','eu-withdrawal-button-for-woocommerce','easy-return-eu-withdrawal-button-for-woocommerce','bitron-right-of-withdrawal','widerrufsbutton','woocommerce-germanized'],
   'garantie':['garanlabs-eu-guarantee-notice-durability-labels','eu-withdrawal-compliance','arthursmith-guarantee-notice-garan-label','eu-warranty-ready','woocommerce-germanized']}
def months(t,a,b):
    out=[]
    for k in range(a,b+1):
        mm=t.month+k; yy=t.year+(mm-1)//12; mm=(mm-1)%12+1; out.append(f'{yy}-{mm:02d}')
    return out
out={}
for g,sl in G.items():
    t=T[g]; ms=months(t,-6,6); rows=[]
    for s in sl:
        dl=json.load(open(f'faza5/date/wp/descarcari/{s}.json'))
        info=json.load(open(f'faza5/date/wp/info_{s}.json'))
        c=Counter()
        for k,v in dl.items(): c[k[:7]]+=int(v)
        first=min(dl); 
        added=info.get('added')
        rows.append({'slug':s,'nume':info.get('name'),'autor':info.get('author'),'adaugat':added,'zile_fata_de_termen':(date.fromisoformat(added)-t).days if added else None,
          'instalari_active':info.get('active_installs'),'prima_zi_in_serie':first,
          'lunar':{m:(c.get(m) if m>=first[:7] else None) for m in ms},'aug_oct_2026':sum(c.get(m,0) for m in ['2026-08','2026-09','2026-10'])})
    out[g]={'termen':t.isoformat(),'pluginuri':rows}
json.dump(out,open('faza5/date/wp/valuri_wp.json','w'),ensure_ascii=False,indent=1)
for g,o in out.items():
    print('==',g,o['termen'])
    for r in o['pluginuri']: print('  ',r['instalari_active'],r['adaugat'],r['zile_fata_de_termen'],r['slug'],'| aug-oct',r['aug_oct_2026'],'|',' '.join('-' if x is None else str(x) for x in r['lunar'].values()))
