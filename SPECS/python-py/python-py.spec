Name:           python3-py
Version:        1.9.0
Release:        3%{?dist}
Summary:        Python development support library
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/pytest-dev/py
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://pypi.python.org/packages/53/72/6c6f1e787d9cab2cc733cf042f125abec07209a58308831c9f292504e826/py-%{version}.tar.gz
%define sha1    py=8cbe522347596ffc292fd9b1ceaa4564a551ac76

Patch0:         python-py-CVE-2020-29651.patch
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-xml

Requires:       python3
Requires:       python3-libs

BuildArch:      noarch

%description
The py lib is a Python development support library featuring the following tools and modules:

py.path: uniform local and svn path objects
py.apipkg: explicit API control and lazy-importing
py.iniconfig: easy parsing of .ini files
py.code: dynamic code generation and introspection

%prep
%autosetup -p1 -n py-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
#python-py and python-pytest have circular dependency. Hence not adding tests
make %{?_smp_mflags} -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 1.9.0-3
-   Bump up to compile with python 3.10
*   Mon Jun 21 2021 Dweep Advani <dadvani@vmware.com> 1.9.0-2
-   Patched for CVE-2020-29651
*   Tue Jul 28 2020 Tapas Kundu <tkundu@vmware.com> 1.9.0-1
-   Updated to version 1.9.0
*   Tue Jun 16 2020 Tapas Kundu <tkundu@vmware.com> 1.6.0-2
-   Mass removal python2
*   Thu Sep 13 2018 Tapas Kundu <tkundu@vmware.com> 1.6.0-1
-   Updated to versiob 1.6.0
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 1.4.33-3
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.4.33-2
-   Use python2_sitelib
*   Tue Apr 25 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.4.33-1
-   Initial
