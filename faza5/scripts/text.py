#!/usr/bin/env python3
# usage: text.py file.html [regex] [context]  -> prints plain text or matches with context
import re,sys,html
t=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
t=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',t)
t=re.sub(r'<[^>]+>',' ',t);t=html.unescape(t);t=re.sub(r'\s+',' ',t)
if len(sys.argv)<3: print(t)
else:
    c=int(sys.argv[3]) if len(sys.argv)>3 else 300
    for m in re.finditer(sys.argv[2],t,re.I): print('...'+t[max(0,m.start()-c):m.end()+c]+'...\n---')
