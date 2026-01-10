#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.22
%define		qtver		5.15.2
%define		kfname		kio

Summary:	Network transparent access to files and data
Name:		kf6-%{kfname}
Version:	6.22.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	0f532d11d33405cd15a393e125a1917e
Patch0:		kio_help-fallback-to-kde4-docs.patch
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel >= %{qtver}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	Qt6Qt5Compat-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	acl-devel
BuildRequires:	cmake >= 3.16
BuildRequires:	heimdal-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kdeframever}
BuildRequires:	kf6-karchive-devel >= %{kdeframever}
BuildRequires:	kf6-kauth-devel >= %{kdeframever}
BuildRequires:	kf6-kbookmarks-devel >= %{kdeframever}
BuildRequires:	kf6-kcompletion-devel >= %{kdeframever}
BuildRequires:	kf6-kconfig-devel >= %{kdeframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kdeframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kdeframever}
BuildRequires:	kf6-kcrash-devel >= %{kdeframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kdeframever}
BuildRequires:	kf6-kded-devel >= %{kdeframever}
BuildRequires:	kf6-kdoctools-devel >= %{kdeframever}
BuildRequires:	kf6-kguiaddons-devel >= %{kdeframever}
BuildRequires:	kf6-ki18n-devel >= %{kdeframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kdeframever}
BuildRequires:	kf6-kitemviews-devel >= %{kdeframever}
BuildRequires:	kf6-kjobwidgets-devel >= %{kdeframever}
BuildRequires:	kf6-knotifications-devel >= %{kdeframever}
BuildRequires:	kf6-kservice-devel >= %{kdeframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kdeframever}
BuildRequires:	kf6-kwallet-devel >= %{kdeframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kdeframever}
BuildRequires:	kf6-kwindowsystem-devel >= %{kdeframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kdeframever}
BuildRequires:	kf6-solid-devel >= %{kdeframever}
BuildRequires:	libblkid-devel
BuildRequires:	libmount-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires:	Qt6Core >= %{qtver}
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6Gui >= %{qtver}
Requires:	Qt6Network >= %{qtver}
Requires:	Qt6Qml >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
Requires:	Qt6Xml >= %{qtver}
Requires:	kf6-dirs
Requires:	kf6-karchive >= %{kdeframever}
Requires:	kf6-kauth >= %{kdeframever}
Requires:	kf6-kbookmarks >= %{kdeframever}
Requires:	kf6-kcompletion >= %{kdeframever}
Requires:	kf6-kconfig >= %{kdeframever}
Requires:	kf6-kconfigwidgets >= %{kdeframever}
Requires:	kf6-kcoreaddons >= %{kdeframever}
Requires:	kf6-kcrash >= %{kdeframever}
Requires:	kf6-kdbusaddons >= %{kdeframever}
Requires:	kf6-kdoctools >= %{kdeframever}
Requires:	kf6-ki18n >= %{kdeframever}
Requires:	kf6-kiconthemes >= %{kdeframever}
Requires:	kf6-kitemviews >= %{kdeframever}
Requires:	kf6-kjobwidgets >= %{kdeframever}
Requires:	kf6-knotifications >= %{kdeframever}
Requires:	kf6-kservice >= %{kdeframever}
Requires:	kf6-ktextwidgets >= %{kdeframever}
Requires:	kf6-kwallet >= %{kdeframever}
Requires:	kf6-kwidgetsaddons >= %{kdeframever}
Requires:	kf6-kwindowsystem >= %{kdeframever}
Requires:	kf6-kxmlgui >= %{kdeframever}
Requires:	kf6-solid >= %{kdeframever}
%requires_eq_to Qt6Core Qt6Core-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file
management.

It supports accessing files locally as well as via HTTP and FTP out of
the box and can be extended by plugins to support other protocols as
well. There is a variety of plugins available, e.g. to support access
via SSH.

The framework can also be used to bridge a native protocol to a
file-based interface. This makes the data accessible in all
applications using the KDE file dialog or any other KIO enabled
infrastructure.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Concurrent-devel >= %{qtver}
Requires:	Qt6DBus-devel >= %{qtver}
Requires:	Qt6Network-devel >= %{qtver}
Requires:	cmake >= 3.16
Requires:	kf6-kbookmarks-devel >= %{kdeframever}
Requires:	kf6-kcompletion-devel >= %{kdeframever}
Requires:	kf6-kconfig-devel >= %{kdeframever}
Requires:	kf6-kcoreaddons-devel >= %{kdeframever}
Requires:	kf6-kitemviews-devel >= %{kdeframever}
Requires:	kf6-kjobwidgets-devel >= %{kdeframever}
Requires:	kf6-kservice-devel >= %{kdeframever}
Requires:	kf6-kwindowsystem-devel >= %{kdeframever}
Requires:	kf6-kxmlgui-devel >= %{kdeframever}
Requires:	kf6-solid-devel >= %{kdeframever}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}
%patch -P0 -p1

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

install -d $RPM_BUILD_ROOT%{qt6dir}/plugins/kf6/{kfileitemaction,kio_dnd}
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr@latin

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,tok}

%find_lang %{kfname}6 --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun


%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/ktelnetservice6
%attr(755,root,root) %{_bindir}/ktrash6
%{_libdir}/libKF6KIOCore.so.*.*
%ghost %{_libdir}/libKF6KIOCore.so.6
%{_libdir}/libKF6KIOFileWidgets.so.*.*
%ghost %{_libdir}/libKF6KIOFileWidgets.so.6
%{_libdir}/libKF6KIOGui.so.*.*
%ghost %{_libdir}/libKF6KIOGui.so.6
%{_libdir}/libKF6KIOWidgets.so.*.*
%ghost %{_libdir}/libKF6KIOWidgets.so.6
%{_libdir}/libkuriikwsfiltereng_private.so
%{_libdir}/qt6/plugins/designer/kio6widgets.so
%{_libdir}/qt6/plugins/kf6/kded/remotenotifier.so
%dir %{_libdir}/qt6/plugins/kf6/kio
%{_libdir}/qt6/plugins/kf6/kio/kio_file.so
%{_libdir}/qt6/plugins/kf6/kio/kio_ftp.so
%{_libdir}/qt6/plugins/kf6/kio/kio_ghelp.so
%{_libdir}/qt6/plugins/kf6/kio/kio_help.so
%{_libdir}/qt6/plugins/kf6/kio/kio_http.so
%{_libdir}/qt6/plugins/kf6/kio/kio_remote.so
%{_libdir}/qt6/plugins/kf6/kio/kio_trash.so
%dir %{_libdir}/qt6/plugins/kf6/kiod
%{_libdir}/qt6/plugins/kf6/kiod/kioexecd.so
%{_libdir}/qt6/plugins/kf6/kiod/kpasswdserver.so
%{_libdir}/qt6/plugins/kf6/kiod/kssld.so
%{_libdir}/qt6/plugins/kf6/urifilters/fixhosturifilter.so
%{_libdir}/qt6/plugins/kf6/urifilters/kshorturifilter.so
%{_libdir}/qt6/plugins/kf6/urifilters/kuriikwsfilter.so
%{_libdir}/qt6/plugins/kf6/urifilters/kurisearchfilter.so
%{_libdir}/qt6/plugins/kf6/urifilters/localdomainurifilter.so
%{_libdir}/qt6/plugins/kf6/kio_dnd/dropintonewfolder.so
%attr(755,root,root) %{_prefix}/libexec/kf6/kiod6
%attr(755,root,root) %{_prefix}/libexec/kf6/kioexec
%attr(755,root,root) %{_prefix}/libexec/kf6/kioworker
%{_desktopdir}/ktelnetservice6.desktop
%{_datadir}/dbus-1/services/org.kde.kiod6.service
%{_datadir}/dbus-1/services/org.kde.kioexecd6.service
%{_datadir}/dbus-1/services/org.kde.kpasswdserver6.service
%{_datadir}/dbus-1/services/org.kde.kssld6.service
%{_datadir}/kdevappwizard/templates/kioworker6.tar.bz2
%dir %{_datadir}/kf6/searchproviders
%{_datadir}/kf6/searchproviders/7digital.desktop
%{_datadir}/kf6/searchproviders/acronym.desktop
%{_datadir}/kf6/searchproviders/amazon.desktop
%{_datadir}/kf6/searchproviders/amazon_mp3.desktop
%{_datadir}/kf6/searchproviders/amg.desktop
%{_datadir}/kf6/searchproviders/archpkg.desktop
%{_datadir}/kf6/searchproviders/archwiki.desktop
%{_datadir}/kf6/searchproviders/backports.desktop
%{_datadir}/kf6/searchproviders/baidu.desktop
%{_datadir}/kf6/searchproviders/beolingus.desktop
%{_datadir}/kf6/searchproviders/bing.desktop
%{_datadir}/kf6/searchproviders/boo.desktop
%{_datadir}/kf6/searchproviders/bug.desktop
%{_datadir}/kf6/searchproviders/call.desktop
%{_datadir}/kf6/searchproviders/cia.desktop
%{_datadir}/kf6/searchproviders/citeseer.desktop
%{_datadir}/kf6/searchproviders/codeberg.desktop
%{_datadir}/kf6/searchproviders/cpan.desktop
%{_datadir}/kf6/searchproviders/cplusplus.desktop
%{_datadir}/kf6/searchproviders/cppreference.desktop
%{_datadir}/kf6/searchproviders/ctan.desktop
%{_datadir}/kf6/searchproviders/ctan_cat.desktop
%{_datadir}/kf6/searchproviders/dbug.desktop
%{_datadir}/kf6/searchproviders/de2en.desktop
%{_datadir}/kf6/searchproviders/de2fr.desktop
%{_datadir}/kf6/searchproviders/deb.desktop
%{_datadir}/kf6/searchproviders/deepl.desktop
%{_datadir}/kf6/searchproviders/dictfr.desktop
%{_datadir}/kf6/searchproviders/docbook.desktop
%{_datadir}/kf6/searchproviders/doi.desktop
%{_datadir}/kf6/searchproviders/duckduckgo.desktop
%{_datadir}/kf6/searchproviders/duckduckgo_info.desktop
%{_datadir}/kf6/searchproviders/duckduckgo_shopping.desktop
%{_datadir}/kf6/searchproviders/ecosia.desktop
%{_datadir}/kf6/searchproviders/en2de.desktop
%{_datadir}/kf6/searchproviders/en2es.desktop
%{_datadir}/kf6/searchproviders/en2fr.desktop
%{_datadir}/kf6/searchproviders/en2it.desktop
%{_datadir}/kf6/searchproviders/es2en.desktop
%{_datadir}/kf6/searchproviders/facebook.desktop
%{_datadir}/kf6/searchproviders/fedora.desktop
%{_datadir}/kf6/searchproviders/feedster.desktop
%{_datadir}/kf6/searchproviders/flatpak.desktop
%{_datadir}/kf6/searchproviders/flickr.desktop
%{_datadir}/kf6/searchproviders/flickrcc.desktop
%{_datadir}/kf6/searchproviders/foldoc.desktop
%{_datadir}/kf6/searchproviders/fr2de.desktop
%{_datadir}/kf6/searchproviders/fr2en.desktop
%{_datadir}/kf6/searchproviders/freecode.desktop
%{_datadir}/kf6/searchproviders/freedb.desktop
%{_datadir}/kf6/searchproviders/fsd.desktop
%{_datadir}/kf6/searchproviders/github.desktop
%{_datadir}/kf6/searchproviders/gitlab.desktop
%{_datadir}/kf6/searchproviders/google.desktop
%{_datadir}/kf6/searchproviders/google_advanced.desktop
%{_datadir}/kf6/searchproviders/google_code.desktop
%{_datadir}/kf6/searchproviders/google_groups.desktop
%{_datadir}/kf6/searchproviders/google_images.desktop
%{_datadir}/kf6/searchproviders/google_lucky.desktop
%{_datadir}/kf6/searchproviders/google_maps.desktop
%{_datadir}/kf6/searchproviders/google_movie.desktop
%{_datadir}/kf6/searchproviders/google_news.desktop
%{_datadir}/kf6/searchproviders/google_shopping.desktop
%{_datadir}/kf6/searchproviders/grec.desktop
%{_datadir}/kf6/searchproviders/hyperdictionary.desktop
%{_datadir}/kf6/searchproviders/hyperdictionary_thesaurus.desktop
%{_datadir}/kf6/searchproviders/identica_groups.desktop
%{_datadir}/kf6/searchproviders/identica_notices.desktop
%{_datadir}/kf6/searchproviders/identica_people.desktop
%{_datadir}/kf6/searchproviders/imdb.desktop
%{_datadir}/kf6/searchproviders/invent.desktop
%{_datadir}/kf6/searchproviders/invent_issues.desktop
%{_datadir}/kf6/searchproviders/invent_mr.desktop
%{_datadir}/kf6/searchproviders/invent_repo.desktop
%{_datadir}/kf6/searchproviders/it2en.desktop
%{_datadir}/kf6/searchproviders/jamendo.desktop
%{_datadir}/kf6/searchproviders/jeeves.desktop
%{_datadir}/kf6/searchproviders/kde.desktop
%{_datadir}/kf6/searchproviders/kde_apps.desktop
%{_datadir}/kf6/searchproviders/kde_forums.desktop
%{_datadir}/kf6/searchproviders/kde_store.desktop
%{_datadir}/kf6/searchproviders/kde_techbase.desktop
%{_datadir}/kf6/searchproviders/kde_userbase.desktop
%{_datadir}/kf6/searchproviders/kreddit.desktop
%{_datadir}/kf6/searchproviders/krita.desktop
%{_datadir}/kf6/searchproviders/learncpp.desktop
%{_datadir}/kf6/searchproviders/leo.desktop
%{_datadir}/kf6/searchproviders/linguee.desktop
%{_datadir}/kf6/searchproviders/magnatune.desktop
%{_datadir}/kf6/searchproviders/metacrawler.desktop
%{_datadir}/kf6/searchproviders/microsoft_cpp.desktop
%{_datadir}/kf6/searchproviders/msdn.desktop
%{_datadir}/kf6/searchproviders/multitran-deru.desktop
%{_datadir}/kf6/searchproviders/multitran-enru.desktop
%{_datadir}/kf6/searchproviders/multitran-esru.desktop
%{_datadir}/kf6/searchproviders/multitran-frru.desktop
%{_datadir}/kf6/searchproviders/multitran-itru.desktop
%{_datadir}/kf6/searchproviders/multitran-nlru.desktop
%{_datadir}/kf6/searchproviders/netcraft.desktop
%{_datadir}/kf6/searchproviders/nl-telephone.desktop
%{_datadir}/kf6/searchproviders/nl-teletekst.desktop
%{_datadir}/kf6/searchproviders/opendesktop.desktop
%{_datadir}/kf6/searchproviders/opensuse.desktop
%{_datadir}/kf6/searchproviders/pgpkeys.desktop
%{_datadir}/kf6/searchproviders/php.desktop
%{_datadir}/kf6/searchproviders/protondb.desktop
%{_datadir}/kf6/searchproviders/pypi.desktop
%{_datadir}/kf6/searchproviders/python.desktop
%{_datadir}/kf6/searchproviders/qt5.desktop
%{_datadir}/kf6/searchproviders/qt6.desktop
%{_datadir}/kf6/searchproviders/qwant.desktop
%{_datadir}/kf6/searchproviders/qwant_images.desktop
%{_datadir}/kf6/searchproviders/qwant_news.desktop
%{_datadir}/kf6/searchproviders/qwant_shopping.desktop
%{_datadir}/kf6/searchproviders/qwant_social.desktop
%{_datadir}/kf6/searchproviders/qwant_videos.desktop
%{_datadir}/kf6/searchproviders/rae.desktop
%{_datadir}/kf6/searchproviders/rag.desktop
%{_datadir}/kf6/searchproviders/reddit.desktop
%{_datadir}/kf6/searchproviders/rfc.desktop
%{_datadir}/kf6/searchproviders/rpmfind.desktop
%{_datadir}/kf6/searchproviders/ruby_application_archive.desktop
%{_datadir}/kf6/searchproviders/rust.desktop
%{_datadir}/kf6/searchproviders/soundcloud.desktop
%{_datadir}/kf6/searchproviders/sourceforge.desktop
%{_datadir}/kf6/searchproviders/technorati.desktop
%{_datadir}/kf6/searchproviders/technoratitags.desktop
%{_datadir}/kf6/searchproviders/thesaurus.desktop
%{_datadir}/kf6/searchproviders/tvtome.desktop
%{_datadir}/kf6/searchproviders/ubuntu.desktop
%{_datadir}/kf6/searchproviders/urbandictionary.desktop
%{_datadir}/kf6/searchproviders/uspto.desktop
%{_datadir}/kf6/searchproviders/vimeo.desktop
%{_datadir}/kf6/searchproviders/voila.desktop
%{_datadir}/kf6/searchproviders/webster.desktop
%{_datadir}/kf6/searchproviders/wikia.desktop
%{_datadir}/kf6/searchproviders/wikipedia.desktop
%{_datadir}/kf6/searchproviders/wiktionary.desktop
%{_datadir}/kf6/searchproviders/wine.desktop
%{_datadir}/kf6/searchproviders/wolfram_alpha.desktop
%{_datadir}/kf6/searchproviders/wordref.desktop
%{_datadir}/kf6/searchproviders/yahoo.desktop
%{_datadir}/kf6/searchproviders/yahoo_image.desktop
%{_datadir}/kf6/searchproviders/yahoo_local.desktop
%{_datadir}/kf6/searchproviders/yahoo_shopping.desktop
%{_datadir}/kf6/searchproviders/yahoo_video.desktop
%{_datadir}/kf6/searchproviders/yandex.desktop
%{_datadir}/kf6/searchproviders/youtube.desktop
%{_datadir}/kf6/searchproviders/caniuse.desktop
%{_datadir}/kf6/searchproviders/dockerhub.desktop
%{_datadir}/kf6/searchproviders/mdn.desktop
%{_datadir}/kf6/searchproviders/nixpkgs.desktop
%{_datadir}/kf6/searchproviders/npm.desktop
%{_datadir}/qlogging-categories6/kio.categories
%{_datadir}/qlogging-categories6/kio.renamecategories
%{_desktopdir}/org.kde.kiod6.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KIO
%{_includedir}/KF6/KIOCore
%{_includedir}/KF6/KIOFileWidgets
%{_includedir}/KF6/KIOWidgets
%{_includedir}/KF6/KIOGui
%{_libdir}/cmake/KF6KIO
%{_libdir}/libKF6KIOCore.so
%{_libdir}/libKF6KIOFileWidgets.so
%{_libdir}/libKF6KIOGui.so
%{_libdir}/libKF6KIOWidgets.so
