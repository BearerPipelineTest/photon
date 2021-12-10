Summary:          OSS implementation of the TCG TPM2 Software Stack (TSS2)
Name:             tpm2-pkcs11
Version:          1.6.0
Release:          3%{?dist}
License:          BSD 2-Clause
URL:              https://github.com/tpm2-software/tpm2-pkcs11
Group:            System Environment/Security
Vendor:           VMware, Inc.
Distribution:     Photon
Source0:          %{name}-%{version}.tar.gz
%define sha1      tpm2=3e9e018c0f83c1351cc68ae5f3fcb5f4cf831c5f
Patch0:           0001-openssl-3.0.0-compatibility.patch
BuildRequires:    make gcc openssl-devel tpm2-tools tpm2-tss-devel tpm2-abrmd-devel
BuildRequires:    libyaml-devel libgcrypt-devel sqlite-devel autoconf-archive
BuildRequires:    python3 python3-cryptography python3-setuptools
BuildRequires:    python3-PyYAML python3-pyasn1-modules
BuildRequires:    python3-macros
BuildRequires:    cmocka dbus
Requires:         openssl tpm2-tools tpm2-tss tpm2-abrmd libyaml sqlite-libs
%description
OSS implementation of the TCG TPM2 PKCSv11 Software Stack

%package          tools
Summary:          The tools required to setup and configure TPM2 for PKCSv11
Requires:         %{name} = %{version}-%{release}
Requires:         python3
Requires:         python3-cryptography
Requires:         python3-setuptools
Requires:         python3-pyasn1-modules
Requires:         python3-PyYAML

%description tools
Tools for TCG TPM2 PKCSv11 Software Stack

%prep
%autosetup -p1 -n %{name}-%{version}
%build
./bootstrap
%configure --enable-unit
make %{?_smp_mflags} PACKAGE_VERSION=%{version}
cd tools
python3 setup.py build

%install
# make doesn't support _smp_mflags
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/pkgconfig/tpm2-pkcs11.pc
rm %{buildroot}%{_libdir}/libtpm2_pkcs11.la
cd tools
python3 setup.py install --root=%{buildroot} --optimize=1 --skip-build

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
make %{?_smp_mflags} check
cd tools
python3 setup.py test

%files
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/libtpm2_pkcs11.so
%{_libdir}/libtpm2_pkcs11.so.0*

%files tools
%defattr(-,root,root,-)
%{_bindir}/tpm2_ptool
%{python3_sitelib}/*

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 1.6.0-3
-   Bump up to compile with python 3.10
*   Thu Sep 02 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 1.6.0-2
-   openssl 3.0.0 compatibility
*   Sun Aug 8 2021 Vamsi Krishna Brahmajosyula <vbrahmajosyula@vmware.com> 1.6.0-1
-   Initial build. First version
