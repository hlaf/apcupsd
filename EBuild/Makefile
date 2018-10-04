
EBUILD_ROOT = $(CURDIR)
BUILD_ROOT = $(EBUILD_ROOT)/../BUILD/unix

#CC = /usr/bin/gcc44
#CXX = /usr/bin/g++44
CFLAGS = "-fPIC"

MAKE_OPTS = -j4 CC=$(CC) CXX=$(CXX) CFLAGS=$(CFLAGS) VERBOSE=true

VERBOSE = true
ifeq ($(VERBOSE),true)
	REDIRECT = 2>&1 | tee -a
else
	REDIRECT = &>
endif

POPD = popd >> /dev/null
VMAKE = $(MAKE)
BUILD = @$(VMAKE) VERBOSE=$(VERBOSE) build_cmd

Release  = FLAVOR=Release
Debug    = FLAVOR=Debug
Linux64  = PLAT=Linux64 CFG="--enable-64bit"
Linux32  = PLAT=Linux32 CFLAGS="-m32"
Macosx64 = PLAT=Macosx64 CFG="--enable-64bit"

#----------------------------------------------------------------------
# Global targets
#----------------------------------------------------------------------

all: Release Debug

Release: Release_Linux64 Release_Linux32 Release_Macosx64

Debug: Debug_Linux64 Debug_Linux32 Debug_Macosx64

Release_Linux64: prerequisites
	$(BUILD) $(Release) $(Linux64)

Release_Linux32: prerequisites
	$(BUILD) $(Release) $(Linux32)

Release_Macosx64: prerequisites
	$(BUILD) $(Release) $(Macosx64)

Release_Windows64: prerequisites
	@INSTALL_PATH=$$(cygpath -w $(EBUILD_ROOT)/Release_Windows64) && \
        LOG_FILE=$(EBUILD_ROOT)/Release_Windows64/buildlog.txt && \
        rm -rf $$INSTALL_PATH && \
        mkdir -p $$INSTALL_PATH && \
        module load visual_studio/2013 && \
        pushd $(BUILD_ROOT)/../win && \
        cmd /C "vcvarsall x64 && nmake -nologo -f makefile.vc release install MACHINE=AMD64 OPTS=threads INSTALLDIR=$$INSTALL_PATH" $(REDIRECT) $$LOG_FILE && \
        cp -r $(EBUILD_ROOT)/../BUILD $$INSTALL_PATH/src && \
        cp $${INSTALL_PATH}/lib/tcl86t.lib $${INSTALL_PATH}/lib/tcl86.lib

Release_Windows32: prerequisites
	@INSTALL_PATH=$$(cygpath -w $(EBUILD_ROOT)/Release_Windows32) && \
        LOG_FILE=$(EBUILD_ROOT)/Release_Windows32/buildlog.txt && \
        rm -rf $$INSTALL_PATH && \
        mkdir -p $$INSTALL_PATH && \
        module load visual_studio/2013 && \
        pushd $(BUILD_ROOT)/../win && \
        cmd /C "vcvarsall x86 && nmake -nologo -f makefile.vc release install OPTS=threads INSTALLDIR=$$INSTALL_PATH" $(REDIRECT) $$LOG_FILE

Debug_Windows32: prerequisites
	@INSTALL_PATH=$$(cygpath -w $(EBUILD_ROOT)/Debug_Windows32) && \
        LOG_FILE=$(EBUILD_ROOT)/Debug_Windows32/buildlog.txt && \
        rm -rf $$INSTALL_PATH && \
        mkdir -p $$INSTALL_PATH && \
        module load visual_studio/2013 && \
        pushd $(BUILD_ROOT)/../win && \
        cmd /C "vcvarsall x86 && nmake -nologo -f makefile.vc release install OPTS=threads,symbols INSTALLDIR=$$INSTALL_PATH" $(REDIRECT) $$LOG_FILE


clean:
	@$(call clean_cmd)

#----------------------------------------------------------------------
# Macros
#----------------------------------------------------------------------

build_cmd:
	@$(call clean_cmd)
	@$(call build_cmd)

define build_cmd
  INSTALL_PATH=$(EBUILD_ROOT)/$(FLAVOR)_$(PLAT) && \
  LOG_FILE=$${INSTALL_PATH}/buildlog.txt && \
  rm -rf $$INSTALL_PATH && \
  mkdir -p $$INSTALL_PATH && \
  pushd $(BUILD_ROOT) >> /dev/null && \
  ./configure --enable-threads --enable-shared $(CFG) \
    --prefix=$$INSTALL_PATH $(REDIRECT) $$LOG_FILE && \
  $(VMAKE) $(MAKE_OPTS) CFLAGS=$(CFLAGS) install $(REDIRECT) $$LOG_FILE
endef

define clean_cmd
  @pushd $(BUILD_ROOT) >> /dev/null && \
  if [ -f Makefile ]; then $(VMAKE) $(MAKE_OPTS) clean distclean; fi; \
  $(POPD)
endef

.PHONY=prerequisites
prerequisites:

