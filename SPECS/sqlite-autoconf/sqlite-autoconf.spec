%define sourcever 3320100
Summary:        A portable, high level programming interface to various calling conventions
Name:           sqlite-autoconf
Version:        3.32.1
Release:        2%{?dist}
License:        Public Domain
URL:            http://www.sqlite.org
Group:          System Environment/GeneralLibraries
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://sqlite.org/2020/%{name}-3320100.tar.gz
%define sha1    sqlite=3d34d86ef726b66edeb0b93b2a4c0d036ea8dcf3

Patch0:         sqlite-CVE-2020-15358.patch

Obsoletes:      libsqlite
Provides:       sqlite3

%description
This package contains most of the static files that comprise the
www.sqlite.org website including all of the SQL Syntax and the
C/C++ interface specs and other miscellaneous documentation.

%prep
%autosetup -p1 -n %{name}-%{sourcever}

%build
sh ./configure \
    CFLAGS="%{optflags}                 \
    -DSQLITE_ENABLE_FTS3=1              \
    -DSQLITE_ENABLE_COLUMN_METADATA     \
    -DSQLITE_ENABLE_UNLOCK_NOTIFY=1     \
    -DSQLITE_SECURE_DELETE=1"           \
    CXXFLAGS="%{optflags}               \
    -DSQLITE_ENABLE_FTS3=1              \
    -DSQLITE_ENABLE_COLUMN_METADATA=1   \
    -DSQLITE_ENABLE_UNLOCK_NOTIFY=1     \
    -DSQLITE_SECURE_DELETE=1"           \
    --prefix=%{_prefix}                 \
    --bindir=%{_bindir}                 \
    --libdir=%{_libdir}                 \
    --disable-static
make %{?_smp_mflags}

%install
[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -D -m644 sqlite3.1 %{buildroot}/%{_mandir}/man1/sqlite3.1
find %{buildroot}/%{_libdir} -name '*.la' -delete
rm -rf %{buildroot}/%{_infodir}
%{_fixperms} %{buildroot}/*

%check
make -k check %{?_smp_mflags} |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_libdir}/*.so*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_mandir}/man1/*

%changelog
* Fri Jul 03 2020 Shreyas B <shreyasb@vmware.com> 3.32.1-2
- Fix for CVE-2020-15358
* Thu May 28 2020 Siju Maliakkal <smaliakkal@vmware.com> 3.32.1-1
- Upgrade to 3.32.1 for following CVEs
- CVE-2020-13630 CVE-2020-13434 CVE-2020-13435 CVE-2020-13631 CVE-2020-13632
* Wed Apr 15 2020 Siju Maliakkal <smaliakkal@vmware.com> 3.31.1-3
- Fix for CVE-2020-9327
* Mon Apr 13 2020 Ankit Jain <ankitja@vmware.com> 3.31.1-2
- Fix for CVE-2020-11656
* Thu Jan 30 2020 Siju Maliakkal <smaliakkal@vmware.com> 3.31.1-1
- Upgrade to 3.31.1 for following CVEs.
- CVE-2019-19959 CVE-2019-19926 CVE-2019-19925 CVE-2019-19923 CVE-2019-19244
* Mon Jan 06 2020 Ankit Jain <ankitja@vmware.com> 3.30.1-2
- Fix for CVE-2019-20218
* Fri Jan 03 2020 Ankit Jain <ankitja@vmware.com> 3.30.1-1
- Upgrade to version 3.30.1
* Fri Dec 20 2019 Ankit Jain <ankitja@vmware.com> 3.27.2-5
- Fix for CVE-2019-19317,CVE-2019-19603, CVE-2019-19646
* Fri Oct 18 2019 Michelle Wang <michellew@vmware.com> 3.27.2-4
- Add patch CVE-2019-16168.patch.
* Wed Jun 5 2019 Michelle Wang <michellew@vmware.com> 3.27.2-3
- Add patch CVE-2019-8457.
* Thu Apr 25 2019 Michelle Wang <michellew@vmware.com> 3.27.2-2
- Add patch CVE-2019-9937.
* Mon Apr 15 2019 Michelle Wang <michellew@vmware.com> 3.27.2-1
- Upgrade to 3.27.2 and add patch CVE-2019-9936.
* Sun Feb 3 2019 Michelle Wang <michellew@vmware.com> 3.26.0-1
- Upgrade to 3.26.0 for a critical Vulnerability named 'Magallan'.
* Thu May 31 2018 Xiaolin Li <xiaolinl@vmware.com> 3.22.0-3
- Change cflags.
* Tue Apr 17 2018 Xiaolin Li <xiaolinl@vmware.com> 3.22.0-2
- Apply patch for CVE-2018-8740
* Tue Feb 20 2018 Xiaolin Li <xiaolinl@vmware.com> 3.22.0-1
- Upgrade to version 3.22.0
* Fri Nov 10 2017 Xiaolin Li <xiaolinl@vmware.com> 3.21.0-1
- Upgrade to version 3.21.0
* Thu Jul 13 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.18.0-2
- Adding patch for CVE-2017-10989
* Mon May 8 2017 Divya Thaluru <dthaluru@vmware.com> 3.18.0-1
- Updated to version 3.18.0
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.11.0-2
- GA - Bump release of all rpms
* Tue Feb 23 2016 Xiaolin Li <xiaolinl@vmware.com> 3.11.0-1
- Updated to version 3.11.0
* Wed Feb 03 2016 Anish Swaminathan <anishs@vmware.com> - 3.8.3.1-2
- Fix versioning
* Tue Oct 7 2014 Divya Thaluru <dthaluru@vmware.com> 3080301-1
- Initial build.  First version
