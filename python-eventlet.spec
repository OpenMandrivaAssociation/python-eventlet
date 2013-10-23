%define module eventlet
Name:           python-%module
Version:        0.13.0
Release:        1
Summary:        Highly concurrent networking library
License:        MIT
Group:          Development/Python
URL:            http://eventlet.net
Source0:        http://pypi.python.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz
BuildRequires:  python-devel
Buildrequires:	python-setuptools
BuildRequires:  python-sphinx
Buildrequires:	python-greenlet
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
%{__python} setup.py install --root %{buildroot} --install-purelib=%{py_puresitedir}

%files 
%doc AUTHORS LICENSE NEWS README README.twisted
%{py_puresitedir}/*

%files doc
%defattr(-,root,root,-)
%doc doc/_build/html examples tests



%changelog
* Thu Jan 12 2012 Lev Givon <lev@mandriva.org> 0.9.16-1mdv2011.0
+ Revision: 760422
- Update to 0.9.16.
  Remove greenpipe patch (no longer needed).
  Suggest installation of python-pyzmq.

* Thu Jun 09 2011 Antoine Ginies <aginies@mandriva.com> 0.9.14-1
+ Revision: 683432
- fix group
- import python-eventlet


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.9.14
- first release for Mandriva

