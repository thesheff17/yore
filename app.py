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
This program is a simple flask app showing you how to start a web site.
This program will auto detect your eth0 ip address and launch a web server
  on it.
  http://ipAddress:5000/
  http://ipAddress:5000/dan
  http://ipaddress:5000/dan?name=Laura
"""

from flask import Flask, request
import socket
import struct
import fcntl

app = Flask(__name__)


def get_ip_address(ifname):
    """
    This method pulls the private IP of the local machine
    """
    # I did not write this function I give credit to this site
    # for it:
    # hpython-mysqldbttp://code.activestate.com/recipes/439094/
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915,  # SIOCGIFADDR
                                        struct.pack('256s', ifname[:15])
                                        )[20:24])


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/dan", methods=['GET'])
def dan():
    if request.args.get('name'):
        name = request.args.get('name')
    else:
        name = "Dan Sheffner"
    return name + " made this site."

if __name__ == "__main__":
    ipAddress = get_ip_address("eth0")
    app.run(host=ipAddress, debug=True)
