%global packagename nave

Name:           nodejs-%{packagename}
Version:        2.2.3
Release:        1
Summary:        Virtual Environments for Node
License:        ISC
URL:            https://github.com/isaacs/nave
Source0:        https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging

%description
%{summary}.

%prep
%setup -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json nave.sh \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%check
# TODO: Investigate: This package provides a shell script. Can it not be loaded by NodeJS?
# %{__nodejs} -e 'require("./")'

%files
%doc *.md example/
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Feb 3 2018 Christian Glombek <christian.glombek@rwth-aachen.de> - 2.2.3-1
- Initial RPM Spec
