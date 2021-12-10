Summary:        Measures number of Terminal column cells of wide-character codes.
Name:           python3-wcwidth
Version:        0.2.5
Release:        2%{?dist}
License:        MIT
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/wcwidth
Source0:        https://files.pythonhosted.org/packages/source/w/wcwidth/wcwidth-%{version}.tar.gz
%define         sha1 wcwidth=3822ed26dc70a4055827bc66cdc21126e51efd66

BuildRequires:  python3
BuildRequires:  python3-libs
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3
Requires:       python3-libs

BuildArch:      noarch

%description
This Library is mainly for those implementing a Terminal Emulator, or programs that carefully produce output to be interpreted by one.

%prep
%autosetup -n wcwidth-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python3 setup.py test

%files
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 0.2.5-2
-   Bump up to compile with python 3.10
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 0.2.5-1
-   Automatic Version Bump
*   Thu Jun 11 2020 Tapas Kundu <tkundu@vmware.com> 0.1.7-3
-   Mass removal python2
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 0.1.7-2
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Wed Apr 05 2017 Xiaolin Li <xiaolinl@vmware.com> 0.1.7-1
-   Initial packaging for Photon
