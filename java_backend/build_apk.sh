#!/usr/bin/env bash

function lazyclone {
    url=$1;
    reponame=$(echo $url | awk -F/ '{print $NF}' | sed -e 's/.git$//');
    git clone $url $reponame;
    git submodule update --init --recursive
    cd $reponame;
}
lazyclone $1
gradle build