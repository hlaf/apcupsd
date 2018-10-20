
EBUILD_ROOT = $(CURDIR)
BUILD_ROOT = $(EBUILD_ROOT)/../BUILD

MAKE_OPTS = CC=$(CC) CXX=$(CXX) VERBOSE=1

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
Linux64  = PLAT=Linux64 CFG=""
Linux32  = PLAT=Linux32 CFLAGS="-m32" CXXFLAGS="-m32 -I$(BUILD_ROOT)/include" LDFLAGS="-m32"

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
  ./configure $(CFG) --enable-usb \
    $(REDIRECT) $$LOG_FILE && \
  $(VMAKE) $(MAKE_OPTS) \
    CFLAGS=$(CFLAGS) DESTDIR=$$INSTALL_PATH install $(REDIRECT) $$LOG_FILE
endef

define clean_cmd
  @pushd $(BUILD_ROOT) >> /dev/null && \
  if [ -f Makefile ]; then $(VMAKE) $(MAKE_OPTS) clean; fi; \
  $(POPD)
endef

.PHONY=prerequisites
prerequisites:

