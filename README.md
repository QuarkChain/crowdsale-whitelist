# Crowdsale Whitelist for QuarkChain

`applicants.csv`: applicants' access code and scores, of those who were approved in the KYC process and had a total score >= 60.

`blacklist.txt`: blacklisted participants' access code, identified by our community admins for behaviors like selling code.

`whitelist.py`: Lottery.

The lottery can be run as following:

```python
python3 whitelist.py <blockhash>
```
