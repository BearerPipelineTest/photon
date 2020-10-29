Summary:        A free package dependency solver
Name:           libsolv
Version:        0.6.35
Release:        5%{?dist}
License:        BSD
URL:            https://github.com/openSUSE/libsolv
Source0:        https://github.com/openSUSE/libsolv/archive/%{name}-%{version}.tar.gz
%define sha1    libsolv=4f53d60467ddab4099cfe5eb91a3fe7260666209
Patch0:         libsolv-xmlparser.patch
Patch1:         libsolv-rpm4-IndexOoB-fix.patch
Patch2:         CVE-2019-20387.patch
# These 2 patches are required to build libdnf latest version in rpm-ostree
Patch3:         libsolv-Add-support-for-modular.patch
Patch4:         libsolv-Add-selection_make-support.patch
Patch5:         CVE-2018-20532-20533-20534.patch
Group:          Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon
Requires:       libdb
Requires:       expat-libs
BuildRequires:  libdb-devel
BuildRequires:  cmake
BuildRequires:  rpm-devel
BuildRequires:  expat-devel
%description
Libsolv is a free package management library, using SAT technology to solve requests.
It supports debian, rpm, archlinux and haiku style distributions.

%package devel
Summary:        Development headers for libsolv
Requires:       %{name} = %{version}-%{release}
Requires:       expat-devel
Provides:       pkgconfig(libsolv)
Provides:       pkgconfig(libsolvext)
%description devel
The libsolv-devel package contains libraries, header files and documentation
for developing applications that use libsolv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%build
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DRPM5=ON \
    -DENABLE_RPMDB=ON \
    -DENABLE_COMPLEX_DEPS=ON
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%check
make %{?_smp_mflags} test

%files
%defattr(-,root,root)
%{_bindir}/*
%{_lib64dir}/libsolv.so.*
%{_lib64dir}/libsolvext.so.*
%{_mandir}/man1/*


%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_lib64dir}/libsolv.so
%{_lib64dir}/libsolvext.so
%{_lib64dir}/pkgconfig/*
%{_datadir}/cmake/*
%{_mandir}/man3/*

%changelog
*   Thu Oct 29 2020 Keerthana K <keerthanak@vmware.com> 0.6.35-5
-   Fix CVE-2018-20532 CVE-2018-20533 CVE-2018-20534
*   Fri Aug 14 2020 Ankit Jain <ankitja@vmware.com> 0.6.35-4
-   Added 2 patches required to build libdnf latest version in rpm-ostree
*   Tue Feb 25 2020 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.35-3
-   provides pkgconfig(libsolvext).
*   Mon Feb 03 2020 Keerthana K <keerthanak@vmware.com> 0.6.35-2
-   Fix CVE-2019-20387
*   Tue Jun 04 2019 Ankit Jain <ankitja@vmware.com> 0.6.35-1
-   Updated to 0.6.35 and added a patch to fix Index outofBound
*   Thu Feb 14 2019 Keerthana K <keerthanak@vmware.com> 0.6.26-5
-   Fix for CVE-2018-20532, CVE-2018-20533, CVE-2018-20534.
*   Thu Mar 01 2018 Xiaolin Li <xiaolinl@vmware.com> 0.6.26-4
-   provides pkgconfig(libsolv).
*   Fri Apr 21 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.26-3
-   update libdb make config
*   Fri Apr 14 2017 Alexey Makhalov <amakhalov@vmware.com> 0.6.26-2
-   Requires expat-libs and expat-devel.
*   Tue Apr 04 2017 Kumar Kaushik <kaushikk@vmware.com>  0.6.26-1
-   Upgrade to 0.6.26
*   Mon Dec 19 2016 Xiaolin Li <xiaolinl@vmware.com> 0.6.19-4
-   Added -devel subpackage.
*   Thu Oct 27 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.19-3
-   use libdb
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.19-2
-   GA - Bump release of all rpms
*   Tue Feb 23 2016 Anish Swaminathan <anishs@vmware.com>  0.6.19-1
-   Upgrade to 0.6.19
*   Fri Jan 22 2016 Xiaolin Li <xiaolinl@vmware.com> 0.6.17-1
-   Updated to version 0.6.17
*   Tue Sep 22 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.6.6-3
-   Updated build-requires after creating devel package for db.
*   Wed May 20 2015 Touseef Liaqat <tliaqat@vmware.com> 0.6.6-2
-   Updated group.
*   Tue Nov 25 2014 Divya Thaluru <dthaluru@vmware.com> 0.6.6-1
-   Initial build. First version
