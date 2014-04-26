all: realall

PYUIC=pyuic4
PYRCC=pyrcc4

UIS += simwin.ui
UIS += fileframe.ui
UIS += expr.ui
UIS += analysis.ui

realall: $(UIS:%.ui=ui_%.py)
realall: $(RCS:%.qrc=%_rc.py)

ui_%.py: %.ui
	$(PYUIC) -o $@ $<

%_rc.py: %.qrc
	$(PYRCC) -o $@ $<
