import logging
import sys
import argparse
import requests
import concurrent.futures
from urllib.parse import urlparse


def check_vuln(url):
    if url[-1] == '/':
        url = url + '.git/HEAD'
    else:
        url = url + '/.git/HEAD'

    res = requests.get(url)

    if 'refs/heads' not in res.text:
        return False
    else:
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
             description='A tool to find and download exposed .git repos')
    parser.add_argument('--debug', action='store_true')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url')
    group.add_argument('-i', '--input-file', metavar='FILE')
    group.add_argument('--stdin', action='store_true')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    if args.stdin:
        logging.info('standard in')
    elif args.url is not None:
        if check_vuln(args.url):
            logging.info('vulnerable!')
        else:
            logging.info('locked down')
    else:
        logging.debug('file!')
