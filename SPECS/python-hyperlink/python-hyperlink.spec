Summary:        provides a pure-Python implementation of immutable URLs
Name:           python3-hyperlink
Version:        20.0.1
Release:        3%{?dist}
License:        MIT
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://github.com/python-hyper/hyperlink
Source0:        https://github.com/python-hyper/hyperlink/archive/hyperlink-%{version}.tar.gz
%define sha1    hyperlink=2004894d4e90436988065c3cb00d13f4d9c1dcce

BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       python3
Requires:       python3-libs
%if %{with_check}
BuildRequires:  python3-idna
BuildRequires:  curl-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-pip
%endif
BuildArch:      noarch

%description
Hyperlink provides a pure-Python implementation of immutable URLs. Based on RFC 3986 and 3987, the Hyperlink URL makes working with both URIs and IRIs easy.

%prep
%autosetup -p1 -n hyperlink-%{version}

%build
python3 setup.py build


%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
pip3 install pytest
pytest

%files
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
*   Mon Nov 15 2021 Prashant S Chauhan <psinghchauha@vmware.com> 20.0.1-3
-   Update release to compile with python 3.10
*   Tue Sep 29 2020 Satya Naga Vasamsetty <svasamsetty@vmware.com> 20.0.1-2
-   openssl 1.1.1
*   Tue Aug 11 2020 Gerrit Photon <photon-checkins@vmware.com> 20.0.1-1
-   Automatic Version Bump
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 19.0.0-1
-   Automatic Version Bump
*   Fri Jun 19 2020 Tapas Kundu <tkundu@vmware.com> 18.0.0-3
-   Mass removal python2
*   Thu Dec 06 2018 Tapas Kundu <tkundu@vmware.com> 18.0.0-2
-   Fix make check.
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 18.0.0-1
-   Update to version 18.0.0
*   Wed Sep 20 2017 Bo Gan <ganb@vmware.com> 17.3.1-2
-   Fix make check issues
*   Mon Sep 11 2017 Dheeraj Shetty <dheerajs@vmware.com> 17.3.1-1
-   Initial packaging for Photon
