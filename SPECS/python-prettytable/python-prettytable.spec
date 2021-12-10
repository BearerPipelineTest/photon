Name:           python3-prettytable
Version:        0.7.2
Release:        8%{?dist}
Summary:        Library for displaying tabular data in a visually appealing ASCII format
License:        BSD-2-Clause
Group:          Development/Languages/Python
Vendor:		VMware, Inc.
Distribution:	Photon
Url:            http://code.google.com/p/prettytable/
Source0:        prettytable-%{version}.tar.gz
%define sha1 prettytable=b7d0bf0feee0d23108a044ffae44aff5c5935250

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml

Requires:       python3
Requires:       python3-libs

BuildArch:      noarch

%description
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by
specifying a row range.



%prep
%autosetup -n prettytable-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
LANG=en_US.UTF-8 python3 prettytable_test.py

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 0.7.2-8
-   Bump up to compile with python 3.10
*   Sat Jun 20 2020 Tapas Kundu <tkundu@vmware.com> 0.7.2-7
-   Mass removal python2
*   Wed Jul 26 2017 Divya Thaluru <dthaluru@vmware.com> 0.7.2-6
-   Fixed rpm check errors
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 0.7.2-5
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Tue May 16 2017 Kumar Kaushik <kaushikk@vmware.com> 0.7.2-4
-   Adding python3 support.
*   Tue Oct 04 2016 ChangLee <changlee@vmware.com> 0.7.2-3
-   Modified %check
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.7.2-2
-   GA - Bump release of all rpms
*   Wed Mar 04 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
-   Initial packaging for Photon
