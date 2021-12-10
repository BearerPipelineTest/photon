Name:           python3-zope.interface
Version:        5.2.0
Release:        2%{?dist}
Url:            https://github.com/zopefoundation/zope.interface
Summary:        Interfaces for Python
License:        ZPL 2.1
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
%define sha1    zope.interface=7e0e62fa44bdae42266b4fdb7121857e14ef5f11

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       python3
Requires:       python3-libs
Requires:       python3-setuptools

%description
This package is intended to be independently reusable in any Python project. It is maintained by the Zope Toolkit project.

This package provides an implementation of “object interfaces” for Python. Interfaces are a mechanism for labeling objects as conforming to a given API or contract. So, this package can be considered as implementation of the Design By Contract methodology support in Python.

For detailed documentation, please see http://docs.zope.org/zope.interface

%prep
%autosetup -n zope.interface-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}


%check
python3 setup.py test

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 5.2.0-2
-   Bump up to compile with python 3.10
*   Fri Nov 06 2020 Gerrit Photon <photon-checkins@vmware.com> 5.2.0-1
-   Automatic Version Bump
*   Wed Sep 30 2020 Gerrit Photon <photon-checkins@vmware.com> 5.1.2-1
-   Automatic Version Bump
*   Thu Sep 03 2020 Tapas Kundu <tkundu@vmware.com> 5.1.0-2
-   Requires python3-setuptools for installation
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 5.1.0-1
-   Automatic Version Bump
*   Thu Jun 11 2020 Tapas Kundu <tkundu@vmware.com> 4.5.0-2
-   Mass removal python2
*   Fri Sep 14 2018 Tapas Kundu <tkundu@vmware.com> 4.5.0-1
-   Updated to release 4.5.0
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 4.3.3-2
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Mon Mar 13 2017 Xiaolin Li <xiaolinl@vmware.com> 4.3.3-1
-   Updated to version 4.3.3.
*   Tue Oct 04 2016 ChangLee <changlee@vmware.com> 4.1.3-3
-   Modified %check
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 4.1.3-2
-   GA - Bump release of all rpms
*   Tue Oct 27 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
-   Initial packaging for Photon
