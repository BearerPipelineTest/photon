Summary:	Libical — an implementation of iCalendar protocols and data formats
Name:		libical
Version:	3.0.8
Release: 	3%{?dist}
License:	MPL-2.0
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://github.com/libical/libical/releases/download/v%{version}/%{name}-%{version}.tar.gz
%define sha1 libical=d2a9cecb9b8d825d5b6989e44b424235a27173a7
BuildRequires:  cmake
BuildRequires:  glib-devel
BuildRequires:  libxml2-devel
Requires:       libxml2

%description
Libical is an Open Source implementation of the iCalendar protocols and
protocol data units. The iCalendar specification describes how calendar
clients can communicate with calendar servers so users can store their
calendar data and arrange meetings with other users.

%package	devel
Summary:	Development files for Libical
Group:		Development/System
Requires:	%{name} = %{version}-%{release}

%description	devel
The libical-devel package contains libraries and header files for developing
applications that use libical.

%prep
%autosetup -p1

%build
mkdir build
cd build
cmake -DENABLE_GTK_DOC=OFF ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%check
make %{?_smp_mflags} -k check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/local/lib64/*.so.*
/usr/local/lib64/cmake/LibIcal/*.cmake
%doc COPYING TODO

%files devel
/usr/local/include/*
/usr/local/lib64/*.so
/usr/local/lib64/*.a
/usr/local/lib64/pkgconfig/*.pc

%changelog
* Thu Nov 18 2021 Nitesh Kumar <kunitesh@vmware.com> 3.0.8-3
- Release bump up to use libxml2 2.9.12-1.
* Wed Jun 30 2021 Tapas Kundu <tkundu@vmware.com> 3.0.8-2
- Need libxml2 in requires
* Wed Jul 08 2020 Gerrit Photon <photon-checkins@vmware.com> 3.0.8-1
- Automatic Version Bump
* Mon Jan 6 2020 Ajay Kaher <akaher@vmware.com> 3.0.7-1
- Initial version
