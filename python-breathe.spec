#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx Doxygen renderer
Summary(pl.UTF-8):	Renderer Doxygena dla systemu dokumentacji Sphinx
Name:		python-breathe
Version:	1.0.0
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/michaeljones/breathe/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a1617f9cb555bbd618257d70e577909f
URL:		https://github.com/michaeljones/breathe
BuildRequires:	python >= 1:2.5
%if %{with python2}
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-Sphinx >= 1.0.7
Requires:	python-docutils >= 0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Breathe is an extension to reStructuredText and Sphinx to be able to
read and render the Doxygen XML output.

%description -l pl.UTF-8
Breathe to rozszerzenie do systemu dokumentacji reStructuredText i
Sphinx, pozwalające na odczyt i renderowanie wyjścia XML z Doxygena.

%package -n python3-breathe
Summary:	Sphinx Doxygen renderer
Summary(pl.UTF-8):	Renderer Doxygena dla systemu dokumentacji Sphinx
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-breathe
Breathe is an extension to reStructuredText and Sphinx to be able to
read and render the Doxygen XML output.

%description -n python3-breathe -l pl.UTF-8
Breathe to rozszerzenie do systemu dokumentacji reStructuredText i
Sphinx, pozwalające na odczyt i renderowanie wyjścia XML z Doxygena.

%prep
%setup -q -n breathe-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE README.rst
%{py_sitescriptdir}/breathe
%{py_sitescriptdir}/breathe-%{version}-py*.egg-info

%files -n python3-breathe
%defattr(644,root,root,755)
%doc LICENCE README.rst
%{py3_sitescriptdir}/breathe
%{py3_sitescriptdir}/breathe-%{version}-py*.egg-info
