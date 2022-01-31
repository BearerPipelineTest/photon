Name:           bpftrace
Version:        0.11.1
Release:        3%{?dist}
Summary:        High-level tracing language for Linux eBPF
License:        ASL 2.0
Vendor:         VMware, Inc.
Distribution:   Photon
Group:          System Environment/Security

URL:            https://github.com/iovisor/bpftrace
Source0:        https://github.com/iovisor/bpftrace/archive/%{name}-%{version}.tar.gz
%define sha1    bpftrace=6bb8d682de04ffd47d565eb2542bc7c7d7b5da84

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  cmake
BuildRequires:  elfutils-libelf-devel
BuildRequires:  zlib-devel
BuildRequires:  llvm-devel
BuildRequires:  clang-devel
BuildRequires:  bcc-devel >= 0.16.0
BuildRequires:  libbpf-devel
BuildRequires:  binutils-devel

Requires:       bcc >= 0.16.0
Requires:       bcc-tools >= 0.16.0
Requires:       clang >= 10.0.1
Requires:       llvm >= 10.0.1
Requires:       zlib
Requires:       libbpf

%description
BPFtrace is a high-level tracing language for Linux enhanced Berkeley Packet
Filter (eBPF) available in recent Linux kernels (4.x). BPFtrace uses LLVM as a
backend to compile scripts to BPF-bytecode and makes use of BCC for
interacting with the Linux BPF system, as well as existing Linux tracing
capabilities: kernel dynamic tracing (kprobes), user-level dynamic tracing
(uprobes), and tracepoints. The BPFtrace language is inspired by awk and C,
and predecessor tracers such as DTrace and SystemTap

%prep
%autosetup -p1

%build
%cmake . \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DBUILD_TESTING:BOOL=OFF \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
        -DENABLE_TESTS:BOOL=OFF \
        -DBUILD_DEPS=OFF
%make_build

%install
%make_install

find %{buildroot}%{_datadir}/%{name}/tools -type f -exec \
  sed -i -e '1s=^#!/usr/bin/env %{name}\([0-9.]\+\)\?$=#!%{_bindir}/%{name}=' {} \;

%files
%doc README.md CONTRIBUTING-TOOLS.md
%doc docs/reference_guide.md docs/tutorial_one_liners.md
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tools
%dir %{_datadir}/%{name}/tools/doc
%{_bindir}/%{name}
%{_mandir}/man8/*
%attr(0755,-,-) %{_datadir}/%{name}/tools/*.bt
%{_datadir}/%{name}/tools/doc/*.txt

%changelog
* Mon Jan 24 2022 Ankit Jain <ankitja@vmware.com> 0.11.1-3
- Version Bump to build with new version of cmake
* Tue Jul 27 2021 Tapas Kundu <tkundu@vmware.com> 0.11.1-2
- Rebuild with updated clang
* Mon Jun 7 2021 Him Kalyan Bordoloi <bordoloih@vmware.com>  0.11.1-1
- Initial version
