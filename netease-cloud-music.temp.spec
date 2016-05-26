%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:		netease-cloud-music
Version:	${VERSION}
Release:	${RELEASE}
Summary:	Netease Cloud Music (unofficial release, package made by Senorsen)

Group:		Sound and Video
License:	Proprietary
URL:		https://github.com/Senorsen/netease-cloud-music-rpm

Source:	   ${SOURCE}

AutoReqProv:	no

Provides:	netease-cloud-music = ${VERSION}-${RELEASE}
Provides:	application(netease-cloud-music.desktop)

Requires:	alsa-lib%{?_isa} >= 1.0.16
Requires:	atk%{?_isa} >= 1.12.4
Requires:	glibc%{?_isa} >= 2.14
Requires:	cairo%{?_isa} >= 1.6.0
Requires:	libcue%{?_isa}
Requires:	dbus%{?_isa} >= 1.2.14
Requires:	expat%{?_isa} >= 2.0.1
Requires:	fontconfig%{?_isa} >= 2.11
Requires:	freetype%{?_isa} >= 2.6
Requires:	libgcc%{?_isa}
Requires:	gdk-pixbuf2%{?_isa} >= 2.22.0
Requires:	glib2%{?_isa} >= 2.37.3
Requires:	gtk2%{?_isa} >= 2.24.0
Requires:	nspr%{?_isa}
Requires:	nss%{?_isa}
Requires:	pango%{?_isa}
Requires:	qt5-qtbase%{?_isa}
Requires:	qt5-qtmultimedia%{?_isa}
Requires:	qt5-qtx11extras%{?_isa}
Requires:	sqlite%{?_isa}
Requires:	libstdc++%{?_isa}
Requires:	taglib%{?_isa} >= 1.8
Requires:	libXcursor%{?_isa}
Requires:	libXext%{?_isa}
Requires:	libXfixes%{?_isa}
Requires:	libXi%{?_isa}
Requires:	libXrandr%{?_isa}
Requires:	libXrender%{?_isa}
Requires:	libXScrnSaver%{?_isa}
Requires:	libXtst%{?_isa}
Requires:	zlib%{?_isa} >= 1.2.3
Requires:	gstreamer1-plugins-ugly%{?_isa}


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
/usr/lib/netease-cloud-music/libcrypto.so.1.0.2
/usr/bin/netease-cloud-music


%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 26 2016 Senorsen <senorsen.zhang@gmail.com> - 0.9.0-3
- Fix memory leak (according to issue #1, Xu Shaohua's fix)
* Wed May 25 2016 Senorsen <senorsen.zhang@gmail.com> - 0.9.0-1
- First rpm package! :-)
