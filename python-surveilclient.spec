Name:             python-surveilclient
Epoch:            1
Version:          0.6.0
Release:          1%{?dist}
Summary:          Python API and CLI for Surveil

Group:            Development/Languages
License:          ASL 2.0
URL:              http://pypi.python.org/pypi/%{name}
Source0:          http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-d2to1
BuildRequires:    python-pbr

Requires:         python-argparse
Requires:         python-iso8601
Requires:         python-oslo-i18n
Requires:         python-oslo-serialization
Requires:         python-oslo-utils
Requires:         python-prettytable
Requires:         python-requests
Requires:         python-simplejson
Requires:         python-six
Requires:         python-babel
Requires:         python-keystoneclient
Requires:         python-keyring
Requires:         python-setuptools
Requires:         python-pbr
Requires:         python-netifaces

%description
This is a client for the Surveil API. There's a Python API (the
surveilclient module), and a command-line script (surveil).

%prep
%setup -q

# Remove bundled egg-info
rm -rf python_novaclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/nova.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/nova

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/novaclient/tests
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man

install -p -D -m 644 man/nova.1 %{buildroot}%{_mandir}/man1/nova.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%{_bindir}/nova
%{python2_sitelib}/novaclient
%{python2_sitelib}/*.egg-info
%{_sysconfdir}/bash_completion.d
%{_mandir}/man1/nova.1.gz

%files doc
%doc html

%changelog
* Wed Apr 01 2015 Haikel Guemar <hguemar@fedoraproject.org> 1:2.23.0-1
- Update to upstream 2.23.0
