%define major 5
%define libname %mklibname KF5Service %{major}
%define devname %mklibname KF5Service -d
%define debug_package %{nil}

Name: kservice
Version: 5.1.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 Service handling framework
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5DocTools)
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
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
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

# We get %{_sysconfdir}/xdg/menus/applications.menu from desktop-common-data for now
# FIXME sync any modifications from kservice there
rm -rf %{buildroot}%{_sysconfdir}/xdg

%find_lang kservice5

%files -f kservice5.lang
%{_bindir}/*
%{_datadir}/kservicetypes%{major}
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
