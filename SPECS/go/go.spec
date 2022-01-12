%global goroot          /usr/lib/golang
%global gopath          %{_datadir}/gocode
%ifarch aarch64
%global gohostarch      arm64
%else
%global gohostarch      amd64
%endif
%define debug_package %{nil}
%define __strip /bin/true

# rpmbuild magic to keep from having meta dependency on libc.so.6
#%%define _use_internal_dependency_generator 0
#%%define __find_requires %{nil}

Summary:        Go
Name:           go
Version:        1.13.15
Release:        1%{?dist}
License:        BSD
URL:            https://golang.org
Group:          System Environment/Security
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        https://dl.google.com/go/%{name}%{version}.src.tar.gz
%define sha1    go=54860ef92533677bb1366e6441716a77e5ec6f13

Requires:       glibc
%define ExtraBuildRequires go

%description
Go is an open source programming language that makes it easy to build simple, reliable, and efficient software.

%prep
%autosetup -p1 -n %{name}

%build
export GOHOSTOS=linux
export GOHOSTARCH=%{gohostarch}
export GOROOT_BOOTSTRAP=%{goroot}

export GOROOT="`pwd`"
export GOPATH=%{gopath}
export GOROOT_FINAL=%{_bindir}/go
rm -f  %{gopath}/src/runtime/*.c
pushd src
./make.bash --no-clean
popd

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{goroot}

cp -R api bin doc favicon.ico lib pkg robots.txt src misc VERSION %{buildroot}%{goroot}

# remove the unnecessary zoneinfo file (Go will always use the system one first)
rm -rfv %{buildroot}%{goroot}/lib/time

# remove the doc Makefile
rm -rfv %{buildroot}%{goroot}/doc/Makefile

# put binaries to bindir, linked to the arch we're building,
# leave the arch independent pieces in %{goroot}
mkdir -p %{buildroot}%{goroot}/bin/linux_%{gohostarch}
ln -sfv ../go %{buildroot}%{goroot}/bin/linux_%{gohostarch}/go
ln -sfv ../gofmt %{buildroot}%{goroot}/bin/linux_%{gohostarch}/gofmt
ln -sfv %{goroot}/bin/gofmt %{buildroot}%{_bindir}/gofmt
ln -sfv %{goroot}/bin/go %{buildroot}%{_bindir}/go

# ensure these exist and are owned
mkdir -p %{buildroot}%{gopath}/src/github.com/
mkdir -p %{buildroot}%{gopath}/src/bitbucket.org/
mkdir -p %{buildroot}%{gopath}/src/code.google.com/
mkdir -p %{buildroot}%{gopath}/src/code.google.com/p/

install -vdm755 %{buildroot}/etc/profile.d
cat >> %{buildroot}/etc/profile.d/go-exports.sh <<- "EOF"
export GOROOT=%{goroot}
export GOPATH=%{_datadir}/gocode
export GOHOSTOS=linux
export GOHOSTARCH=%{gohostarch}
export GOOS=linux
EOF

#chown -R root:root %{buildroot}/etc/profile.d/go-exports.sh
#%%{_fixperms} %{buildroot}/*

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  #This is uninstall
  rm /etc/profile.d/go-exports.sh
  rm -rf /opt/%{name}
  exit 0
fi

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%exclude %{goroot}/src/*.rc
%exclude %{goroot}/include/plan9
/etc/profile.d/go-exports.sh
%{goroot}/*
%{gopath}/src
%exclude %{goroot}/src/pkg/debug/dwarf/testdata
%exclude %{goroot}/src/pkg/debug/elf/testdata
%{_bindir}/*

%changelog
* Thu Sep 10 2020 Ashwin H <ashwinh@vmware.com> 1.13.15-1
- Update to 1.13.15
* Tue Aug 18 2020 Ashwin H <ashwinh@vmware.com> 1.11.13-5
- Fix CVE-2020-16845
* Thu Apr 23 2020 Harinadh Dommaraju <hdommaraju@vmware.com> 1.11.13-4
- Add patch for CVE-2020-7919
* Mon Jan 06 2020 Ashwin H <ashwinh@vmware.com> 1.11.13-3
- Add patch for CVE-2019-16276 CVE-2019-17596 which was missed
* Fri Jan 03 2020 Ashwin H <ashwinh@vmware.com> 1.11.13-2
- Fix CVE-2019-16276 and CVE-2019-17596
* Tue Aug 27 2019 Ashwin H <ashwinh@vmware.com> 1.11.13-1
- Update to  1.11.13
* Wed Apr 24 2019 Ashwin H <ashwinh@vmware.com> 1.11.9-1
- Upgrade to 1.11.9
* Mon Apr 02 2018 Dheeraj Shetty <dheerajs@vmware.com> 1.9.4-2
- Fix for CVE-2018-7187
* Thu Mar 15 2018 Xiaolin Li <xiaolinl@vmware.com> 1.9.4-1
- Update to golang release v1.9.4
* Mon Oct 23 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.9.1-1
- Update to golang release v1.9.1
* Thu Oct 19 2017 Xiaolin Li <xiaolinl@vmware.com> 1.8.1-2
- Fix CVE-2017-8932
* Tue Apr 11 2017 Danut Moraru <dmoraru@vmware.com> 1.8.1-1
- Update Golang to version 1.8.1, updated patch0
* Wed Dec 28 2016 Xiaolin Li <xiaolinl@vmware.com> 1.7.4-1
- Updated Golang to 1.7.4.
* Wed Jul 27 2016 Anish Swaminathan <anishs@vmware.com> 1.6.3-1
- Update Golang to version 1.6.3 - fixes CVE 2016-5386
* Fri Jul 8 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6.2-1
- Updated the Golang to version 1.6.2
* Thu Jun 2 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.4.2-5
- Fix script syntax
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.4.2-4
- GA - Bump release of all rpms
* Thu May 05 2016 Kumar Kaushik <kaushikk@vmware.com> 1.4.2-3
- Handling upgrade scenario pre/post/un scripts.
* Wed Dec 09 2015 Anish Swaminathan <anishs@vmware.com> 1.4.2-2
- Edit post script.
* Mon Aug 03 2015 Vinay Kulkarni <kulkarniv@vmware.com> 1.4.2-1
- Update to golang release version 1.4.2
* Fri Oct 17 2014 Divya Thaluru <dthaluru@vmware.com> 1.3.3-1
- Initial build.	First version
