####
Yore
####

* yore.py - I need a script to automatically create a linux machine for
  programming.

############
Requirements
############
* Latest http://www.ubuntu.com/ LTS version
* Python 2.7.x
* git
* non privileged user - usually called ubuntu
    * add user: sudo useradd -m ubuntu

############
Installation
############
* copy/paste the below command if you don't have a local mirror
    * apt-get upgrade && apt-get -y install wget python && wget --no-check-certificate https://raw.github.com/thesheff17/yore/master/yore.py && python yore.py run
* copy/paste the below command if you do have a local mirror
    * apt-get upgrade && apt-get -y install wget python && wget --no-check-certificate https://raw.github.com/thesheff17/yore/master/yore.py && python yore.py apt-mirror && python yore.py run

#################
Technical Details
#################

* apt-get the folling packages: python-pip python-dev build-essential bpython  git-core postgresql postgresql-contrib vim libpq-dev curl wget openssh-server locate
* apt-get non interactive packages: mailutils mutt postfix sendemail mysql-server
* pip installvirtualenv autoenv
* Vim plugins:
    * https://github.com/tpope/vim-pathogen
    * https://github.com/kien/ctrlp.vim.git
    * https://github.com/scrooloose/nerdtree
    * https://github.com/klen/python-mode.git
    * https://github.com/Lokaltog/vim-powerline.gitS

###############
Speed of Script
###############
* Hardware
    * CPU: i7-4750HQ
    * RAM: 16GB RAM
    * HD: Samsung 840 EVO SSD
    * Internet: 50 Mbps
* Without local apt-mirror
    * 127.58 seconds
* With local apt-mirror
    * 81.59 seconds
