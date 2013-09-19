#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Sphinx Doxygen renderer
Summary(pl.UTF-8):	Renderer Doxygena dla systemu dokumentacji Sphinx
# Name must match the python module/package name (as in 'import' statement)
Name:		python-breathe
Version:	1.0.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/michaeljones/breathe/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	a1617f9cb555bbd618257d70e577909f
URL:		https://github.com/michaeljones/breathe
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

%prep
%setup -q -n breathe-%{version}

%build
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE README.rst
%{py_sitescriptdir}/breathe
%{py_sitescriptdir}/breathe-%{version}-py*.egg-info
