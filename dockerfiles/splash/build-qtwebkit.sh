#!/usr/bin/env bash
set -e

mkdir -p /tmp/builds
cd /tmp/builds

copied_files=`ls -1 /tmp/builds | wc -l`
if [ "$copied_files" -lt "2" ];
then
    tar xvfJ "$1" --keep-newer-files --strip-components 1
else
    echo "Use already provided sources"
fi

mkdir -p build
cd build
cmake -G Ninja -DPORT=Qt -DCMAKE_BUILD_TYPE=Release ..
ninja
ninja install
