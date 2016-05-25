#!/bin/sh
#
# Author: Senorsen <senorsen.zhang@gmail.com>
# https://github.com/Senorsen/netease-cloud-music-rpm
#

set -e
set -x

DEBURL="http://s1.music.126.net/download/pc/netease-cloud-music_0.9.0-1_amd64.deb"
DEBFILENAME="netease-cloud-music_0.9.0-1_amd64.deb"
VERSION=0.9.0
RELEASE=1
ARCH="x86_64"
NAME="netease-cloud-music"
SEMIDIR="$NAME-$VERSION"
FULLDIR="$SEMIDIR-$RELEASE.$ARCH"

mkdir -p ~/rpmbuild/SOURCES
cd $(dirname $0)
mkdir -p tmp
cd tmp
cp -rv ../netease-cloud-music.spec ./
rm $DEBFILENAME -rf
wget $DEBURL
ar xf $DEBFILENAME
tar xvf data.tar.xz
mkdir -p $SEMIDIR
mv usr $SEMIDIR/
tar zcvf ${SEMIDIR}.tar.gz $SEMIDIR
cp ${SEMIDIR}.tar.gz ~/rpmbuild/SOURCES
mkdir -p ~/rpmbuild/SPECS
cp netease-cloud-music.spec ~/rpmbuild/SPECS/
fakeroot rpmbuild -ba netease-cloud-music.spec --target $ARCH
cp ~/rpmbuild/RPMS/$ARCH/${FULLDIR}.rpm ./
