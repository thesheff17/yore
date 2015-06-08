#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright (c) Dan Sheffner Digital Imaging Software Solutions, INC
# Email: Dan@Sheffner.com
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""
yore.py - This program will create a development env from start to finish
          on a ubuntu LTS server
"""

import os
import sys
import subprocess
import shutil
import timeit


class Yore:
    """
    The Yore class will configure your system
    """

    def __init__(self):
        """
        manages all the software you need on your machine
        """
        self.update = "apt-get update"
        preFix = "apt-get -y "
        self.upgrade = preFix + "upgrade"

        self.packages = preFix + ("install python-pip python-dev " +
                                  "build-essential git-core postgresql " +
                                  "postgresql-contrib vim libpq-dev curl wget "
                                  "ssh locate postgresql-server-dev-9.3 " +
                                  "libssl-dev libffi-dev tmux htop")

        self.pip = "pip install virtualenv autoenv virtualenvwrapper"

        self.nonInteractivePackages = ("DEBIAN_FRONTEND=noninteractive " +
                                       preFix + "install mailutils mutt " +
                                       "postfix sendemail mysql-server " +
                                       "postgresql-9.3")

        # git repos
        self.vimRepo = []
        self.vimRepo.append("git clone https://github.com/tpope/" +
                            "vim-sensible.git")
        self.vimRepo.append("git clone https://github.com/kien/ctrlp.vim.git")
        self.vimRepo.append("git clone https://github.com/scrooloose/nerdtree")
        self.vimRepo.append("git clone https://github.com/klen/python-mode.git")
        self.vimRepo.append("git clone https://github.com/Lokaltog/" +
                            "vim-powerline.git")

    def checkRoot(self):
        userId = os.getuid()
        if userId is not 0:
            subprocess.call('clear')
            print "You are not root. Please switch to root or use sudo."
            sys.exit(1)

    def runCommand(self, commandString, useShell=False):

        if useShell:
            status = subprocess.call(commandString, shell=useShell)
        else:
            commandList = commandString.split(" ")
            status = subprocess.call(commandList, shell=useShell)

        if status is not 0:
            print "Command failed: " + commandString
            sys.exit()

    def clearScreen(self):
        self.runCommand("clear")

    def preMenu(self):
        self.clearScreen()
        print '################################'
        print "# Welcome to the yore.py menu. #"
        print "# Created by Dan Sheffner      #"
        print "################################"
        print ""
        print "This program comes with no warranty and you should ALWAYS "
        print "read the source code of these programs before running them."
        print ""
        userInput = raw_input("Would you like to continue? Answer YES " +
                              "Case sesitive. ")
        if userInput == 'YES':
            pass
        else:
            print 'Exiting Yore.py script...'
            sys.exit(1)

    def preMenu2(self):
        self.clearScreen()
        print "Please enter a non privileged user name usually ubuntu"
        print ""
        self.defaultUser = raw_input("Enter a username: ")
        self.directory = "/home/" + self.defaultUser + "/"

    def setLocalMirror(self, ip):
        with open('/etc/apt/sources.list', 'w') as fileObj:
            fileObj.write("deb http://" + ip + "/ubuntu trusty main restricted "
                          "universe multiverse\n")
            fileObj.write("deb http://" + ip + "/ubuntu trusty-updates main "
                          "restricted universe multiverse\n")
            fileObj.write("deb http://" + ip + "/ubuntu trusty-security main "
                          "restricted universe multiverse\n")

    def ubuntuUpdates(self):
        self.runCommand(self.update)
        self.runCommand(self.upgrade)

    def basePackages(self):
        self.runCommand(self.packages)
        self.runCommand(self.nonInteractivePackages, True)

    def pipPackages(self):
        self.runCommand(self.pip)

    def vim(self):
        if not os.path.isdir(self.directory + '.vim/'):
            os.makedirs(self.directory + '.vim/')
            os.makedirs(self.directory + '.vim/autoload')
            os.makedirs(self.directory + '.vim/bundle')
            os.makedirs(self.directory + '.vim/colors')

            self.runCommand("curl -LSso " + self.directory +
                            ".vim/autoload/pathogen.vim " +
                            "https://tpo.pe/pathogen.vim")

            for each in self.vimRepo:
                self.runCommand("cd " + self.directory + ".vim/bundle && " +
                                each, True)

            # my .vimrc file
            self.runCommand("curl -LSso " + self.directory + ".vimrc" +
                            " https://raw.githubusercontent.com/thesheff17/" +
                            "yore/master/vimrc")

            # Due to this bug I have committed my own version of lint.py
            # https://github.com/klen/python-mode/issues/452
            lintFile = self.directory + ".vim/bundle/python-mode/pymode/lint.py"
            self.runCommand("rm " + lintFile)
            self.runCommand("curl -LSso " + lintFile +
                            " https://raw.githubusercontent.com/thesheff17/"
                            "yore/master/lint.py")

            # colors file
            self.runCommand("curl -LSso " + self.directory +
                            ".vim/colors/wombat256mod.vim" +
                            " https://raw.githubusercontent.com/thesheff17/" +
                            "yore/master/wombat256mod.vim")

    def getFiles(self):
        self.runCommand("curl -LSso " + self.directory +
                        "requirements.txt " +
                        "https://raw.githubusercontent.com/thesheff17/" +
                        "yore/master/requirementsSample.txt")

        self.runCommand("curl -LSso " + self.directory +
                        "app.py " +
                        "https://raw.githubusercontent.com/thesheff17/" +
                        "yore/master/app.py")

        self.runCommand("curl -LSso " + self.directory +
                        "app.py " +
                        "https://raw.githubusercontent.com/thesheff17/" +
                        "yore/master/startTmuxDefault.sh")

    def virtualEnvConfig(self):
        with open(self.directory + ".bashrc", 'w') as file:
                file.write("source /usr/local/bin/virtualenvwrapper.sh\n")

    def fixPermissions(self):
        self.runCommand("chown -H -R " + self.defaultUser + ":" +
                        self.defaultUser + " " + self.directory)

    def buildLocateDB(self):
        self.runCommand("updatedb")

    def mongodb(self):
        pass
        # There is some bug here with it being a lxc/lxd container :(
        # invoke-rc.d: initscript mongodb, action "start" failed.
        # self.runCommand("apt-key adv --keyserver " +
        #                "hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10")

        # with open('/etc/apt/sources.list.d/mongodb-org-3.0.list', 'w+')
        # as file:
        #    file.write('deb http://repo.mongodb.org/apt/ubuntu ' +
        #               'trusty/mongodb-org/3.0 multiverse')

        # self.runCommand(self.update)
        # self.runCommand("export LANGUAGE=en_US.UTF-8 && " +
        #                "export LANG=en_US.UTF-8 && " +
        #                "export LC_ALL=en_US.UTF-8 && " +
        #                "locale-gen en_US.UTF-8 && " +
        #                "dpkg-reconfigure locales && " +
        #                "apt-get install -y mongodb-org", True)

    def clean(self):
        if os.path.isdir(self.directory + '.vim'):
            shutil.rmtree(self.directory + '.vim')

        if os.path.isdir(self.directory + ".virtualenvs"):
            shutil.rmtree(self.directory + ".virtualenvs")

        if os.path.isfile(self.directory + "requirements.txt"):
            os.remove(self.directory + "requirements.txt")

        if os.path.isfile(self.directory + ".vimrc"):
            os.remove(self.directory + ".vimrc")

        if os.path.isfile(self.directory + "app.py"):
            os.remove(self.directory + "app.py")


if __name__ == "__main__":
    print "yore.py started..."
    start = timeit.default_timer()

    yore = Yore()
    yore.checkRoot()

    try:
        option = sys.argv[1]
    except IndexError:
        print "This is an interactive prompt.  You need to pass it an option"
        print "run        - installs the dev env"
        print "apt-mirror - configures your local mirror"
        print "clean      - cleans up the old files"

    if option == "run":
        yore.preMenu()
        yore.preMenu2()
        yore.ubuntuUpdates()
        yore.basePackages()
        yore.pipPackages()
        yore.vim()
        yore.fixPermissions()
        yore.buildLocateDB()
        yore.getFiles()
        yore.virtualEnvConfig()
        yore.mongodb()

    if option == "apt-mirror":
        yore.preMenu()
        print "Please enter a DNS name or IP address"
        mirror = raw_input("DNS/IP: ")
        yore.setLocalMirror(mirror)

    if option == "clean":
        yore.preMenu2()
        yore.clean()

    stop = timeit.default_timer()
    print stop - start
    print "yore.py completed..."
