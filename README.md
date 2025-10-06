# RPCM | RePo CoMmits

RPCM is a data visualisation script written in Python that creates a bar chart of commits each day inside a given repository.
Please note that repositories with a range of lots of commits will take a very long time to process, or it may exceed the rate limit and return an error.
If there are no commits on certain days within your desired date range, they may not be shown. For example if your range was January 1st 2021 to January 31st 2021, and there was a commit everyday other than the 31st, then the range shown will only be the 1st to the 30th.

# Installation
## Linux
To run rpcm on linux you need to clone this repository, then create a virtual environment (venv) with python to install the required pip packages:

` git clone https://github.com/zfellowes/rpcm.git `

` cd rpcm/ `

To create a venv, run:

` python3 -m venv venv `

Make sure to enable it with:

` source ./venv/bin/activate `

Then to install the requirements, run:

` pip install -r requirements.txt `

After this you will now be able to run:

` python3 rpcm.py `

And it should create the graph for you once it gathers the information.
