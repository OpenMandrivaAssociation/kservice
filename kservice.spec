%define major 5
%define libname %mklibname KF5Service %{major}
%define devname %mklibname KF5Service -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kservice
Version:	5.48.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 Service handling framework
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
Patch0: kservice-5.15.0-kde-menu.patch
BuildRequires: flex
BuildRequires: bison
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5DocTools)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: cmake(Qt5Concurrent)
# For test
BuildRequires: appstream
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 Service handling framework.

%package -n %{libname}
Summary: The KDE Frameworks 5 Service handling framework
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 Service handling framework.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5 \
	-DAPPLICATIONS_MENU_NAME:STRING=kde-applications.menu

%build
%ninja -C build

%install
%ninja_install -C build

# We get %{_sysconfdir}/xdg/menus/applications.menu from desktop-common-data for now
# FIXME sync any modifications from kservice there
#rm -rf %{buildroot}%{_sysconfdir}/xdg

%find_lang kservice5

%files -f kservice5.lang
%{_bindir}/*
# Never used (we use /etc/xdg/menus/kde-applications.menu) but let's keep it
%{_sysconfdir}/xdg/kde5/menus/kde-applications.menu
%{_sysconfdir}/xdg/kservice.categories
%{_datadir}/kservicetypes%{major}
%{_mandir}/man8/*
%lang(ca) %{_mandir}/ca/man8/*
%lang(de) %{_mandir}/de/man8/*
%lang(es) %{_mandir}/es/man8/*
%lang(it) %{_mandir}/it/man8/*
%lang(nl) %{_mandir}/nl/man8/*
%lang(pt) %{_mandir}/pt/man8/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/*
%lang(sv) %{_mandir}/sv/man8/*
%lang(uk) %{_mandir}/uk/man8/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
