%define module eventlet
# sphinxcontrib-apidoc is not built for Python 3.15
%bcond docs 0

Name:		python-eventlet
Version:	0.41.2
Release:	1
Summary:	Highly concurrent networking library
License:	MIT
Group:		Development/Python
URL:		https://eventlet.net
Source0:	https://pypi.python.org/packages/source/e/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(greenlet)
BuildRequires:	python%{pyver}dist(dnspython)
%if %{with docs}
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphinxcontrib-apidoc)
BuildRequires:	python%{pyver}dist(pyzmq)
%endif

%description
Eventlet is a networking library written in Python. It achieves high
scalability by using non-blocking io while at the same time retaining
high programmer usability by using coroutines to make the non-blocking
io operations appear blocking at the source code level.

%if %{with docs}
%package doc
Summary:	Documentation for %{name}
Group:	Development/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for the python-eventlet package.
%endif

%build -p
export CFLAGS="%{optflags}"
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%install -a
%if %{with docs}
# Use sphinx-build to build html docs into buildroot docdir,
# Doc generation requires the module to be installed in order to run successfully.
PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}" \
    sphinx-build -b html doc/source %{buildroot}%{_docdir}/%{name}-doc/html
# remove .buildinfo and .doctrees
rm -rf %{buildroot}%{_docdir}/%{name}-doc/html/{.buildinfo,.doctrees}
%endif


%files
%doc AUTHORS NEWS README.rst
%license LICENSE
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info

%if %{with docs}
%files doc
%doc examples tests
%{_docdir}/%{name}-doc/html
%endif
