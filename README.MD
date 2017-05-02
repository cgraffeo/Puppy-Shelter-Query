# Shelter Query
Shelter Query is an application built in python for the Udacity Full Stack Nanodegree.  It focuses on building SQL queries, datatables, and proper code formating.

This project consists of the three following files:
* database_setup.py
* puppy_queries.py
* puppypopulator.py

## How to use
You will need to have Python and Vagrant to run on a VM.
You will also need to clone this repo, you can do so by doing the following:
```
$ git clone https://github.com/cgraffeo/Puppy-Shelter-Query
```
Now you will need to CD into the apropriate files, create a database running database_setup.py:
```
-> vagrant ssh
$ cd /vagrant
$ cd shelters/
$ python  database_setup.py
$ python puppypopulator.py
```
The program has been built to create a databse and populate it for you.

Run the query file:
```
$python puppy_queries.py
```