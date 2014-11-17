#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# Copyright (c) Dan Sheffner Digitsoft, INC
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


class Yore:
    """
    The Yore class will configure your system
    """

    def __init__(self):
        """
        manages all the software you need on your machine
        """
        update = "apt-get update"
        preFix = "apt-get -y "
        upgrade = preFix + " upgrade"

        packages = preFix + ("install python-pip python-dev build-essential " +
                             "bpython git-core postgresql postgresql-contrib " +
                             "vim libpq-dev curl wget openssh-server locate")
        pip = "pip install virtualenv autoenv"
        self.nonInteractivePackages = ("DEBIAN_FRONTEND=noninteractive " +
                                       preFix + "install mailutils mutt " +
                                       "postfix sendemail mysql-server")

        self.update = update.split()
        self.upgrade = upgrade.split()

        self.packages = packages.split()
        self.pip = pip.split()
        # self.nonInteractivePackages = nonInteractivePackages.split()

        # git repos
        self.vimRepo = []
        self.vimRepo.append("git clone git://github.com/tpope/vim-sensible.git")
        self.vimRepo.append("git clone https://github.com/kien/ctrlp.vim.git")
        self.vimRepo.append("git clone https://github.com/scrooloose/nerdtree")
        self.vimRepo.append("git clone git://github.com/klen/python-mode.git")
        self.vimRepo.append("git clone git://github.com/Lokaltog/" +
                            "vim-powerline.git")

    def checkRoot(self):
        userId = os.getuid()
        if userId is not 0:
            subprocess.call('clear')
            print "You are not root. Please switch to root or use sudo."
            sys.exit(1)

    def clearScreen(self):
        os.system("clear")

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

    def runCommand(self, commandList, useShell=False):
        status = subprocess.call(commandList, shell=useShell)

        if status is not 0:
            print "Command failed: " + str(commandList)
            sys.exit()

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

    def configureVirtualEnv(self):
        pass
        # "virtualenv test"
        # "source test/bin/activate && pip install -r test/requirements.txt"

    def vim(self):
        directory = "/home/" + self.defaultUser + "/"
        if not os.path.isdir(directory + '.vim/'):
            os.makedirs(directory + '.vim/')
            os.makedirs(directory + '.vim/autoload')
            os.makedirs(directory + '.vim/bundle')

            self.runCommand("curl -LSso " + directory +
                            ".vim/autoload/pathogen.vim " +
                            "https://tpo.pe/pathogen.vim", True)

            for each in self.vimRepo:
                self.runCommand("cd " + directory + ".vim/bundle && " +
                                each, True)

            # my .vimrc file
            self.runCommand("curl -LSso " + directory + ".vimrc" +
                            " https://tpo.pe/pathogen.vim", True)

            # Due to this bug I have committed my own version of lint.py
            # https://github.com/klen/python-mode/issues/452
            lintFile = directory + ".vim/bundle/python-mode/pymode/lint.py"
            self.runCommand("rm " + lintFile)
            self.runCommand("curl -LSso " + lintFile +
                            " https://tpo.pe/pathogen.vim", True)

    def fixPermissions(self):
        directory = "/home/" + self.defaultUser + "/"
        self.runCommand(["chown", "-H", "-R", self.defaultUser + ":" +
                         self.defaultUser, directory])

    def buildLocateDB(self):
        self.runCommand("updatedb")

    def clean(self):
        directory = "/home/" + self.defaultUser + "/"
        if os.path.isdir(directory + '.vim'):
            self.runCommand("rm -rf " + directory + '.vim', True)

        if os.path.isfile(directory + ".vimrc"):
            self.runCommand("rm " + directory + '.vimrc', True)


if __name__ == "__main__":
    print "yore.py started..."

    yore = Yore()
    yore.checkRoot()

    try:
        option = sys.argv[1]
    except IndexError:
        print "This is an interactive prompt.  You need to pass it an option"
        print "run        - installs the dev env"
        print "apt-mirror - configures your local mirror"

    if option == "run":
        yore.clearScreen()
        yore.preMenu()
        yore.preMenu2()
        yore.ubuntuUpdates()
        yore.basePackages()
        yore.pipPackages()
        yore.vim()
        yore.fixPermissions()
        yore.buildLocateDB()

    if option == "apt-mirror":
        yore.clearScreen()
        print "Please enter a DNS name or IP address"
        mirror = raw_input("DNS/IP: ")
        yore.setLocalMirror(mirror)

    if option == "clean":
        yore.clearScreen()
        yore.preMenu2()
        yore.clean()

    print "yore.py completed..."
