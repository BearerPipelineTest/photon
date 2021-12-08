%global	major 78
Summary:       Mozilla's JavaScript engine.
Name:          mozjs
Version:       78.3.1
Release:       4%{?dist}
Group:         Applications/System
Vendor:        VMware, Inc.
License:       GPLv2+ or LGPLv2+ or MPL-2.0
URL:           https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey
Source0:       https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz
%define sha1   firefox-%{version}=b60bcb10184a682380832c0f558c89cfa25d3dbf
Patch0:        emitter.patch
Patch1:        emitter_test.patch
# Build fixes
Patch2:        init_patch.patch
Patch3:        spidermonkey_checks_disable.patch
Patch4:        rust-nix-fix.patch
Patch5:        compile-with-python3.10.patch
Distribution:  Photon
BuildRequires: which
BuildRequires: python3-xml
BuildRequires: python3-libs
BuildRequires: python3-devel
BuildRequires: zlib-devel
BuildRequires: clang-devel
BuildRequires: icu-devel
BuildRequires: rust
BuildRequires: autoconf = 2.13
Requires:      icu
Requires:      python3
Requires:      python3-libs
Obsoletes:     mozjs60
Obsoletes:     js

%description
Mozilla's JavaScript engine includes a just-in-time compiler (JIT) that compiles
JavaScript to machine code, for a significant speed increase.

%package devel
Summary:        mozjs devel
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}
%description devel
This contains development tools and libraries for SpiderMonkey.

%prep
%autosetup -p1 -n firefox-%{version}
rm -rf modules/zlib

%build
cd js/src
%configure \
    --with-system-icu \
    --enable-readline \
    --disable-jemalloc \
    --disable-tests \
    --with-system-zlib
make %{?_smp_mflags}

%install
cd js/src
make %{?_smp_mflags} DESTDIR=%{buildroot} install
chmod -x %{buildroot}%{_libdir}/pkgconfig/*.pc
# remove non required files
rm %{buildroot}%{_libdir}/libjs_static.ajs
rm -rf %{buildroot}%{_libdir}/debug
rm -rf %{buildroot}/usr/src
find %{buildroot} -name '*.la' -delete

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/js%{major}
%{_bindir}/js%{major}-config
%{_libdir}/libmozjs-%{major}.so

%files devel
%defattr(-,root,root)
%{_includedir}/mozjs-%{major}
%{_libdir}/pkgconfig/mozjs-%{major}.pc

%changelog
*   Mon Nov 15 2021 Prashant S Chauhan <psinghchauha@vmware.com> 78.3.1-4
-   Update release to compile with python 3.10
*   Tue Apr 20 2021 Ankit Jain <ankitja@vmware.com> 78.3.1-3
-   Fix build failure with rust-1.51.0
*   Fri Feb 19 2021 Alexey Makhalov <amakhalov@vmware.com> 78.3.1-2
-   Remove python2 requirements
*   Mon Oct 05 2020 Ankit Jain <ankitja@vmware.com> 78.3.1-1
-   Updated to 78.3.1
*   Tue Aug 25 2020 Ankit Jain <ankitja@vmware.com> 68.11.0-2
-   Removed autoconf213 dependency and obsoletes js
*   Sat Oct 26 2019 Ankit Jain <ankitja@vmware.com> 68.11.0-1
-   initial version
