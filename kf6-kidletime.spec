%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6IdleTime
%define devname %mklibname KF6IdleTime -d
#define git 20240217

Name: kf6-kidletime
Version: 6.20.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kidletime/-/archive/master/kidletime-master.tar.bz2#/kidletime-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kidletime-%{version}.tar.xz
%endif
Summary: Reporting of idle time of user and system
URL: https://invent.kde.org/frameworks/kidletime
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xscrnsaver)
Requires: %{libname} = %{EVRD}

%description
Reporting of idle time of user and system

%package -n %{libname}
Summary: Reporting of idle time of user and system
Group: System/Libraries
Requires: %{name} = %{EVRD}
Requires: (%{name}-x11 if x11-server-xorg)
Requires: (%{name}-wayland if plasma6-kwin-wayland)

%description -n %{libname}
Reporting of idle time of user and system

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Reporting of idle time of user and system

%package wayland
Summary: Wayland windowing system support for KIdleTime
Group: System/Libraries

%description wayland
Wayland windowing system support for KIdleTime

%package x11
Summary: X11 windowing system support for KIdleTime
Group: System/Libraries

%description x11
X11 windowing system support for KIdleTime

%prep
%autosetup -p1 -n kidletime-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/kidletime.*
%dir %{_qtdir}/plugins/kf6/org.kde.kidletime.platforms

%files wayland
%{_qtdir}/plugins/kf6/org.kde.kidletime.platforms/KF6IdleTimeWaylandPlugin.so

%files x11
%{_qtdir}/plugins/kf6/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin0.so
%{_qtdir}/plugins/kf6/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin1.so

%files -n %{devname}
%{_includedir}/KF6/KIdleTime
%{_libdir}/cmake/KF6IdleTime

%files -n %{libname}
%{_libdir}/libKF6IdleTime.so*
