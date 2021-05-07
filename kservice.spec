%define major 5
%define libname %mklibname KF5Service %{major}
%define devname %mklibname KF5Service -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kservice
Version:	5.82.0
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
BuildRequires: kdoctools >= %{version}
# For test
BuildRequires: appstream
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5 \
	-DAPPLICATIONS_MENU_NAME:STRING=kde-applications.menu

%build
if ! %ninja -C build; then
	ninja -d explain -C build
	exit 1
fi

%install
%ninja_install -C build

# We get %{_sysconfdir}/xdg/menus/applications.menu from desktop-common-data for now
# FIXME sync any modifications from kservice there
#rm -rf %{buildroot}%{_sysconfdir}/xdg

%find_lang kservice5 --all-name --with-man

%files -f kservice5.lang
%{_bindir}/*
# Never used (we use /etc/xdg/menus/kde-applications.menu) but let's keep it
%{_sysconfdir}/xdg/kde5/menus/kde-applications.menu
%{_datadir}/qlogging-categories5/kservice.categories
%{_datadir}/qlogging-categories5/kservice.renamecategories
%{_datadir}/kservicetypes%{major}
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
