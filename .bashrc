#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
export TERM=xterm-256color
export EDITOR="nvim"

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

[ -f ~/.fzf.bash ] && source ~/.fzf.bash
. "$HOME/.cargo/env"
alias config='/usr/bin/git --git-dir=/home/santorar/.cfg/ --work-tree=/home/santorar'
