#!/bin/sh
#
# Author: Senorsen <senorsen.zhang@gmail.com>
# https://github.com/Senorsen/netease-cloud-music-rpm
#

set -e
set -x

cd $(dirname $0)

DEBFILE_64="netease-cloud-music_0.9.0_amd64.deb"
DEBFILE_32="netease-cloud-music_0.9.0_i386.deb"
VERSION=0.9.0
RELEASE=3

./build.sh $DEBFILE_64 $VERSION $RELEASE x86_64
./build.sh $DEBFILE_32 $VERSION $RELEASE i686
