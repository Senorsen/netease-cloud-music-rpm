%global debug_package %{nil}

Name:		netease-cloud-music
Version:	0.9.0
Release:	1
Summary:	Netease Cloud Music (unofficial release, package made by Senorsen)

Group:		Sound and Video
License:	Proprietary
URL:		https://github.com/Senorsen/netease-cloud-music-rpm

Source: netease-cloud-music-0.9.0.tar.gz

AutoReqProv: no
Requires:	alsa-lib >= 1.0.16, atk >= 1.12.4, glibc >= 2.14, cairo >= 1.6.0, libcue, dbus >= 1.2.14, expat >= 2.0.1, fontconfig >= 2.11, freetype >= 2.6, libgcc, gdk-pixbuf2 >= 2.22.0, glib2 >= 2.37.3, gtk2 >= 2.24.0, nspr, nss, pango, qt5-qtbase, qt5-qtmultimedia, qt5-qtx11extras, sqlite, openssl, libstdc++, taglib >= 1.8, libXcursor, libXext, libXfixes, libXi, libXrandr, libXrender, libXScrnSaver, libXtst, zlib >= 1.2.3, gstreamer1-plugins-ugly

%description
Netease Cloud Music (unofficial release, package made by Senorsen <senorsen.zhang@gmail.com>)

%prep
%setup -q


%build
echo $RPM_BUILD


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mv ./* $RPM_BUILD_ROOT/
rm -rf $RPM_BUILD_ROOT/usr/bin/netease-cloud-music
ln -svf ../lib/netease-cloud-music/netease-cloud-music $RPM_BUILD_ROOT/usr/bin/netease-cloud-music

%post
gtk-update-icon-cache /usr/share/icons/hicolor
install -m 644 /usr/share/senorsen/senorsen.public.key /etc/pki/rpm-gpg/RPM-GPG-KEY-SENORSEN
install -m 644 /usr/share/senorsen/senorsen.repo /etc/yum.repos.d/senorsen.repo

%files
%defattr(-,root,root)
/usr/share/senorsen/senorsen.public.key
/usr/share/senorsen/senorsen.repo
/usr/share/icons/hicolor/scalable/apps/netease-cloud-music.svg
/usr/share/doc/netease-cloud-music/README.md.gz
/usr/share/doc/netease-cloud-music/changelog.gz
/usr/share/doc/netease-cloud-music/copyright
/usr/share/applications/netease-cloud-music.desktop
/usr/lib/netease-cloud-music/cef.pak
/usr/lib/netease-cloud-music/cef_100_percent.pak
/usr/lib/netease-cloud-music/natives_blob.bin
/usr/lib/netease-cloud-music/snapshot_blob.bin
/usr/lib/netease-cloud-music/netease-cloud-music
/usr/lib/netease-cloud-music/cef_extensions.pak
/usr/lib/netease-cloud-music/locales/ta.pak
/usr/lib/netease-cloud-music/locales/es.pak
/usr/lib/netease-cloud-music/locales/gu.pak
/usr/lib/netease-cloud-music/locales/th.pak
/usr/lib/netease-cloud-music/locales/sv.pak
/usr/lib/netease-cloud-music/locales/ar.pak
/usr/lib/netease-cloud-music/locales/fa.pak
/usr/lib/netease-cloud-music/locales/nl.pak
/usr/lib/netease-cloud-music/locales/ca.pak
/usr/lib/netease-cloud-music/locales/sk.pak
/usr/lib/netease-cloud-music/locales/en-US.pak
/usr/lib/netease-cloud-music/locales/kn.pak
/usr/lib/netease-cloud-music/locales/tr.pak
/usr/lib/netease-cloud-music/locales/sr.pak
/usr/lib/netease-cloud-music/locales/pt-PT.pak
/usr/lib/netease-cloud-music/locales/es-419.pak
/usr/lib/netease-cloud-music/locales/ml.pak
/usr/lib/netease-cloud-music/locales/sl.pak
/usr/lib/netease-cloud-music/locales/da.pak
/usr/lib/netease-cloud-music/locales/fi.pak
/usr/lib/netease-cloud-music/locales/et.pak
/usr/lib/netease-cloud-music/locales/uk.pak
/usr/lib/netease-cloud-music/locales/fr.pak
/usr/lib/netease-cloud-music/locales/he.pak
/usr/lib/netease-cloud-music/locales/ms.pak
/usr/lib/netease-cloud-music/locales/bn.pak
/usr/lib/netease-cloud-music/locales/ja.pak
/usr/lib/netease-cloud-music/locales/fil.pak
/usr/lib/netease-cloud-music/locales/pt-BR.pak
/usr/lib/netease-cloud-music/locales/ru.pak
/usr/lib/netease-cloud-music/locales/lt.pak
/usr/lib/netease-cloud-music/locales/id.pak
/usr/lib/netease-cloud-music/locales/am.pak
/usr/lib/netease-cloud-music/locales/ko.pak
/usr/lib/netease-cloud-music/locales/nb.pak
/usr/lib/netease-cloud-music/locales/cs.pak
/usr/lib/netease-cloud-music/locales/lv.pak
/usr/lib/netease-cloud-music/locales/it.pak
/usr/lib/netease-cloud-music/locales/te.pak
/usr/lib/netease-cloud-music/locales/hr.pak
/usr/lib/netease-cloud-music/locales/el.pak
/usr/lib/netease-cloud-music/locales/sw.pak
/usr/lib/netease-cloud-music/locales/zh-TW.pak
/usr/lib/netease-cloud-music/locales/mr.pak
/usr/lib/netease-cloud-music/locales/bg.pak
/usr/lib/netease-cloud-music/locales/hu.pak
/usr/lib/netease-cloud-music/locales/de.pak
/usr/lib/netease-cloud-music/locales/zh-CN.pak
/usr/lib/netease-cloud-music/locales/vi.pak
/usr/lib/netease-cloud-music/locales/pl.pak
/usr/lib/netease-cloud-music/locales/ro.pak
/usr/lib/netease-cloud-music/locales/en-GB.pak
/usr/lib/netease-cloud-music/locales/hi.pak
/usr/lib/netease-cloud-music/icudtl.dat
/usr/lib/netease-cloud-music/libcef.so
/usr/lib/netease-cloud-music/chrome-sandbox
/usr/lib/netease-cloud-music/cef_200_percent.pak
/usr/bin/netease-cloud-music
/usr/lib/netease-cloud-music/libcrypto.so.1.0.2
/usr/lib/netease-cloud-music/libssl.so.1.0.2


%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed May 25 2016 Senorsen <senorsen.zhang@gmail.com> - 0.9.0-1
- First rpm package! :-)
