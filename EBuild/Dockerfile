FROM centos:6

# Update the image with the latest packages
# RUN yum update -y; yum clean all

# Install the 32-bit gcc development tools
RUN yum install -y glibc-devel.i686 libgcc.i686 libstdc++-devel.i686 ncurses-devel.i686 gcc gcc-c++ \
  && yum clean all

# Install some 64-bit development tools
RUN yum install -y glibc-devel.x86_64 && yum clean all

# Install RPM development tools
RUN yum install -y rpm-build rpmdevtools rpmlint hunspell-en && yum clean all

# Install tools required for building apcupsd
RUN yum install -y upstart sysvinit-tools man util-linux-ng && yum clean all

