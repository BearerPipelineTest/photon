Name:           python3-pytest
Version:        6.1.2
Release:        3%{?dist}
Summary:        pytest is a mature full-featured Python testing tool that helps you write better programs
License:        MIT
Group:          Development/Languages/Python
URL:            https://docs.pytest.org
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://pypi.python.org/packages/00/e9/f77dcd80bdb2e52760f38dbd904016da018ab4373898945da744e5e892e9/pytest-%{version}.tar.gz
%define sha1    pytest=aef7f0b5a3a5be7dc8c4a65b95d000f95df8b525

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-attrs
BuildRequires:  python3-iniconfig
BuildRequires:  python3-more-itertools
BuildRequires:  python3-packaging
BuildRequires:  python3-pluggy
BuildRequires:  python3-py
BuildRequires:  python3-toml
BuildRequires:  python3-wcwidth

Requires:       python3
Requires:       python3-libs
Requires:       python3-pluggy
Requires:       python3-iniconfig
Requires:       python3-packaging
Requires:       python3-toml
Requires:       python3-attrs
Requires:       python3-py

BuildArch:      noarch

%description
pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

%prep
%autosetup -n pytest-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest%{python3_version}
ln -snf pytest%{python3_version} %{buildroot}%{_bindir}/pytest3
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test%{python3_version}
ln -snf py.test%{python3_version} %{buildroot}%{_bindir}/py.test3

%check
make %{_smp_mflags} -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%files
%defattr(-,root,root,-)
%{_bindir}/pytest3
%{_bindir}/pytest%{python3_version}
%{_bindir}/py.test3
%{_bindir}/py.test%{python3_version}
%{python3_sitelib}/*

%changelog
*   Mon Nov 15 2021 Prashant S Chauhan <psinghchauha@vmware.com> 6.1.2-3
-   Update release to compile with python 3.10
*   Tue Dec 15 2020 Shreenidhi Shedi <sshedi@vmware.com> 6.1.2-2
-   Fix build with new rpm
*   Fri Nov 06 2020 Gerrit Photon <photon-checkins@vmware.com> 6.1.2-1
-   Automatic Version Bump
*   Tue Sep 29 2020 Gerrit Photon <photon-checkins@vmware.com> 6.1.0-1
-   Automatic Version Bump
*   Mon Sep 21 2020 Gerrit Photon <photon-checkins@vmware.com> 6.0.2-1
-   Automatic Version Bump
*   Tue Aug 11 2020 Gerrit Photon <photon-checkins@vmware.com> 6.0.1-1
-   Automatic Version Bump
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 5.4.3-1
-   Automatic Version Bump
*   Mon Jun 15 2020 Tapas Kundu <tkundu@vmware.com> 3.8.2-2
-   Mass removal python2
*   Tue Oct 09 2018 Tapas Kundu <tkundu@vmware.com> 3.8.2-1
-   Updated to release 3.8.2
-   Removed buildrequires from subpackage.
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 3.0.7-3
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.0.7-2
-   Use python2 instead of python and rename the scripts in bin directory
*   Tue Apr 25 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.0.7-1
-   Initial
