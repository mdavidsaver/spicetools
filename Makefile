all: realall

PYUIC=pyuic4
PYRCC=pyrcc4

UICFLAGS += --from-imports

UIS += spicetools/bench/simwin.ui
UIS += spicetools/bench/fileframe.ui
UIS += spicetools/bench/expr.ui
UIS += spicetools/bench/analysis.ui
UIS += spicetools/view/mainwin.ui
UIS += spicetools/log/logwin.ui

RCS += spicetools/bench/bench.qrc
RCS += spicetools/view/viewer.qrc

GEN_UIS = $(UIS:%.ui=%_ui.py)
GEN_RCS = $(RCS:%.qrc=%_rc.py)

realall: $(GEN_UIS) $(GEN_RCS)

clean:
	rm -f $(GEN_UIS)
	rm -f $(GEN_RCS)

%_ui.py: %.ui
	$(PYUIC) $(UICFLAGS) -o $@ $<

%_rc.py: %.qrc
	$(PYRCC) $(RCCFLAGS) -o $@ $<
