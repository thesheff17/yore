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
      * install: sudo apt-get update && sudo apt-get -y python
    * git 
        * install: sudo apt-get update && sudo apt-get -y git-core
    * non privileged user - usually called ubuntu 
        * add user: sudo useradd -m ubuntu

############
Installation
############
    * git clone https://github.com/thesheff17/yore
    * python yore.py apt-mirror - If you have your own local ubuntu mirror
    * python yore.py run        - configures your instances for developement
    * python yore.py clean      - cleans up so you can run the script again

#################
Technical Details
#################

* apt-get the folling packages: python-pip python-dev build-essential bpython
  git-core postgresql postgresql-contrib vim libpq-dev curl wget openssh-server
  locate
* apt-get non interactive packages: mailutils mutt postfix sendemail
  mysql-server
* pip installing virtualenv autoenv
* Vim plugins:
    * https://github.com/tpope/vim-pathogen
    * https://github.com/kien/ctrlp.vim.git
    * https://github.com/scrooloose/nerdtree
    * git://github.com/klen/python-mode.git  
    * git://github.com/Lokaltog/vim-powerline.git
