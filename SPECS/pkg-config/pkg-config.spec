Summary:	Build tool
Name:		pkg-config
Version:	0.28
Release:	5%{?dist}
License:	GPLv2+
URL:		http://www.freedesktop.org/wiki/Software/pkg-config
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution: Photon
Source0:		http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
%define sha1 pkg-config=71853779b12f958777bffcb8ca6d849b4d3bed46
Patch0:         pkg-config-glib-CVE-2018-16428.patch
Patch1:         pkg-config-glib-CVE-2018-16429.patch
Patch2:		pkg-config-glib-CVE-2020-35457.patch
Patch3:		pkg-config-glib-CVE-2021-27218.patch
%description
Contains a tool for passing the include path and/or library paths
to build tools during the configure and make file execution.

%prep
%setup -q
cd glib  # patches need to apply to internal glib
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
cd ..

%build
%configure \
	--prefix=%{_prefix} \
	--with-internal-glib \
	--disable-host-tool \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
	--disable-silent-rules
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files
%defattr(-,root,root)
%{_bindir}/pkg-config
%{_datadir}/aclocal/pkg.m4
%{_docdir}/pkg-config-0.28/pkg-config-guide.html
%{_mandir}/man1/pkg-config.1.gz
%changelog
*	Mon Dec 13 2021 Mukul Sikka <msikka@vmware.com> 0.28-5
-	Fix internal glib CVE-2021-27218
*	Thu Jan 14 2021 Siju Maliakkal <smaliakkal@vmware.com> 0.28-4
-	Fix internal glib CVE-2020-35457
*	Fri Jan 18 2019 Ajay Kaher <akaher@vmware.com> 0.28-3
-	Fix internal glib for CVE-2018-16428 and CVE-2018-16429
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.28-2
-	GA - Bump release of all rpms
*	Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 0.28-1
-	Initial build. First version
