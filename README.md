System Requirements:
====================

MUST
----
1) vuln check
1.1) output vuln urls to file or to stdout
2) download as much git data as possible
3) rebuild git repo on disk
3.1) place .git folder at ./$url/.git
4) take list of target urls from stdin or from file

SHOULD
------
1) be multithreaded
1.1) control concurrent threads from commandline
1.2) have sensible default
2) configure request options
2.1) UA
2.2) custom headers
2.3) cookies
2.4) basic auth creds
3) timeout configuration

COULD
-----
1) proxy options
1.1) specifically tor

