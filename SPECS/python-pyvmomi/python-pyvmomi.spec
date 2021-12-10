Summary:        pyVmomi is the Python SDK for the VMware vSphere API that allows you to manage ESX, ESXi, and vCenter.
Name:           python3-pyvmomi
Version:        7.0.1
Release:        2%{?dist}
License:        OSI Approved :: Apache Software License
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/pyvmomi
Source0:        pyvmomi-%{version}.tar.gz
%define sha1    pyvmomi=aceec58a3ceeecf381ea75188d277806e47e68df
BuildRequires:  python3
BuildRequires:  python3-libs
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
%if %{with_check}
BuildRequires:  curl-devel
%endif
Requires:       python3
Requires:       python3-libs
BuildArch:      noarch

%description
pyVmomi is the Python SDK for the VMware vSphere API that allows you to manage ESX, ESXi, and vCenter.

%prep
%autosetup -n pyvmomi-%{version}

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
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 7.0.1-2
-   Bump up to compile with python 3.10
*   Fri Nov 06 2020 Gerrit Photon <photon-checkins@vmware.com> 7.0.1-1
-   Automatic Version Bump
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 7.0-1
-   Automatic Version Bump
*   Sat Jun 20 2020 Tapas Kundu <tkundu@vmware.com> 6.7.0.2018.9-3
-   Mass removal python2
*   Fri Dec 07 2018 Tapas Kundu <tkundu@vmware.com> 6.7.0.2018.9-2
-   Fix make check
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 6.7.0.2018.9-1
-   Update to version 6.7.0.2018.9
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 6.5-2
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Mon Mar 06 2017 Xiaolin Li <xiaolinl@vmware.com> 6.5-1
-   Initial packaging for Photon.
