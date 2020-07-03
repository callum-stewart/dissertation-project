System Requirements:
====================

MUST
----
1. vuln check
   1. output vuln urls to file or to stdout
1. download as much git data as possible
1. rebuild git repo on disk
   1. place .git folder at ./$url/.git
1. take list of target urls from stdin or from file

SHOULD
------
1. be multithreaded
   1. control concurrent threads from commandline
   1. have sensible default
1. configure request options
   1. UA
   1. custom headers
   1. cookies
   1. basic auth creds
1. timeout configuration

COULD
-----
1. proxy options
   1. specifically tor

Dissertation Writeup
====================

- What is git
- How does git work (v. high level)
- Why is leaving .git exposed bad? (impact)
- What can you do with .git after it has been downloaded (exploitation)
- How wide spread is this issue? (bug bounty, alexa top 1M)
- Mitigation strategies
- Discussion of our tool:
  - Requirements
  - Git plumbing
  - How does the tool work
  - How can it be used by Blue Teams to assess vulnerability and impact
  - How can it be used by Red Teams to exploit a target
    - Discussion of recon techniques
  - Additional useful features
