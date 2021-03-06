#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-vishvananda-netns
Version  : 1fec6582c067519857603311ad090e23a5ca57de
Release  : 7
URL      : https://github.com/vishvananda/netns/archive/1fec6582c067519857603311ad090e23a5ca57de.tar.gz
Source0  : https://github.com/vishvananda/netns/archive/1fec6582c067519857603311ad090e23a5ca57de.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go

%description
# netns - network namespaces in go #
The netns package provides an ultra-simple interface for handling
network namespaces in go. Changing namespaces requires elevated
privileges, so in most cases this code needs to be run as root.

%prep
%setup -q -n netns-1fec6582c067519857603311ad090e23a5ca57de

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/vishvananda/netns"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/vishvananda/netns/netns.go
/usr/lib/golang/src/github.com/vishvananda/netns/netns_linux.go
/usr/lib/golang/src/github.com/vishvananda/netns/netns_test.go
/usr/lib/golang/src/github.com/vishvananda/netns/netns_unspecified.go
