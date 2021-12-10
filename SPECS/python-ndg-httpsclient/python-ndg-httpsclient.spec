Name:           python3-ndg-httpsclient
Version:        0.5.1
Release:        5%{?dist}
Summary:        Enhanced HTTPS support for httplib and urllib2 using PyOpenSSL.
License:        BSD
Group:          Development/Languages/Python
Url:            https://pypi.python.org/pypi/ndg-httpsclient
Source0:        ndg_httpsclient-%{version}.tar.gz
%define sha1    ndg_httpsclient=aa0b3c2d8ada61fa3f4e82ed307056b14cc63cb9
Vendor:         VMware, Inc.
Distribution:   Photon

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
%if %{with_check}
BuildRequires:  python3-urllib3
BuildRequires:  python3-pyOpenSSL
BuildRequires:  openssl-devel
BuildRequires:  curl-devel
BuildRequires:  libffi-devel
%endif
Requires:       python3
Requires:       python3-libs
Requires:       python3-setuptools
BuildArch:      noarch

%description
Enhanced HTTPS support for httplib and urllib2 using PyOpenSSL.


%prep
%autosetup -n ndg_httpsclient-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
pushd ndg/httpsclient/test

openssl s_server -www -cert pki/localhost.crt -key pki/localhost.key -accept 4443 &
openssl_pid=$!
if ps -p $openssl_pid > /dev/null
then
    echo "Started openssl. PID:$openssl_pid"
else
    echo "Failed to start openssl"
    exit 1
fi

trap "{ kill $openssl_pid ; }" EXIT


function run_python3_test()
{
    test_script="$1"
    PATH=%{buildroot}%{_bindir}:${PATH} \
    PYTHONPATH=%{buildroot}%{python3_sitelib} \
    python3 $test_script
}

test_cases=(test_urllib2.py test_https.py test_utils.py)
for test_case in "${test_cases[@]}"
do
    run_python3_test $test_case
done

popd

%files
%defattr(-,root,root,-)
%{_bindir}/ndg_httpclient
%{python3_sitelib}/*

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 0.5.1-5
-   Bump up to compile with python 3.10
*   Tue Sep 29 2020 Satya Naga Vasamsetty <svasamsetty@vmware.com> 0.5.1-4
-   openssl 1.1.1
*   Thu Jun 18 2020 Tapas Kundu <tkundu@vmware.com> 0.5.1-3
-   Remove python3
*   Wed Dec 05 2018 Ashwin H <ashwinh@vmware.com> 0.5.1-2
-   Add %check
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 0.5.1-1
-   Updated to 0.5.1
*   Tue Aug 29 2017 Vinay Kulkarni <kulkarniv@vmware.com> 0.4.2-1
-   Initial version of python ndg-httpsclient for PhotonOS.
