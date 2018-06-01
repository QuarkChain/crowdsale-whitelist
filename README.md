# Crowdsale Whitelist for QuarkChain

`applicants.csv`: applicants' access code and scores, of those who were approved in the KYC process and had a total score >= 60.

`blacklist.txt`: blacklisted participants' access code, identified by our community admins for behaviors like selling code.

`whitelist.py`: Lottery.

The lottery can be run as following:

```python
# Use blockhash at height 525485.
python3 whitelist.py 000000000000000000139dba4d2169f991f9867dd3e996f5e0a86f1ae985308f
```
