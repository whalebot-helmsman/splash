#!/usr/bin/env bash
set -e

mkdir -p /tmp/builds
cd /tmp/builds
tar xvfJ "$1" --keep-newer-files --strip-components 1
mkdir -p build
cd build
cmake -G Ninja -DPORT=Qt -DCMAKE_BUILD_TYPE=Release ..
ninja
ninja install
