Summary:        A Universal Character Encoding Detector in Python
Name:           python3-chardet
Version:        3.0.4
Release:        3%{?dist}
Url:            https://pypi.org/project/chardet/
License:        LGPL v2.1
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://github.com/chardet/chardet/archive/chardet-%{version}.tar.gz
%define sha1    chardet=bf740348e002581b026dc4af47d56479097c1fcd

BuildRequires:  python3
BuildRequires:  python3-libs
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
%if %{with_check}
BuildRequires:  python3-pytest
%endif

Requires:       python3
Requires:       python3-libs

BuildArch:      noarch

%description
chardet is a universal character encoding detector in Python.


%prep
%autosetup -n chardet-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
# TODO

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/chardetect

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 3.0.4-3
-   Bump up to compile with python 3.10
*   Tue Jun 16 2020 Tapas Kundu <tkundu@vmware.com> 3.0.4-2
-   Mass removal python2
*   Thu Sep 27 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 3.0.4-1
-   Initial packaging.
