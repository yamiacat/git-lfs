#global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%define gem_name hpricot
Name:           rubygem-%{gem_name}
Version:        0.8.6
Release:	1%{?dist}
Summary:        a swift, liberal HTML parser with a fantastic library

Group:          Applications/Programming
License:        N/A
URL:		https://rubygems.org/gems/%{gem_name}
Source0:	https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot:      %(echo %{_topdir}/BUILDROOT/%{gem_name}-%{version})
BuildRequires:	gem
Requires:       ruby

%description
a swift, liberal HTML parser with a fantastic library

%prep
%setup -q -n %{gem_name}-%{version}
%if ! 0%{?el8}
gem install -V --local --force --install-dir ./%{gemdir} %{SOURCE0}
%endif
#mv ./%{gemdir}/bin ./usr/local

%build
%if 0%{?el8}
gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%endif

%install
mkdir -p ${RPM_BUILD_ROOT}
cp -a ./usr ${RPM_BUILD_ROOT}/usr

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%if 0%{?el8}
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems
%else
%{gemdir}
%endif

%changelog
* Wed May 20 2015 Andrew Neff <andyneff@users.noreply.github.com> - 2.1.8
- Initial Spec
