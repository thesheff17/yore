/bin/bash
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

# startTmuxDefault.sh - easy to use tmux session with top

tmux start-server
tmux new-session -d -s monitor -n htop

#splits
tmux split-window -h -p 50
tmux select-pane -t monitor.1
tmux split-window -v -p 50

#commands
tmux send-keys -t monitor.1 'top' C-m
t

#enable mouse
set-option -g mouse-select-pane on

#which pain to select
tmux selectp -t 0
tmux attach-session -t monitor
