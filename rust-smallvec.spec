%bcond_without check
%global debug_package %{nil}

%global crate smallvec

Name:           rust-%{crate}
Version:        1.6.1
Release:        1
Summary:        'Small vector' optimization: store up to a small number of items on the stack

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/smallvec
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
'Small vector' optimization: store up to a small number of items on the stack.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+may_dangle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+may_dangle-devel %{_description}

This package contains library source intended for building other packages
which use "may_dangle" feature of "%{crate}" crate.

%files       -n %{name}+may_dangle-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+specialization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+specialization-devel %{_description}

This package contains library source intended for building other packages
which use "specialization" feature of "%{crate}" crate.

%files       -n %{name}+specialization-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+union-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+union-devel %{_description}

This package contains library source intended for building other packages
which use "union" feature of "%{crate}" crate.

%files       -n %{name}+union-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+write-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+write-devel %{_description}

This package contains library source intended for building other packages
which use "write" feature of "%{crate}" crate.

%files       -n %{name}+write-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
