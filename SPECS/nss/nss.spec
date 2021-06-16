Summary:        Security client
Name:           nss
Version:        3.44
Release:        4%{?dist}
License:        MPLv2.0
URL:            http://ftp.mozilla.org/pub/mozilla.org/security/nss/
Group:          Applications/System
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        %{name}-%{version}.tar.gz
%define sha1    nss=11eab8681754472a9d1eb196e3c604d794ebe7f3
Patch0:         nss-3.44-standalone-1.patch
Patch1:         nss-CVE-2020-12403.patch
Requires:       nspr
Requires:       sqlite-autoconf
BuildRequires:  nspr
BuildRequires:  sqlite-autoconf

%description
 The Network Security Services (NSS) package is a set of libraries
 designed to support cross-platform development of security-enabled
 client and server applications. Applications built with NSS can
 support SSL v2 and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12,
 S/MIME, X.509 v3 certificates, and other security standards.
 This is useful for implementing SSL and S/MIME or other Internet
 security standards into an application.

%package devel
Summary: Development Libraries for Network Security Services
Group: Development/Libraries
Requires: nss = %{version}-%{release}
%description devel
Header files for doing development with Network Security Services.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%build
cd nss
# -j is not supported by nss
make VERBOSE=1 BUILD_OPT=1 \
    NSPR_INCLUDE_DIR=%{_includedir}/nspr \
    USE_SYSTEM_ZLIB=1 \
    ZLIB_LIBS=-lz \
    $([ $(uname -m) = x86_64 ] && echo USE_64=1) \
    $([ -f %{_includedir}/sqlite3.h ] && echo NSS_USE_SYSTEM_SQLITE=1)

%install
cd nss
cd ../dist
install -vdm 755 %{buildroot}%{_bindir}
install -vdm 755 %{buildroot}%{_includedir}/nss
install -vdm 755 %{buildroot}%{_libdir}
install -v -m755 Linux*/lib/*.so %{buildroot}%{_libdir}
install -v -m644 Linux*/lib/{*.chk,libcrmf.a} %{buildroot}%{_libdir}
cp -v -RL {public,private}/nss/* %{buildroot}%{_includedir}/nss
chmod 644 %{buildroot}%{_includedir}/nss/*
install -v -m755 Linux*/bin/{certutil,nss-config,pk12util} %{buildroot}%{_bindir}
install -vdm 755 %{buildroot}%{_libdir}/pkgconfig
install -vm 644 Linux*/lib/pkgconfig/nss.pc %{buildroot}%{_libdir}/pkgconfig
%define __spec_install_post \
  %{?__debug_package:%{__debug_install_post}} \
  %{__arch_install_post} \
  %{__os_install_post} \
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} Linux*/bin/shlibsign -i %{buildroot}%{_libdir}/libsoftokn3.so \
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} Linux*/bin/shlibsign -i %{buildroot}%{_libdir}/libnssdbm3.so \
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} Linux*/bin/shlibsign -i %{buildroot}%{_libdir}/libfreebl3.so \
  LD_LIBRARY_PATH=%{buildroot}%{_libdir} Linux*/bin/shlibsign -i %{buildroot}%{_libdir}/libfreeblpriv3.so \
%{nil}

%check
cd nss/tests
chmod g+w . -R
useradd test -G root -m
HOST=localhost DOMSUF=localdomain BUILD_OPT=1
sudo -u test ./all.sh && userdel test -r -f

%post -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.chk
%{_libdir}/*.so

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc

%changelog
*   Fri Jun 11 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 3.44-4
-   Fix CVE-2020-12403
*   Mon Jun 01 2020 Siju Maliakkal <smaliakkal@vmware.com> 3.44-3
-   use latest sqlite
*   Fri Aug 09 2019 Ashwin H <ashwinh@vmware.com> 3.44-2
-   Fix to enable nss in fips mode
*   Wed May 29 2019 Michelle Wang <michellew@vmware.com> 3.44-1
-   Upgrade to 3.44 for CVE-2018-12404
*   Tue May 29 2018 Xiaolin Li <xiaolinl@vmware.com> 3.31.1-1
-   Upgrade to 3.31.1
*   Tue Jun 20 2017 Xiaolin Li <xiaolinl@vmware.com> 3.31-1
-   Upgrade to 3.31.
*   Tue Jul 05 2016 Anish Swaminathan <anishs@vmware.com> 3.25-1
-   Upgrade to 3.25
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.21-2
-   GA - Bump release of all rpms
*   Thu Jan 21 2016 Xiaolin Li <xiaolinl@vmware.com> 3.21
-   Updated to version 3.21
*   Tue Aug 04 2015 Kumar Kaushik <kaushikk@vmware.com> 3.19-2
-   Version update. Firefox requirement.
*   Fri May 29 2015 Alexey Makhalov <amakhalov@vmware.com> 3.19-1
-   Version update. Firefox requirement.
*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 3.15.4-1
-   Initial build. First version
