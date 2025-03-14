# NOTE: this package is closely related to Sphinx version, so keep it in sync with sphinx-pdg.spec
#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Sphinx Doxygen renderer
Summary(pl.UTF-8):	Renderer Doxygena dla systemu dokumentacji Sphinx
Name:		python3-breathe
Version:	4.35.0
Release:	3
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/michaeljones/breathe/releases
Source0:	https://github.com/michaeljones/breathe/archive/v%{version}/breathe-%{version}.tar.gz
# Source0-md5:	06bddf761f69fafb684238a656955fe6
URL:		https://github.com/michaeljones/breathe
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 4.0
BuildRequires:	python3-Sphinx
BuildRequires:	python3-docutils >= 0.12
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-Sphinx >= 3
Requires:	python3-modules >= 1:3.6
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
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
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
