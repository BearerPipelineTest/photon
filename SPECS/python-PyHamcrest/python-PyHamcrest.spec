Name:           python3-PyHamcrest
Version:        2.0.2
Release:        2%{?dist}
Summary:        Python Hamcrest framework for matcher objects
Group:          Development/Libraries
License:        BSD License (New BSD)
URL:            https://pypi.org/project/PyHamcrest
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://pypi.python.org/packages/source/n/deepmerge/PyHamcrest-%{version}.tar.gz
%define sha1    PyHamcrest=ba0c1e274bb0cd71a8bbb451fa657cc5c1fcc81e
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       python3
Requires:       python3-libs
BuildArch:      noarch

%description
PyHamcrest is a framework for writing matcher objects, allowing you to declaratively define “match” rules.


%prep
%autosetup -n PyHamcrest-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
#no test folder in source tar

%clean
rm -rf %{buildroot}/*


%files
%defattr(-,root,root,-)
%doc README.rst
%doc LICENSE.txt
%{python3_sitelib}/*

%changelog
*  Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 2.0.2-2
-  Bump up to compile with python 3.10
*  Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 2.0.2-1
-  Automatic Version Bump
*  Fri Jun 19 2020 Tapas Kundu <tkundu@vmware.com> 1.9.0-2
-  Mass removal python2
*  Fri Aug 30 2019 Tapas Kundu <tkundu@vmware.com> 1.9.0-1
-  Initial packaging for photon OS
