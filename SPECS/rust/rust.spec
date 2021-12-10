Summary:        Rust Programming Language
Name:           rust
Version:        1.56.0
Release:        3%{?dist}
License:        Apache License Version 2.0 and MIT
URL:            https://github.com/rust-lang/rust
Group:          Applications/System
Vendor:         VMware, Inc.
Distribution:   Photon
# Manually created Source tar which is equal to
# Source0 + .git as it requires git hooks at build time
Source0:        https://github.com/rust-lang/rust/archive/%{name}-%{version}.tar.gz
%define sha1    %{name}-%{version}=f89514bc0d7ffda0d20552ce1a72b9ff5f3f5a4d
Patch0:         CVE-2021-42574.patch
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  glibc
BuildRequires:  binutils
BuildRequires:  python3
BuildRequires:  curl-devel
BuildRequires:  ninja-build
BuildRequires:  photon-release

%description
Rust Programming Language

%prep
%autosetup -p1

%build
sh ./configure --prefix=%{_prefix} --enable-extended --tools="cargo"
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot}%{_libdir} -maxdepth 1 -type f -name '*.so' -exec chmod -v +x '{}' '+'
rm %{buildroot}%{_docdir}/%{name}/html/.lock
rm %{buildroot}%{_docdir}/%{name}/*.old

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc CONTRIBUTING.md README.md RELEASES.md
%{_bindir}/rustc
%{_bindir}/rustdoc
%{_bindir}/rust-lldb
%{_mandir}/man1/*
%{_libdir}/lib*.so
%{_libdir}/rustlib/*
%{_libexecdir}/cargo-credential-1password
%{_bindir}/rust-gdb
%{_bindir}/rust-gdbgui
%doc %{_docdir}/%{name}/html/*
%exclude %{_docdir}/%{name}/html/.stamp
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/COPYRIGHT
%doc %{_docdir}/%{name}/LICENSE-APACHE
%doc %{_docdir}/%{name}/LICENSE-MIT
%doc src/tools/rustfmt/{README,CHANGELOG,Configurations}.md
%doc src/tools/clippy/{README.md,CHANGELOG.md}
%{_bindir}/cargo
%{_datadir}/zsh/*
%doc %{_docdir}/%{name}/LICENSE-THIRD-PARTY
%{_sysconfdir}/bash_completion.d/cargo

%changelog
*   Thu Dec 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 1.56.0-3
-   Bump up to compile with python 3.10
*   Mon Nov 08 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 1.56.0-2
-   bump up for openssl
*   Thu Oct 28 2021 Ankit Jain <ankitja@vmware.com> 1.56.0-1
-   Updated to 1.56.0 and fix CVE-2021-42574
*   Sat Aug 28 2021 Ankit Jain <ankitja@vmware.com> 1.54.0-1
-   Updated to 1.54.0
*   Mon Aug 23 2021 Ankit Jain <ankitja@vmware.com> 1.51.0-4
-   Fixes CVE-2021-29922
*   Tue May 04 2021 Ankit Jain <ankitja@vmware.com> 1.51.0-3
-   Fixes CVE-2020-36323
*   Wed Apr 28 2021 Ankit Jain <ankitja@vmware.com> 1.51.0-2
-   Fixes CVE-2021-28876,CVE-2021-28878,CVE-2021-28879
*   Mon Apr 19 2021 Ankit Jain <ankitja@vmware.com> 1.51.0-1
-   Update to latest version to fix CVE-2021-31162
*   Wed Sep 02 2020 Gerrit Photon <photon-checkins@vmware.com> 1.46.0-1
-   Automatic Version Bump
*   Thu Aug 13 2020 Ankit Jain <ankitja@vmware.com> 1.45.2-1
-   Updated to 1.45.2
*   Tue Jun 23 2020 Tapas Kundu <tkundu@vmware.com> 1.34.2-3
-   Build with python3
-   Mass removal python2
*   Thu Oct 24 2019 Ankit Jain <ankitja@vmware.com> 1.34.2-2
-   Added for ARM Build
*   Wed May 15 2019 Ankit Jain <ankitja@vmware.com> 1.34.2-1
-   Initial build. First version
