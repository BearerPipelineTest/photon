%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name nokogiri

Summary:        Nokogiri is an HTML, XML, SAX, and Reader parser.
Name:           rubygem-nokogiri
Version:        1.12.5
Release:        1%{?dist}
License:        MIT
Group:          Development/Languages
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/nokogiri/
Source0:        https://rubygems.org/downloads/nokogiri-%{version}.gem
%define sha1    nokogiri=a290767b2fe1c9e233c8dd93bb0da86754c9292e
BuildRequires:  ruby >= 2.4.0
BuildRequires:  rubygem-mini_portile2
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
Requires:       ruby >= 2.4.0
Requires:       rubygem-mini_portile2
Requires:       libxml2
Requires:       libxslt
%description
Nokogiri is an HTML, XML, SAX, and Reader parser. Among Nokogiri's many features is the ability to search documents via XPath or CSS3 selectors.
%prep
%autosetup -c

%build

%install
NOKOGIRI_USE_SYSTEM_LIBRARIES=1 gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Fri Nov 5 2021 Sujay G <gsujay@vmware.com> 1.12.5-1
-   Bump version to 1.12.5 to fix CVE-2021-41098, CVE-2020-26247. CVE-2019-5477
*   Mon Feb 4 2019 Sujay G <gsujay@vmware.com> 1.7.1-3
-   Increment the release version as part of ruby upgrade
*   Thu Apr 13 2017 Siju Maliakkal <smaliakkal@vmware.com> 1.7.1-2
-   Change ruby version in buildrequires and requires
*   Wed Mar 22 2017 Xiaolin Li <xiaolinl@vmware.com> 1.7.1-1
-   Updated to version 1.7.1.
*   Wed Jan 25 2017 Anish Swaminathan <anishs@vmware.com> 1.6.7.2-4
-   Bump up release number to reflect ruby upgrade
*   Thu Oct 27 2016 Anish Swaminathan <anishs@vmware.com> 1.6.7.2-3
-   Use SYSTEM_LIBRARIES for nokogiri
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.6.7.2-2
-   GA - Bump release of all rpms
*   Wed Jan 20 2016 Anish Swaminathan <anishs@vmware.com> 1.6.7.2-1
-   Upgrade version.
*   Wed Nov 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6.6.2-1
-   Initial build

