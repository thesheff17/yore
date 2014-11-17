####
Yore
####

* yore.py - I need a script to automatically create a linux machine for
  programming.
  * Why is this program named yore?  A long time ago when you first started
    with computers the commands just worked.  Now computers accomplish so much
    allot is missing.  This program attempts to bridge that gap.

############
Requirements
############
    * Latest http://www.ubuntu.com/ LTS version
    * Python 2.7.x command to install - sudo apt-get update && sudo apt-get -y python
    * git - command to install: sudo apt-get update && sudo apt-get -y git-core
    * non privileged user - usually called ubuntu 

############
Installation
############
    * git clone https://github.com/thesheff17/yore
    * cd yore
    * python yore.py apt-mirror - If you have your own local ubuntu mirror
    * python yore.py run        - configures your instances for developement

#################
Technical Details
#################

* apt-get the folling packages: python-pip python-dev build-essential bpython
  git-core postgresql postgresql-contrib vim libpq-dev
* apt-get non interactive packages: mailutils mutt postfix sendemail
  mysql-server
* pip installing virtualenv autoenv
* Vim plugins:
  * https://github.com/tpope/vim-pathogen
l
  
 
