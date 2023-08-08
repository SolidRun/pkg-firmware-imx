%define blobpkg_name firmware-imx-3.10.17-1.0.0
%define blobpkg_md5 29a54f6e5bf889a00cd8ca85080af223
%define blob_search_paths /home/abuild/rpmbuild/SOURCES ~

Name: firmware-imx6
Version: 1
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

%changelog
