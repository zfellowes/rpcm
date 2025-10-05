# RPCM | RePo CoMmits

RPCM is a data visualisation script written in Python that creates a bar chart of commits each day inside a given repository.
Currently, you are able to set a custom start date, but the end date will automatically be set to today, meaning you cannot view a custom range like October 2014 to February 2015. However this will soon be changed in the future.
Repositories with a range of lots of commits will take a very long time to process, this is why there will eventually be custom date selection enabling it to be more optimised.

# Installation
## Linux
To run rpcm on linux you need to clone this repository, then create a virtual environment (venv) with python to install the required pip packages.

To create a venv, change directory to this repo that you cloned, and once inside, run:

` python3 -m venv venv `

Make sure to enable it with:

` source ./venv/bin/activate `

Then to install the requirements, run:

` pip install -r requirements.txt `

After this you will now be able to run:

` python3 rpcm.py `

And it should create the graph for you once it gathers the information.
