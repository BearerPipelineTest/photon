Summary:        A XML/HTML/XHTML Markup safe string for Python.
Name:           python3-markupsafe
Version:        1.1.1
Release:        2%{?dist}
License:        BSD
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/MarkupSafe
Source0:        https://pypi.python.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-%{version}.tar.gz
%define sha1    MarkupSafe=f70e5fd3c120a1b108d4347ea1115e3962c42026

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
%if %{with_check}
BuildRequires:  python3-pip
%endif
Requires:       python3
Requires:       python3-libs

%description
MarkupSafe implements a XML/HTML/XHTML Markup safe string for Python.


%prep
%autosetup -p1 -n MarkupSafe-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
pip3 install py
python3 setup.py test

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Mon Nov 15 2021 Prashant S Chauhan <psinghchauha@vmware.com> 1.1.1-2
-   Update release to compile with python 3.10
*   Sun Jul 26 2020 Tapas Kundu <tkundu@vmware.com> 1.1.1-1
-   Update to 1.1.1
*   Fri Jun 19 2020 Tapas Kundu <tkundu@vmware.com> 1.0-4
-   Mass removal python2
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 1.0-3
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.0-2
-   Removed erroneous version line
*   Thu Mar 30 2017 Sarah Choi <sarahc@vmware.com> 1.0-1
-   Upgrade version to 1.0
*   Thu Mar 02 2017 Xiaolin Li <xiaolinl@vmware.com> 0.23-1
-   Initial packaging for Photon
