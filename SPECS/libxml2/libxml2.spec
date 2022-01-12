%{!?python2_sitelib: %define python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        Libxml2
Name:           libxml2
Version:        2.9.11
Release:        2%{?dist}
License:        MIT
URL:            http://xmlsoft.org/
Group:          System Environment/General Libraries
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://xmlsoft.org/sources/%{name}-%{version}.tar.gz
%define sha1    libxml2=7902b9cc7a549c09f8fb227fc4aa1d0275d4282c

Patch0:         0001-Work-around-lxml-API.patch

BuildRequires:  python3-devel
BuildRequires:  python2-devel
BuildRequires:  python2-libs

Provides:       pkgconfig(libxml-2.0)

%description
The libxml2 package contains libraries and utilities used for parsing XML files.

%package python
Summary:        The libxml2 python module
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python2
Requires:       python2-libs

%description python
The libxml2 python module

%package -n     python3-libxml2
Summary:        Python 3 bindings for libxml2.
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       python3

%description -n python3-libxml2
Python3 libxml2.

%package devel
Summary:    Libraries and header files for libxml
Requires: %{name} = %{version}

%description devel
Static libraries and header files for the support library for libxml

%prep
%autosetup -p1

sed \
  -e /xmlInitializeCatalog/d \
  -e 's/((ent->checked =.*&&/(((ent->checked == 0) ||\
          ((ent->children == NULL) \&\& (ctxt->options \& XML_PARSE_NOENT))) \&\&/' \
  -i parser.c

%build
%configure \
  --disable-static \
  --with-history
make %{?_smp_mflags}

%install
[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot}/%{_libdir} -name '*.la' -delete
%{_fixperms} %{buildroot}/*

#Build and install python3-libxml2
make clean %{?_smp_mflags}
%configure \
    --disable-static \
    --with-python=/usr/bin/python3.5
make %{?_smp_mflags}
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%check
make -k check %{?_smp_mflags} |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_docdir}/*
%{_libdir}/libxml*
%{_libdir}/xml2Conf.sh
%{_bindir}/*
%{_datadir}/aclocal/*
%{_datadir}/gtk-doc/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files python
%defattr(-,root,root)
%{python2_sitelib}/*

%files -n python3-libxml2
%defattr(-,root,root)
%{python3_sitelib}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/libxml2/libxml2-config.cmake

%changelog
* Sat Jun 19 2021 Ankit Jain <ankitja@vmware.com> 2.9.11-2
- fix for lxml API issue
* Mon May 31 2021 Sujay G <gsujay@vmware.com> 2.9.11-1
- Bump version to 2.9.11 to fix CVE-2021-3517, CVE-2021-3518, CVE-2021-3537.
- Remove other unnecessary patches.
* Tue Sep 15 2020 Prashant S Chauhan <psinghchauha@vmware.com> 2.9.10-3
- Fix for CVE-2020-24977(Fix Buffer Overflow vulnerability)
* Wed Feb 05 2020 Shreyas B <shreyasb@vmware.com> 2.9.10-2
- Fix for CVE-2019-20388(Fix memory leak in xmlSchemaValidateStream).
* Thu Jan 30 2020 Shreyas B <shreyasb@vmware.com> 2.9.10-1
- Updgrade to v2.9.10 to address CVE-2019-19956(memory leak issue).
- Fix CVE-2020-7595(end-of-file issue).
* Mon Oct 29 2018 Siju Maliakkal <smaliakkal@vmware.com> 2.9.8-2
- Apply patch to fix CVE-2018-14404
* Fri May 11 2018 Sharath George <sharathg@vmware.com> 2.9.8-1
- Update to 2.9.8
* Mon Dec 04 2017 Kumar Kaushik <kaushikk@vmware.com> 2.9.6-2
- Release bump to use python 3.5.4.
* Wed Oct 18 2017 Xiaolin Li <xiaolinl@vmware.com> 2.9.6-1
- Update to version 2.9.6
* Wed Aug 09 2017 Dheeraj Shetty <dheerajs@vmware.com> 2.9.4-7
- Apply patch for CVE-2017-8872
* Mon Jul 10 2017 Divya Thaluru <dthaluru@vmware.com> 2.9.4-6
- Apply patch for CVE-2017-9047, CVE-2017-9048, CVE-2017-9049 and CVE-2017-9050
* Thu May 18 2017 Xiaolin Li <xiaolinl@vmware.com> 2.9.4-5
- Move python2 requires to python subpackage.
* Thu Apr 13 2017 Xiaolin Li <xiaolinl@vmware.com> 2.9.4-4
- Added python3-libxml2 package.
* Tue Jan 3 2017 Alexey Makhalov <amakhalov@vmware.com> 2.9.4-3
- Fix for CVE-2016-9318
* Thu Oct 20 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.9.4-2
- Apply patch for CVE-2016-5131
* Wed Jun 01 2016 Anish Swaminathan <anishs@vmware.com> 2.9.4-1
- Upgrade to 2.9.4
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.9.3-2
- GA - Bump release of all rpms
* Tue Feb 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.9.3-1
- Upgraded to version 2.9.3
* Thu Jan 28 2016 Xiaolin Li <xiaolinl@vmware.com> 2.9.2-1
- Downgrade to version 2.9.2
- libxml 2.9.3 has been found to have major functional issues.
- Until these are resolved, please roadmap updating to 2.9.2.
* Wed Dec 2 2015 Xiaolin Li <xiaolinl@vmware.com> 2.9.3-1
- Update to version 2.9.3
* Thu Jul 2 2015 Mahmoud Bassiouny <mbassiouny@vmware.com> 2.9.1-3
- Seperate the python module from the main library
* Thu Jun 11 2015 Alexey Makhalov <amakhalov@vmware.com> 2.9.1-2
- Moved 'Provides: pkgconfig(...)' into base package
* Mon Oct 13 2014 Divya Thaluru <dthaluru@vmware.com> 2.9.1-1
- Initial build.  First version
