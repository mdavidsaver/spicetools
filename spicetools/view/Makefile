all: realall

PYUIC=pyuic4
PYRCC=pyrcc4

UIS = mainwin.ui

RCS = viewer.qrc

viewer_rc.py: icon.svg

realall: $(UIS:%.ui=ui_%.py)
realall: $(RCS:%.qrc=%_rc.py)

ui_%.py: %.ui
	$(PYUIC) -o $@ $<

%_rc.py: %.qrc
	$(PYRCC) -o $@ $<
