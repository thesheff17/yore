####
Yore
####

* yore.py - I need a script to automatically create a linux machine for
  programming. apt-get, pip, db, and vim plugins.

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
    * apt-get update && apt-get -y upgrade && apt-get -y install wget python && wget --no-check-certificate https://raw.github.com/thesheff17/yore/master/yore.py && python yore.py run
* copy/paste the below command if you do have a local mirror
    * apt-get update && apt-get -y upgrade && apt-get -y install wget python && wget --no-check-certificate https://raw.github.com/thesheff17/yore/master/yore.py && python yore.py apt-mirror && python yore.py run

#####
Usage
#####
* set a ubuntu password if you don't already have one set
  * passwd ubuntu
* log out and log back in to make sure the vim settings take effect
* create a new virtualenv
    * mkvirtualenv test
* install the packages
    * pip install -r requirements.txt
* start flask app
    * python app.py
* used after a virtualenv is already created
    * workon test


#################
Technical Details
#################

* Vim plugins:
    * https://github.com/tpope/vim-pathogen
    * https://github.com/kien/ctrlp.vim.git
    * https://github.com/scrooloose/nerdtree
    * https://github.com/klen/python-mode.git
    * https://github.com/Lokaltog/vim-powerline.gitS
