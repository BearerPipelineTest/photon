Name:           python3-websocket-client
Version:        0.57.0
Release:        3%{?dist}
Summary:        WebSocket client for python
License:        LGPL
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/websocket-client
Source0:        websocket_client-%{version}.tar.gz
%define sha1    websocket_client=21ef1198b2d7a3125aac05ec25592099ded4cfb3

%if %{with_check}
BuildRequires:  openssl-devel
BuildRequires:  curl-devel
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       python3
Requires:       python3-libs

BuildArch:      noarch

%description
WebSocket client for python

%prep
%autosetup -n websocket_client-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python3 setup.py test

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
/usr/bin/wsdump.py

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 0.57.0-3
-   Bump up to compile with python 3.10
*   Tue Sep 29 2020 Satya Naga Vasamsetty <svasamsetty@vmware.com> 0.57.0-2
-   openssl 1.1.1
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 0.57.0-1
-   Automatic Version Bump
*   Thu Jun 11 2020 Tapas Kundu <tkundu@vmware.com> 0.53.0-3
-   Mass removal python2.
*   Fri Dec 07 2018 Ashwin H <ashwinh@vmware.com> 0.53.0-2
-   Add %check
*   Fri Sep 14 2018 Tapas Kundu <tkundu@vmware.com> 0.53.0-1
-   Updated to release 0.53.0
*   Thu Nov 30 2017 Xiaolin Li <xiaolinl@vmware.com> 0.44.0-1
-   Update websocket_client to version 0.44.0
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 0.7.0-2
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Sun Jun 04 2017 Vinay Kulkarni <kulkarniv@vmware.com> 0.7.0-1
-   Initial version of python WebSocket for PhotonOS.
