Name:           python3-jsonpatch
Version:        1.26
Release:        2%{?dist}
Summary:        Applying JSON Patches in Python
License:        Modified BSD License
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:		https://pypi.python.org/pypi/jsonpatch
Source0:        https://pypi.python.org/packages/be/c1/947048a839120acefc13a614280be3289db404901d1a2d49b6310c6d5757/jsonpatch-%{version}.tar.gz
%define sha1    jsonpatch=0650a2b986452fe49e346cdad993a6af5d82917a

BuildRequires: python3
BuildRequires: python3-libs
BuildRequires: python3-setuptools
BuildRequires: python3-jsonpointer
BuildRequires: python3-macros
Requires: python3-jsonpointer

BuildArch:      noarch

%description
Library to apply JSON Patches according to RFC 6902.


%prep
%autosetup -n jsonpatch-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python3 ext_tests.py && python3 tests.py

%files
%defattr(-,root,root,-)
%{_bindir}/jsondiff
%{_bindir}/jsonpatch
%{python3_sitelib}/*

%changelog
*       Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 1.26-2
-       Bump up to compile with python 3.10
*       Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 1.26-1
-       Automatic Version Bump
*       Sat Jun 20 2020 Tapas Kundu <tkundu@vmware.com> 1.23-2
-       Mass removal python2
*       Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 1.23-1
-       Update to version 1.23
*       Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.15-4
-       Separate python3 and python2 specific scripts in bin directory
*       Thu Apr 27 2017 Sarah Choi <sarahc@vmware.com> 1.15-3
-       Rename jsonpatch for python3
*       Thu Apr 06 2017 Sarah Choi <sarahc@vmware.com> 1.15-2
-       support python3
*       Mon Apr 03 2017 Sarah Choi <sarahc@vmware.com> 1.15-1
-       Update to 1.15
*       Tue Oct 04 2016 ChangLee <changlee@vmware.com> 1.9-3
-       Modified %check
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.9-2
-	GA - Bump release of all rpms
* Wed Mar 04 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
- Initial packaging for Photon
