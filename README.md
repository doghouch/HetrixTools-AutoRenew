# AutoRenew
Renews free accounts for thirty days by signing in and loading the dashboard (for HetrixTools.com).

# Prerequisites
You only need:

- `python3`
  - the `requests` module
- `unzip`

# Installation
Simply download the [latest release](https://github.com/doghouch/HetrixTools-AutoRenew/releases/download/Main/AutoRenew.zip):

    wget https://github.com/doghouch/HetrixTools-AutoRenew/releases/download/Main/AutoRenew.zip

Unzip it:
	
	unzip AutoRenew.zip

Now, create a CRON job to run (ideally every 20 days) and open the Python file:
	
	nano renew.py

Modify the username/password fields accordingly.

Finally, install the requests module:

    pip3 install requests

... and that's it!

# Warning

This application is **NOT** endorsed by HetrixTools.com or any of their subsidaries. Furthermore, this project isn't actively maintained and should be used at your own risk. 
