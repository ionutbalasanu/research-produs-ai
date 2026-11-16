#!/bin/bash
# usage: cellar.sh CELEX outfile
for acc in "application/xhtml+xml" "text/html" ; do
curl -s -L -A 'Mozilla/5.0' -H "Accept: $acc" -H 'Accept-Language: eng' "http://publications.europa.eu/resource/celex/$1" -o "$2"
if ! grep -q "None of the requests" "$2" && [ $(stat -c%s "$2") -gt 2000 ]; then echo "$1 ok $acc $(stat -c%s $2)"; exit 0; fi
done
echo "$1 FAIL"; head -c 300 "$2"
