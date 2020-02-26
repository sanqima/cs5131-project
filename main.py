#!/usr/bin/python3
#import fetcher/fetcher
#import curator/curator
from curator.curator import Curator

import json
import sys

if __name__ == '__main__':
    curator = Curator()
    result = curator.curate()

    with open('curated_articles.out', 'w') as output:
        output.writelines(json.dumps(result, sort_keys=True, indent=4))

    print(json.dumps(result, sort_keys=True))
    sys.stdout.flush()