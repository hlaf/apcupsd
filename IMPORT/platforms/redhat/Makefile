topdir:=../..

SUBDIRS =
include $(topdir)/autoconf/targets.mak

all-install: install-redhat
all-uninstall: uninstall-redhat

install-redhat:
	$(call DISTINST,RedHat)
   # unlink old rc script (if not doing a DESTDIR install)
	$(call CHKCFG,del,/etc/rc.d/init.d/apcupsd)
   # install new rc script
	$(call MKDIR,/etc/rc.d/init.d)
	$(call INSTDATA,744,apcupsd,/etc/rc.d/init.d)
   # link new rc script (if not doing a DESTDIR install)
	$(call CHKCFG,add,/etc/rc.d/init.d/apcupsd)
	$(V)if cp -fR /etc/rc.d/init.d/halt $(DESTDIR)/etc/rc.d/init.d/halt.old  && \
          awk -f awkhaltprog $(DESTDIR)/etc/rc.d/init.d/halt.old >$(DESTDIR)/etc/rc.d/init.d/halt && \
          chmod 744 $(DESTDIR)/etc/rc.d/init.d/halt ; then true ; else \
      echo "================================================="; \
      echo "WARNING: UNABLE TO UPDATE /etc/rc.d/init.d/halt" ;  \
      echo "You must manually arrange for killpower during OS shutdown." ; \
      echo "================================================="; \
   fi
	@echo "================================================="
	@echo " "
	@echo "apcupsd script installation for RedHat $(DISTVER) complete." 
	@echo " "
	@echo "You should now edit  /etc/apcupsd/apcupsd.conf  to correspond"
	@echo "to your setup then start the apcupsd daemon with:"
	@echo " "
	@echo "/etc/rc.d/init.d/apcupsd start"
	@echo " "
	@echo "thereafter when you reboot, it will be stopped and started"
	@echo "automatically."
	@echo " "
	@echo "Please check that your halt script in:"
	@echo "    /etc/rc.d/init.d/halt"
	@echo "was properly updated (see installation section of manual)"
	@echo " "
	@echo "================================================="

uninstall-redhat:
	$(call DISTUNINST,RedHat)
   # unlink old rc script (if not doing a DESTDIR install)
	-$(call CHKCFG,del,/etc/rc.d/init.d/apcupsd)
	-$(call UNINST,/etc/rc.d/init.d/apcupsd)
	-$(call COPY,$(DESTDIR)/etc/rc.d/init.d/halt.old,/etc/rc.d/init.d/halt)
	-$(call UNINST,/etc/rc.d/init.d/halt.old)

