Summary:        Utilities for aufs
Name:           aufs-util
Version:        5.0
Release:        2%{?dist}
License:    	GPLv2
URL:        	http://aufs.sourceforge.net/
Group:        	System Environment
Vendor:         VMware, Inc.
Distribution: 	Photon

Source0:        %{name}-%{version}.tar.gz
%define sha1 %{name}=0a0c0798ee8f547f726b4a056168549e917efb61
Source1:        aufs5-standalone-5.7.tar.gz
%define sha1 aufs5-standalone-5.7=628eb716350cfce6be8481513ced047007fad491

BuildArch:      x86_64

Requires:       linux-secure

%description
These utilities are always necessary for aufs.

%prep
# Using autosetup is not feasible
%setup -q
# Using autosetup is not feasible
%setup -D -b 1
sed -i 's/__user//' ../aufs5-standalone-aufs5.7/include/uapi/linux/aufs_type.h
sed -i '/override LDFLAGS += -static -s/d' Makefile

%build
make CPPFLAGS="-I $PWD/../aufs5-standalone-aufs5.7/include/uapi" DESTDIR=%{buildroot} %{?_smp_mflags}

%install
make CPPFLAGS="-I $PWD/../aufs5-standalone-aufs5.7/include/uapi" DESTDIR=%{buildroot} install %{?_smp_mflags}
mv %{buildroot}/sbin %{buildroot}%{_usr}

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_sbindir}/*
%{_bindir}/*
%{_libdir}/*.so*
%{_mandir}/*
%exclude %dir %{_libdir}/debug

%changelog
* Tue Mar 01 2022 Shreenidhi Shedi <sshedi@vmware.com> 5.0-2
- Exclude debug symbols properly
* Fri Oct 09 2020 Ajay Kaher <akaher@vmware.com> 5.0-1
- Update to version 5.0
* Mon Oct 22 2018 Ajay Kaher <akaher@vmware.com> 4.14-2
- Adding BuildArch
* Wed Sep 19 2018 Ajay Kaher <akaher@vmware.com> 4.14-1
- Update to version 4.14
* Fri Jul 14 2017 Alexey Makhalov <amakhalov@vmware.com> 20170206-2
- Remove aufs source tarballs from git repo
* Fri Feb 10 2017 Alexey Makhalov <amakhalov@vmware.com> 20170206-1
- Initial build. First version
