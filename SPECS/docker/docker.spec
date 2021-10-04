%global security_hardening nopie
%define debug_package %{nil}
%define __os_install_post %{nil}
Summary:        Docker
Name:           docker
Version:        18.09.9
Release:        7%{?dist}
License:        ASL 2.0
URL:            http://docs.docker.com
Group:          Applications/File
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://github.com/docker/docker-ce/archive/%{name}-%{version}.tar.gz
%define sha1 docker=efe4cb8b60f888ab83776c84717a2b3078928bce
%define DOCKER_GITCOMMIT 039a7df9ba8097dd987370782fcdd6ea79b26016
Source99:       default-disable.preset
Patch98:        remove-firewalld.patch
Patch99:        update-container-binary.patch
Patch50:        containerd-CVE-2021-32760.patch
Patch51:        CVE-2021-41089.patch
Patch52:        containerd-CVE-2021-41103.patch

BuildRequires:  systemd
BuildRequires:  device-mapper-devel
BuildRequires:  btrfs-progs-devel
BuildRequires:  libseccomp
BuildRequires:  libseccomp-devel
BuildRequires:  libltdl-devel
BuildRequires:  libgcc-devel
BuildRequires:  glibc-devel
BuildRequires:  unzip
BuildRequires:  go
BuildRequires:  sed
BuildRequires:  cmake
BuildRequires:  findutils
BuildRequires:  git
Requires:       libltdl
Requires:       libgcc
Requires:       glibc
Requires:       libseccomp >= 2.4.0
Requires:       systemd
Requires:       device-mapper-libs
Requires:       shadow
Requires:       runc = 1.0.0.rc93

%description
Docker is an open source project to build, ship and run any application as a lightweight container.

%package        doc
Summary:        Documentation and vimfiles for docker
Requires:       %{name} = %{version}-%{release}

%description    doc
Documentation and vimfiles for docker

%prep
%setup -q

%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch98 -p1
%patch99 -p1

mkdir -p /go/src/github.com
cd /go/src/github.com
mkdir docker

ln -snrf "$OLDPWD/components/engine" docker/docker
ln -snrf "$OLDPWD/components/cli" docker/cli

%build
export GOPATH="/go"
export TMP_GOPATH="$GOPATH"
export PATH="$PATH:$GOPATH/bin"

GIT_COMMIT=%{DOCKER_GITCOMMIT}
GIT_COMMIT_SHORT=${GIT_COMMIT:0:7}

cd "$GOPATH/src/github.com/docker"

pushd cli
DISABLE_WARN_OUTSIDE_CONTAINER=1 make VERSION=%{version} GITCOMMIT=${GIT_COMMIT_SHORT} dynbinary manpages
popd

pushd docker
for component in tini "proxy dynamic" "containerd dynamic"; do
  hack/dockerfile/install/install.sh $component
done
DOCKER_BUILDTAGS="pkcs11 seccomp exclude_graphdriver_aufs" \
VERSION=%{version} DOCKER_GITCOMMIT=${GIT_COMMIT_SHORT} hack/make.sh dynbinary
popd

%install
export GOPATH="/go"
install -d -m755 %{buildroot}%{_mandir}/man1
install -d -m755 %{buildroot}%{_mandir}/man5
install -d -m755 %{buildroot}%{_mandir}/man8
install -d -m755 %{buildroot}%{_bindir}
install -d -m755 %{buildroot}%{_unitdir}
install -d -m755 %{buildroot}/lib/udev/rules.d
install -d -m755 %{buildroot}%{_datadir}/bash-completion/completions

# install binary
install -p -m 755 "$(readlink -f components/cli/build/docker)" %{buildroot}%{_bindir}/docker
install -p -m 755 "$(readlink -f components/engine/bundles/latest/dynbinary-daemon/dockerd)" %{buildroot}%{_bindir}/dockerd

# install proxy
install -p -m 755 /usr/local/bin/docker-proxy %{buildroot}%{_bindir}/docker-proxy

# install containerd
install -p -m 755 /usr/local/bin/containerd %{buildroot}%{_bindir}/containerd
install -p -m 755 /usr/local/bin/containerd-shim %{buildroot}%{_bindir}/containerd-shim
install -p -m 755 /usr/local/bin/ctr %{buildroot}%{_bindir}/ctr
# Explicitly install conatiner runtime service required by docker.service
install -p -m 644 $GOPATH/src/github.com/containerd/containerd/containerd.service %{buildroot}%{_unitdir}/containerd.service
sed -i 's#/usr/local/bin#/usr/bin#g' %{buildroot}%{_unitdir}/containerd.service

# install tini
install -p -m 755 /usr/local/bin/docker-init %{buildroot}%{_bindir}/docker-init

# install udev rules
install -p -m 644 components/engine/contrib/udev/80-docker.rules %{buildroot}/lib/udev/rules.d/80-docker.rules

# add init scripts
install -p -m 644 components/packaging/systemd/docker.service %{buildroot}%{_unitdir}/docker.service
install -p -m 644 components/packaging/systemd/docker.socket %{buildroot}%{_unitdir}/docker.socket

# add bash completions
install -p -m 644 components/cli/contrib/completion/bash/docker %{buildroot}%{_datadir}/bash-completion/completions/docker

# install manpages
install -p -m 644 components/cli/man/man1/*.1 %{buildroot}%{_mandir}/man1
install -p -m 644 components/cli/man/man5/*.5 %{buildroot}%{_mandir}/man5
install -p -m 644 components/cli/man/man8/*.8 %{buildroot}%{_mandir}/man8

# add vimfiles
install -d -m 755 %{buildroot}%{_datadir}/vim/vimfiles/doc
install -d -m 755 %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
install -d -m 755 %{buildroot}%{_datadir}/vim/vimfiles/syntax
install -p -m 644 components/engine/contrib/syntax/vim/doc/dockerfile.txt %{buildroot}%{_datadir}/vim/vimfiles/doc/dockerfile.txt
install -p -m 644 components/engine/contrib/syntax/vim/ftdetect/dockerfile.vim %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/dockerfile.vim
install -p -m 644 components/engine/contrib/syntax/vim/syntax/dockerfile.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/dockerfile.vim

mkdir -p build-docs
for engine_file in AUTHORS CHANGELOG.md CONTRIBUTING.md LICENSE MAINTAINERS NOTICE README.md; do
    cp "components/engine/$engine_file" "build-docs/engine-$engine_file"
done
for cli_file in LICENSE MAINTAINERS NOTICE README.md; do
    cp "components/cli/$cli_file" "build-docs/cli-$cli_file"
done

install -v -D -m 0644 %{SOURCE99} %{buildroot}%{_presetdir}/50-docker.preset

%preun
%systemd_preun docker.service
%systemd_preun containerd.service

%post
%systemd_post containerd.service
getent group docker >/dev/null || groupadd -r docker
%systemd_post docker.service

%postun
%systemd_postun_with_restart containerd.service
%systemd_postun_with_restart docker.service

if [ $1 -eq 0 ] ; then
    getent group docker >/dev/null && groupdel docker
fi

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_unitdir}/docker.service
%{_unitdir}/docker.socket
%{_unitdir}/containerd.service
%{_presetdir}/50-docker.preset
%{_bindir}/docker
%{_bindir}/dockerd
%{_bindir}/containerd
%{_bindir}/ctr
%{_bindir}/containerd-shim
%{_bindir}/docker-proxy
%{_bindir}/docker-init
%{_datadir}/bash-completion/completions/docker
/lib/udev/rules.d/80-docker.rules

%files doc
%defattr(-,root,root)
%doc build-docs/engine-AUTHORS build-docs/engine-CHANGELOG.md build-docs/engine-CONTRIBUTING.md build-docs/engine-LICENSE build-docs/engine-MAINTAINERS build-docs/engine-NOTICE build-docs/engine-README.md
%doc build-docs/cli-LICENSE build-docs/cli-MAINTAINERS build-docs/cli-NOTICE build-docs/cli-README.md
%doc
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_datadir}/vim/vimfiles/doc/dockerfile.txt
%{_datadir}/vim/vimfiles/ftdetect/dockerfile.vim
%{_datadir}/vim/vimfiles/syntax/dockerfile.vim

%changelog
*   Fri Oct 01 2021 Bo Gan <ganb@vmware.com> 18.09.9-7
-   Fix containerd CVE-2021-41103
*   Thu Sep 30 2021 Bo Gan <ganb@vmware.com> 18.09.9-6
-   Fix CVE-2021-41089
*   Fri Jul 16 2021 Bo Gan <ganb@vmware.com> 18.09.9-5
-   Fix containerd CVE-2021-32760
*   Fri May 14 2021 Bo Gan <ganb@vmware.com> 18.09.9-4
-   Update bundled containerd to 1.4.4
-   Require v1.0.0-rc93 version of runc (requested by containerd)
*   Fri Apr 24 2020 Harinadh D <hdommaraju@vmware.com> 18.09.9-3
-   Add docker to group during install and upgrade if not exists
*   Fri Apr 24 2020 Harinadh D <hdommaraju@vmware.com> 18.09.9-2
-   Bump up version to compile with new go version
*   Tue Apr 21 2020 Ankit Jain <ankitja@vmware.com> 18.09.9-1
-   Update to 18.09.9
-   Fixed CVE-2019-16884 by upgrading containerd version and runc
*   Fri Jan 03 2020 Ashwin H <ashwinh@vmware.com> 18.03.0-8
-   Bump up version to compile with new go
*   Mon Nov 25 2019 Ashwin H <ashwinh@vmware.com> 18.03.0-7
-   Fix CVE-2019-14271
*   Fri Aug 30 2019 Ashwin H <ashwinh@vmware.com> 18.03.0-6
-   Bump up version to compile with new go
*   Tue Jun 4 2019 Bo Gan <ganb@vmware.com> 18.03.0-5
-   Fix CVE-2018-15664
*   Thu Feb 14 2019 Bo Gan <ganb@vmware.com> 18.03.0-4
-   Fix docker version string
*   Mon Feb 11 2019 Him Kalyan Bordoloi <bordoloih@vmware.com> 18.03.0-3
-   Patch to fix CVE-2019-5736
*   Fri Sep 07 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 18.03.0-2
-   Fix apparmor not being applied to exec processes
*   Mon Apr 09 2018 Bo Gan <ganb@vmware.com> 18.03.0-1
-   Update to 18.03.0-ce
*   Mon Apr 09 2018 Bo Gan <ganb@vmware.com> 17.12.1-1
-   Update to 17.12.1-ce
*   Mon Apr 09 2018 Bo Gan <ganb@vmware.com> 17.09.1-1
-   Update to 17.09.1-ce
*   Mon Jan 15 2018 Bo Gan <ganb@vmware.com> 17.06.0-3
-   disable docker service by default
-   Fix post scriptlet to invoke systemd_post
*   Thu Dec 21 2017 Kumar Kaushik <kaushikk@vmware.com> 17.06.0-2
-   Applying patch for CVE-2017-14992
*   Tue Jul 18 2017 Bo Gan <ganb@vmware.com> 17.06.0-1
-   Update to 17.06.0-ce
*   Mon Jul 10 2017 Bo Gan <ganb@vmware.com> 1.13.1-4
-   Fix runc/containerd/libnetwork versions
-   Do not strip binaries
*   Thu May 04 2017 Kumar Kaushik <kaushikk@vmware.com> 1.13.1-3
-   Docker build requires GO.
*   Wed May 03 2017 Kumar Kaushik <kaushikk@vmware.com> 1.13.1-2
-   Fixing docker plugin runc version github issue # 640.
-   Adding docker group for non-sudo users, GitHub issue # 207.
*   Tue Apr 11 2017 Kumar Kaushik <kaushikk@vmware.com> 1.13.1-1
-   Building docker from source.
*   Fri Jan 13 2017 Xiaolin Li <xiaolinl@vmware.com> 1.12.6-1
-   Upgraded to version 1.12.6
*   Wed Sep 21 2016 Xiaolin Li <xiaolinl@vmware.com> 1.12.1-1
-   Upgraded to version 1.12.1
*   Mon Aug 22 2016 Alexey Makhalov <amakhalov@vmware.com> 1.12.0-2
-   Added bash completion file
*   Tue Aug 09 2016 Anish Swaminathan <anishs@vmware.com> 1.12.0-1
-   Upgraded to version 1.12.0
*   Tue Jun 28 2016 Anish Swaminathan <anishs@vmware.com> 1.11.2-1
-   Upgraded to version 1.11.2
*   Thu May 26 2016 Divya Thaluru <dthaluru@vmware.com>  1.11.0-6
-   Fixed logic to restart the active services after upgrade 
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.11.0-5
-   GA - Bump release of all rpms
*   Tue May 10 2016 Anish Swaminathan <anishs@vmware.com> 1.11.0-4
-   Remove commented post actions
*   Tue May 3 2016 Divya Thaluru <dthaluru@vmware.com>  1.11.0-3
-   Fixing spec file to handle rpm upgrade scenario correctly
*   Sat Apr 30 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.11.0-2
-   Add $DOCKER_OPTS to start in docker.service
*   Fri Apr 15 2016 Anish Swaminathan <anishs@vmware.com> 1.11.0-1
-   Updated to version 1.11.0.
*   Tue Feb 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.10.2-1
-   Upgraded to version 1.10.2
*   Thu Dec 10 2015 Xiaolin Li <xiaolinl@vmware.com>  1.9.0-2
-   Add systemd to Requires and BuildRequires.
-   Use systemctl to enable/disable service.
*   Fri Nov 06 2015 Vinay Kulkarni <kulkarniv@vmware.com> 1.9.0-1
-   Update to version 1.9.0
*   Mon Aug 17 2015 Divya Thaluru <dthaluru@vmware.com> 1.8.1-1
-   Update to new version 1.8.1.
*   Fri Jun 19 2015 Fabio Rapposelli <fabio@vmware.com> 1.7.0-1
-   Update to new version.
*   Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> 1.6.0-3
-   Update according to UsrMove.
*   Fri May 15 2015 Divya Thaluru <dthaluru@vmware.com> 1.6.0-2
-   Updated to version 1.6
*   Wed Mar 4 2015 Divya Thaluru <dthaluru@vmware.com> 1.5.0-1
-   Initial build. First version
