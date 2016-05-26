#!/bin/sh
#
# Author: Senorsen <senorsen.zhang@gmail.com>
# https://github.com/Senorsen/netease-cloud-music-rpm
#

set -e
set -x

DEBFILENAME="$1"
DEBURL="http://s1.music.126.net/download/pc/${DEBFILENAME}"
VERSION="$2"
RELEASE="$3"
ARCH="$4"
NAME="netease-cloud-music"
SEMIDIR="$NAME-$VERSION"
FULLDIR="$SEMIDIR-$RELEASE.$ARCH"

mkdir -p ~/rpmbuild/SOURCES
cd $(dirname $0)
rm -rf tmp-${ARCH}
mkdir -p tmp-${ARCH}
mkdir -p dist
cd tmp-${ARCH}
cp -rv ../netease-cloud-music.temp.spec ./netease-cloud-music.spec
sed -i "s/\${VERSION}/${VERSION}/g" netease-cloud-music.spec
sed -i "s/\${RELEASE}/${RELEASE}/g" netease-cloud-music.spec
sed -i "s/\${ARCH}/${ARCH}/g" netease-cloud-music.spec
sed -i "s/\${SOURCE}/${SEMIDIR}.tar.gz/g" netease-cloud-music.spec

rm $DEBFILENAME -rf
wget $DEBURL
ar xf $DEBFILENAME
tar xvf data.tar.xz
mkdir -p $SEMIDIR
mv usr $SEMIDIR/
upx $SEMIDIR/usr/lib/netease-cloud-music/netease-cloud-music
mkdir -p $SEMIDIR/usr/bin
rm -rf $SEMIDIR/usr/bin/netease-cloud-music
install -m 755 ../misc/netease-cloud-music $SEMIDIR/usr/bin/netease-cloud-music
mkdir -p $SEMIDIR/etc/pki/rpm-gpg
mkdir -p $SEMIDIR/etc/yum.repos.d
mkdir -p $SEMIDIR/usr/share/senorsen
wget https://dl-http.senorsen.com/pub/package/linux/senorsen.public.key -O senorsen.public.key
wget https://dl-http.senorsen.com/pub/package/linux/senorsen.repo -O senorsen.repo
install -m 644 senorsen.public.key $SEMIDIR/usr/share/senorsen/senorsen.public.key
install -m 644 senorsen.repo $SEMIDIR/usr/share/senorsen/senorsen.repo
wget https://dl-http.senorsen.com/2016/05/lib/libcrypto.so.1.0.0-${ARCH} -O $SEMIDIR/usr/lib/netease-cloud-music/libcrypto.so.1.0.2
tar zcvf ${SEMIDIR}.tar.gz $SEMIDIR
cp ${SEMIDIR}.tar.gz ~/rpmbuild/SOURCES
mkdir -p ~/rpmbuild/SPECS
cp netease-cloud-music.spec ~/rpmbuild/SPECS/
fakeroot rpmbuild -ba netease-cloud-music.spec --target $ARCH
cp ~/rpmbuild/RPMS/$ARCH/${FULLDIR}.rpm ../dist/
