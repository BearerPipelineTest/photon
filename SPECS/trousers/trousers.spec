Summary:        TCG Software Stack (TSS)
Name:           trousers
Version:        0.3.15
Release:        2%{?dist}
License:        BSD
URL:            https://sourceforge.net/projects/trousers/
Group:          System Environment/Security
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        %{name}-%{version}.tar.gz
%define sha512  %{name}=769c7d891c6306c1b3252448f86e3043ee837e566c9431f5b4353512113e2907f6ce29c91e8044c420025b79c5f3ff2396ddce93f73b1eb2a15ea1de89ac0fdb

Requires:       libtspi = %{version}-%{release}

%description
Trousers is an open-source TCG Software Stack (TSS), released under
the BSD License. Trousers aims to be compliant with the
1.1b and 1.2 TSS specifications available from the Trusted Computing

%package        devel
Summary:        The libraries and header files needed for TSS development.
Requires:       libtspi = %{version}-%{release}

%description    devel
The libraries and header files needed for TSS development.

%package -n     libtspi
Summary:        TSPI library

%description -n libtspi
TSPI library

%prep
%autosetup -p1

%build
sh bootstrap.sh
%configure --disable-static
%make_build

%install
%make_install %{?_smp_mflags}

%post
mkdir -p %{_sharedstatedir}/tpm
if [ $1 -eq 1 ]; then
  # this is initial installation
  if ! getent group tss >/dev/null; then
    groupadd tss
  fi
  if ! getent passwd tss >/dev/null; then
    useradd -c "TCG Software Stack" -d /var/lib/tpm -g tss -s /bin/false tss
  fi
fi

%postun
if [ $1 -eq 0 ]; then
  # this is delete operation
  if getent passwd tss >/dev/null; then
    userdel tss
  fi
  if getent group tss >/dev/null; then
    groupdel tss
  fi
fi

%post -n libtspi -p /sbin/ldconfig
%postun -n libtspi -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_sbindir}/*
%{_mandir}/man5
%{_mandir}/man8
%exclude %dir /var

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libtspi.la
%{_libdir}/libtspi.so
%{_libdir}/libtspi.so.1
%{_mandir}/man3

%files -n libtspi
%defattr(-,root,root)
%{_libdir}/libtspi.so.1.2.0
%exclude %dir %{_libdir}/debug
%exclude %{_libdir}/libtddl.a

%changelog
* Sun May 29 2022 Shreenidhi Shedi <sshedi@vmware.com> 0.3.15-2
- Fix binary path
* Tue Apr 19 2022 Gerrit Photon <photon-checkins@vmware.com> 0.3.15-1
- Automatic Version Bump
* Wed Aug 04 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 0.3.14-5
- Bump up release for openssl
* Thu Jan 14 2021 Alexey Makhalov <amakhalov@vmware.com> 0.3.14-4
- GCC-10 support.
* Wed Aug 19 2020 Shreyas B <shreyasb@vmware.com> 0.3.14-3
- Fix for CVE-2020-24330, CVE-2020-24331 & CVE-2020-24332
* Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 0.3.14-2
- Use standard configure macros
* Thu Mar 2 2017 Alexey Makhalov <amakhalov@vmware.com> 0.3.14-1
- Initial build. First version
