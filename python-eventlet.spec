%define module eventlet
Name:           python-%module
Version:        0.9.16
Release:        %mkrel 1
Summary:        Highly concurrent networking library
License:        MIT
Group:          Development/Python
URL:            http://eventlet.net
Source0:        http://pypi.python.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz
BuildRequires:  python-devel
Buildrequires:	python-setuptools
BuildRequires:  python-sphinx
Buildrequires:	python-greenlet
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       python-greenlet
Suggests:		python-pyzmq
BuildArch:      noarch

%description
Eventlet is a networking library written in Python. It achieves high
scalability by using non-blocking io while at the same time retaining
high programmer usability by using coroutines to make the non-blocking
io operations appear blocking at the source code level.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Python
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for the python-eventlet package.

%prep
%setup -q -n eventlet-%{version}

%build
CFLAGS="%{optflags}" python setup.py build
pushd doc 
make html && rm _build/html/.buildinfo
popd
chmod a-x tests/mock.py

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%files 
%defattr(-,root,root)
%doc AUTHORS LICENSE NEWS README README.twisted
%{python_sitelib}/*

%files doc
%defattr(-,root,root,-)
%doc doc/_build/html examples tests

