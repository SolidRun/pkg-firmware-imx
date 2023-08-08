#
# spec file for package firmware-imx6
#
# Copyright (c) 2014 Josua Mayer <josua@solid-run.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

%define blobpkg_name firmware-imx-3.14.28-1.0.0
%define blobpkg_md5 6e700f3d3a6482db08d5aabee7751630
%define blob_search_paths /home/abuild/rpmbuild/SOURCES ~

Name: firmware-imx6
Version: 2
Release: 1
License: MIT
Group: System/Base
Summary: Firmware blobs for i.MX6
Source: firmware-imx-%{version}.tar.gz
Source1: %{blobpkg_name}.bin

%description
Provides VPU and SDMA firmware for i.MX6 CPUs

%prep
%setup -q
chmod +x %{SOURCE1}
%{SOURCE1} --auto-accept --force

%build
# build imx6 sdma firmware
objcopy -Iihex -Obinary sdma-imx6q.bin.ihex sdma-imx6q.bin

%install
mkdir -p %{buildroot}/lib/firmware/vpu
mkdir -p %{buildroot}/lib/firmware/sdma
install -v -m644 %{blobpkg_name}/firmware/vpu/*.bin %{buildroot}/lib/firmware/vpu/
install -v -m644 %{blobpkg_name}/firmware/sdma/*.bin %{buildroot}/lib/firmware/sdma/
install -v -m644 sdma-imx6q.bin %{buildroot}/lib/firmware/sdma/

%files
%defattr(-,root,root)
%dir /lib/firmware
/lib/firmware/vpu
/lib/firmware/sdma
%doc %{blobpkg_name}/licenses/vpu/EULA

%changelog
