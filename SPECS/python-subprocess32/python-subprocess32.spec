%define debug_package %{nil}

Name:           python3-subprocess32
Version:        3.5.4
Release:        3%{?dist}
Summary:        A backport of the subprocess module from Python 3.2/3.3 for use on 2.x
License:        PSF
Group:          Development/Languages/Python
Url:            https://pypi.python.org/pypi/subprocess32
Source0:        subprocess32-%{version}.tar.gz
%define sha1    subprocess32=73b07bcd4ac4acfcae9d3156451066ee7f034006
Vendor:         VMware, Inc.
Distribution:   Photon

BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
%if %{with_check}
BuildRequires:  python3-test
BuildRequires:  python3-pytest
%endif

Requires:       python3
Requires:       python3-libs
Requires:       python3-setuptools

%description
A backport of the subprocess module from Python 3.2/3.3 for use on 2.x

%prep
%autosetup -n subprocess32-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
PYTHONPATH=build/lib.linux-%{_arch}-%{python3_version}/ python3 test_subprocess32.py

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 3.5.4-3
-   Bump up to compile with python 3.10
*   Tue Dec 15 2020 Shreenidhi Shedi <sshedi@vmware.com> 3.5.4-2
-   Fix build with new rpm
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 3.5.4-1
-   Automatic Version Bump
*   Wed Jun 17 2020 Tapas Kundu <tkundu@vmware.com> 3.5.2-3
-   Mass removal python2
*   Tue Jan 08 2019 Alexey Makhalov <amakhalov@vmware.com> 3.5.2-2
-   Added BuildRequires python2-devel
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 3.5.2-1
-   Update to version 3.5.2
*   Mon Sep 25 2017 Rui Gu <ruig@vmware.com> 3.2.7-2
-   Fix make check failure.
*   Fri Aug 25 2017 Vinay Kulkarni <kulkarniv@vmware.com> 3.2.7-1
-   Initial version of python-subprocess32 package for Photon.
