#!/bin/bash
# usage: fetch_apps.sh handles.txt outdir
while read h; do f="$2/$h.html.gz"; [ -s "$f" ] && continue
  for i in 1 2 3; do curl -s -A 'Mozilla/5.0' "https://apps.shopify.com/$h" | gzip > "$f"; [ $(zcat "$f" | wc -c) -gt 20000 ] && break; sleep 3; done; sleep 0.7
done < "$1"
