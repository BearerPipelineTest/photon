Name:           python3-pyasn1
Version:        0.4.8
Release:        2%{?dist}
Summary:        Implementation of ASN.1 types and codecs in Python programming language
License:        BSD
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/packages/source/p/pyasn1/pyasn1-%{version}.tar.gz
Source0:        pyasn1-%{version}.tar.gz
%define sha1    pyasn1=e0fa19f8fda46a1fa2253477499b116b33f67175
BuildRequires:  python3
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-macros
Requires:       python3
Requires:       python3-libs
BuildArch:      noarch

%description
This is an implementation of ASN.1 types and codecs in Python programming language.
It has been first written to support particular protocol (SNMP),
but then generalized to be suitable for a wide range of protocols based on ASN.1 specification.

%prep
%autosetup -n pyasn1-%{version}

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
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 0.4.8-2
-   Bump up to compile with python 3.10
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 0.4.8-1
-   Automatic Version Bump
*   Fri Jun 19 2020 Tapas Kundu <tkundu@vmware.com> 0.4.4-2
-   Mass removal python2
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 0.4.4-1
-   Update to version 0.4.4
*   Thu Mar 23 2017 Xiaolin Li <xiaolinl@vmware.com> 0.2.3-1
-   Updated to version 0.2.3.
*   Tue Oct 04 2016 ChangLee <changlee@vmware.com> 0.1.9-3
-   Modified %check
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.1.9-2
-   GA - Bump release of all rpms
*   Tue Feb 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.1.9-1
-   Upgraded to version 0.1.9
*   Thu Aug 6 2015 Anish Swaminathan <anishs@vmware.com>
-   Added sha1sum
*   Fri Mar 13 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
-   Initial packaging for Photon
