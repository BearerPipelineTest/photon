%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name kubeclient

Name:           rubygem-kubeclient
Version:        4.9.1
Release:        2%{?dist}
Summary:        A client for Kubernetes REST api.
Group:          Development/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
License:        MIT
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha1    kubeclient=e31c1604d94bfd5a7112624965b71e7821692825
BuildRequires:  ruby >= 2.0.0
BuildRequires:  findutils
Requires:       rubygem-activesupport
Requires:       rubygem-http >= 3.0, rubygem-http < 5.0
Requires:       rubygem-recursive-open-struct > 1.1
Requires:       rubygem-rest-client
BuildArch:      noarch

%description
A client for Kubernetes REST api.

%prep
%autosetup -n %{gem_name}-%{version}

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}
[ -d %{buildroot}/usr/lib ] && find %{buildroot}/usr/lib -type f -perm /022 -exec chmod go-w {} \;

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Thu Oct 14 2021 Stanislav Hadjiiski <hadjiiskis@vmware.com> 4.9.1-2
-   Drop group write permissions for files in /usr/lib to comply with STIG
*   Mon Sep 21 2020 Gerrit Photon <photon-checkins@vmware.com> 4.9.1-1
-   Automatic Version Bump
*   Wed Sep 02 2020 Sujay G <gsujay@vmware.com> 1.1.4-2
-   Rebuilt with ruby-2.7.1
*   Thu Aug 22 2019 Stanislav Hadjiiski <hadjiiskis@vmware.com> 1.1.4-1
-   Initial build
