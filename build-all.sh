#!/bin/sh
#
# Author: Senorsen <senorsen.zhang@gmail.com>
# https://github.com/Senorsen/netease-cloud-music-rpm
#

set -e
set -x

cd $(dirname $0)

DEBFILE_64="netease-cloud-music_1.0.0_amd64_ubuntu16.04.deb"
DEBFILE_32="netease-cloud-music_1.0.0_i386_ubuntu16.04.deb"
VERSION=1.0.0
RELEASE=1

./build.sh $DEBFILE_64 $VERSION $RELEASE x86_64
./build.sh $DEBFILE_32 $VERSION $RELEASE i686
