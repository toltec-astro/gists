#!/bin/bash

if [[ ! $1 ]]; then
    echo Usage: js9_config.sh rootdir
    exit 0
fi
root=$1
prefix=${root}/js9
webdir=${root}/htdocs/js9
cgidir=${root}/cgi-bin/js9
cgiurl=./cgi-bin/js9
cgixpath=${prefix}/bin
cfitsio=/usr
funtools=/usr

./configure \
    --prefix=${webdir} \
    --with-helper=nodejs \
    --with-webdir=${webdir} \
    --with-cgidir=${cgidir} \
    --with-cgiurl=${cgiurl} \
    --with-cgixpath=${cgixpath} \
    --with-funtools=${funtools} \
    --with-cfitsio=${cfitsio}
