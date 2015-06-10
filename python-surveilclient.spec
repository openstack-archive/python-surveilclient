Name:             python-surveilclient
Version:          0.7.0
Release:          1
Summary:          Python API and CLI for Surveil

Group:            Development/Languages
License:          ASL 2.0
URL:              https://github.com/stackforge/python-surveilclient
Source0:          http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python-setuptools
BuildRequires:    python-pbr

Requires:         python-requests
Requires:         python-prettytable
Requires:         python-oslo-serialization
Requires:         python-six

%description
This is a client for the Surveil API. There's a Python API (the
surveilclient module), and a command-line script (surveil).

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/surveil.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/surveil

%files
%{_bindir}/surveil
%{python_sitelib}/surveilclient
%{python_sitelib}/*.egg-info
%{_sysconfdir}/bash_completion.d
/usr/share/surveil.bash_completion

%changelog
* Wed Apr 01 2015 Alexandre Viau <alexandre@alexandreviau.net> 1:2.23.0-1
- Update to upstream 2.23.0
