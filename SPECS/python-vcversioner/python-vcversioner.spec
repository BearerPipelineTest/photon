Name:           python3-vcversioner
Version:        2.16.0.0
Release:        3%{?dist}
Summary:        Python version extractor
License:        ISC
Group:          Development/Languages/Python
Url:		https://github.com/habnabit/vcversioner
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        vcversioner-%{version}.tar.gz
%define sha1    vcversioner=ce076b62e8f0772bf79f29762bfc3cf09f6781b5

BuildRequires: python3
BuildRequires: python3-libs
BuildRequires: python3-setuptools
BuildRequires: python3-xml
BuildRequires: python3-macros

BuildArch:      noarch

%description
Elevator pitch: you can write a setup.py with no version information specified, and vcversioner will find a recent, properly-formatted VCS tag and extract a version from it.

%prep
%autosetup -n vcversioner-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python3 setup test

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 2.16.0.0-3
-   Bump up to compile with python 3.10
*   Thu Jun 11 2020 Tapas Kundu <tkundu@vmware.com> 2.16.0.0-2
-   Mass removal python2
*   Tue Oct 23 2018 Sujay G <gsujay@vmware.com> 2.16.0.0-1
-   Initial version
