# NOTE: this package is closely related to Sphinx version, so keep it in sync with sphinx-pdg.spec
# (4.13.0-4.14.x expect Sphinx 2, 4.15+ expect Sphinx 3)
#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Sphinx Doxygen renderer
Summary(pl.UTF-8):	Renderer Doxygena dla systemu dokumentacji Sphinx
Name:		python3-breathe
Version:	4.14.2
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/michaeljones/breathe/releases
Source0:	https://github.com/michaeljones/breathe/archive/v%{version}/breathe-%{version}.tar.gz
# Source0-md5:	6a97f52f443f5e30e2ecf7afa7f7132d
URL:		https://github.com/michaeljones/breathe
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 2.0
BuildRequires:	python3-docutils >= 0.12
BuildRequires:	python3-pytest
BuildRequires:	python3-six >= 1.9
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
Conflicts:	python3-Sphinx >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Breathe is an extension to reStructuredText and Sphinx to be able to
read and render the Doxygen XML output.

%description -l pl.UTF-8
Breathe to rozszerzenie do systemu dokumentacji reStructuredText i
Sphinx, pozwalające na odczyt i renderowanie wyjścia XML z Doxygena.

%prep
%setup -q -n breathe-%{version}

%build
%py3_build

%if %{with tests}
cd tests
PYTHONPATH=.. \
%{__python3} -m pytest -v
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/breathe-apidoc{,-3}
ln -sf breathe-apidoc-3 $RPM_BUILD_ROOT%{_bindir}/breathe-apidoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/breathe-apidoc
%attr(755,root,root) %{_bindir}/breathe-apidoc-3
%{py3_sitescriptdir}/breathe
%{py3_sitescriptdir}/breathe-%{version}-py*.egg-info
