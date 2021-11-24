%define git 20211002
%define oname cursor-themes

%define  _name  cutefish
Name:           cutefish-cursor-themes
Version:        0
Release:        0.%{git}.1
Summary:        Cutefish Desktop Cursors Theme
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/cutefishos/cursor-themes
Source:         https://github.com/cutefishos/cursor-themes/archive/refs/heads/cursor-themes-master.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
#equires:       gtk3-tools
BuildArch:      noarch

%description
Dark and Light cursors for Cutefish Desktop

%prep
%autosetup -n %{oname}-master

%build

%install
install -dm 0755 %{buildroot}%{_datadir}/icons/
cp -a %{_name}-light %{buildroot}%{_datadir}/icons/
cp -a %{_name}-dark %{buildroot}%{_datadir}/icons/
find %{buildroot}%{_datadir}/icons -type f -exec chmod 0644 {} \;
find -L %{buildroot}%{_datadir}/icons -type l -delete -print

%fdupes -s %{buildroot}%{_datadir}/icons/

%files
%doc README.md
%{_datadir}/icons/%{_name}*/
