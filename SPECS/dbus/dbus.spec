Summary:        DBus for systemd
Name:           dbus
Version:        1.11.12
Release:        2%{?dist}
License:        GPLv2+ or AFL
URL:            http://www.freedesktop.org/wiki/Software/dbus
Group:          Applications/File
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://dbus.freedesktop.org/releases/dbus/%{name}-%{version}.tar.gz
%define sha1    dbus=2e2247398abb22115e724b5e955fece2307dddb0

Patch0:         CVE-2020-12049-1.patch
Patch1:         CVE-2020-12049-2.patch

BuildRequires:  expat-devel
BuildRequires:  systemd-devel
BuildRequires:  xz-devel

Requires:       expat
Requires:       systemd
Requires:       xz

%description
The dbus package contains dbus.

%package    devel
Summary:    Header and development files
Requires:   %{name} = %{version}
Requires:  expat-devel
%description    devel
It contains the libraries and header files to create applications

%prep
%autosetup -p1

%build
sh ./configure --prefix=%{_prefix}                 \
            --sysconfdir=%{_sysconfdir}         \
            --localstatedir=%{_var}             \
            --docdir=%{_datadir}/doc/dbus-1.11.12  \
            --enable-libaudit=no --enable-selinux=no \
            --with-console-auth-dir=/run/console

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -vdm755 %{buildroot}%{_lib}

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%{_sysconfdir}/dbus-1
%{_bindir}/*
%{_libdir}/libdbus-1.so.*
%exclude %{_libdir}/sysusers.d
/lib/*
%{_libexecdir}/*
%{_docdir}/*
%{_datadir}/dbus-1

%files  devel
%defattr(-,root,root)
%{_includedir}/*
%{_datadir}/xml/dbus-1
%{_libdir}/cmake/DBus1
%dir %{_libdir}/dbus-1.0
%{_libdir}/dbus-1.0/include/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Sat Jun 27 2020 Prashant S Chauhan <psinghchauha@vmware.com> 1.11.12-2
- Added patches, Fix CVE-2020-12049
* Fri Apr 21 2017 Bo Gan <ganb@vmware.com> 1.11.12-1
- Update to 1.11.12
* Tue Dec 20 2016 Xiaolin Li <xiaolinl@vmware.com> 1.8.8-8
- Move all header files to devel subpackage.
* Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  1.8.8-7
- Change systemd dependency
* Wed Oct 05 2016 ChangLee <changlee@vmware.com> 1.8.8-6
- Modified %check
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.8.8-5
- GA - Bump release of all rpms
* Tue Sep 22 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.8.8-4
- Created devel sub-package
* Thu Jun 25 2015 Sharath George <sharathg@vmware.com> 1.8.8-3
- Remove debug files.
* Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> 1.8.8-2
- Update according to UsrMove.
* Sun Apr 06 2014 Sharath George <sharathg@vmware.com> 1.8.8
- Initial build. First version
