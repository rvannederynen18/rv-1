#!/usr/bin/env python3
"""Build RV-1 from one source.

  python3 build.py                      -> index.html (the website, and the rv-1.html file) + version.json
  python3 build.py --private SEED OUT   -> also writes the private Claude artifact page to OUT,
                                           using SEED (a JSON file kept outside this public repo)

src/rv1.html   the whole app (markup, styles, script) with a /*@SEED@*/ slot
src/head.html  the <head> used by the website and the downloadable file
src/seed.public.json  starter data with no personal details
"""
import json, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
VERSION = datetime.datetime.now().strftime('%Y.%m.%d.%H%M')


def body(seed):
    src = (ROOT / 'src' / 'rv1.html').read_text()
    assert src.count('/*@SEED@*/{}') == 1 and src.count('/*@VERSION@*/') == 1
    src = src.replace('/*@SEED@*/{}', json.dumps(seed, ensure_ascii=False))
    return src.replace('/*@VERSION@*/', VERSION)


def main(argv):
    pub = json.loads((ROOT / 'src' / 'seed.public.json').read_text())
    (ROOT / 'index.html').write_text((ROOT / 'src' / 'head.html').read_text() + body(pub))
    (ROOT / 'version.json').write_text(json.dumps({'version': VERSION}) + '\n')
    print('index.html + version.json', VERSION)
    if len(argv) >= 3 and argv[0] == '--private':
        priv = json.loads(pathlib.Path(argv[1]).read_text())
        pathlib.Path(argv[2]).write_text(body(priv))
        print('private page ->', argv[2])


if __name__ == '__main__':
    main(sys.argv[1:])
