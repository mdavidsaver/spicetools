v 20100214 2
C 40000 40000 0 0 0 title-B.sym
C 44400 45900 1 90 0 resistor-1.sym
{
T 44000 46200 5 10 0 0 90 0 1
device=RESISTOR
T 44100 46300 5 10 1 1 180 0 1
refdes=Rin
T 44400 46300 5 10 1 1 0 0 1
value=2meg
}
C 47000 46700 1 0 0 resistor-1.sym
{
T 47300 47100 5 10 0 0 0 0 1
device=RESISTOR
T 47200 47000 5 10 1 1 0 0 1
refdes=Rbw
T 47600 47000 5 10 1 1 0 0 1
value=0.5M
}
C 50100 46700 1 0 0 resistor-1.sym
{
T 50400 47100 5 10 0 0 0 0 1
device=RESISTOR
T 50200 47000 5 10 1 1 0 0 1
refdes=Rout
T 50700 47000 5 10 1 1 0 0 1
value=75
}
C 48100 45900 1 90 0 capacitor-1.sym
{
T 47400 46100 5 10 0 0 90 0 1
device=CAPACITOR
T 47800 46200 5 10 1 1 180 0 1
refdes=Cbw
T 47200 46100 5 10 0 0 90 0 1
symversion=0.1
T 47200 45800 5 10 1 1 0 0 1
value=31.85nf
}
C 45400 46100 1 0 0 vcvs-1.sym
{
T 45600 47150 5 10 0 0 0 0 1
device=SPICE-vcvs
T 46000 46950 5 10 1 1 0 0 1
refdes=Egain
T 45600 47350 5 10 0 0 0 0 1
symversion=0.1
T 46100 46050 5 10 1 0 0 5 1
value=100k
}
N 43600 46800 45400 46800 4
{
T 43900 46900 5 8 1 1 0 0 1
netname=Ip
}
N 43600 45900 45400 45900 4
{
T 44000 45900 5 8 1 1 0 0 1
netname=In
}
N 45400 45900 45400 46200 4
C 46900 45900 1 0 0 gnd-1.sym
C 48400 46100 1 0 0 vcvs-1.sym
{
T 48600 47150 5 10 0 0 0 0 1
device=SPICE-vcvs
T 49000 46950 5 10 1 1 0 0 1
refdes=Eout
T 48600 47350 5 10 0 0 0 0 1
symversion=0.1
T 49100 46050 5 10 1 0 0 5 1
value=1
}
N 48400 46800 47900 46800 4
{
T 48100 47000 5 8 1 1 0 0 1
netname=G2
}
C 47800 45600 1 0 0 gnd-1.sym
C 48300 45900 1 0 0 gnd-1.sym
N 46900 46800 47000 46800 4
{
T 46900 47000 5 8 1 1 0 0 1
netname=G1
}
N 46900 46200 47000 46200 4
N 50100 46800 49900 46800 4
{
T 49900 46900 5 8 1 1 0 0 1
netname=O1
}
N 51000 46800 51500 46800 4
{
T 51100 46600 5 8 1 1 0 0 1
netname=O2
}
C 49800 45900 1 0 0 gnd-1.sym
C 41900 49200 1 0 0 spice-subcircuit-LL-1.sym
{
T 42000 49500 5 10 0 1 0 0 1
device=spice-subcircuit-LL
T 42000 49600 5 10 1 1 0 0 1
refdes=A1
T 42000 49300 5 10 1 1 0 0 1
model-name=opamp741
}
C 43800 47100 1 180 0 spice-subcircuit-IO-1.sym
{
T 42900 46700 5 10 0 1 180 0 1
device=spice-IO
T 42950 46850 5 10 1 1 180 0 1
refdes=P1
}
C 43800 46200 1 180 0 spice-subcircuit-IO-1.sym
{
T 42900 45800 5 10 0 1 180 0 1
device=spice-IO
T 42950 45950 5 10 1 1 180 0 1
refdes=P2
}
C 51100 45500 1 180 0 spice-subcircuit-IO-1.sym
{
T 50200 45100 5 10 0 1 180 0 1
device=spice-IO
T 50250 45250 5 10 1 1 180 0 1
refdes=P3
}
C 51200 48700 1 180 0 spice-subcircuit-IO-1.sym
{
T 50300 48300 5 10 0 1 180 0 1
device=spice-IO
T 50350 48450 5 10 1 1 180 0 1
refdes=P4
}
C 51300 46500 1 0 0 spice-subcircuit-IO-1.sym
{
T 52200 46900 5 10 0 1 0 0 1
device=spice-IO
T 52150 46750 5 10 1 1 0 0 1
refdes=P5
}
C 43000 42500 1 0 0 aop-spice-1.sym
{
T 44050 42650 5 8 0 0 0 0 1
device=AOP-Standard
T 43700 43300 5 10 1 1 0 0 1
refdes=U?
T 43600 42900 5 8 0 1 0 0 1
graphical=1
}
T 50100 40800 9 8 1 0 0 0 1
Idealized opamp w/ approx response of lm741
T 42900 43700 9 8 1 0 0 0 1
Use with this symbol
C 51600 47500 1 90 0 diode-1.sym
{
T 51000 47900 5 10 0 0 90 0 1
device=DIODE
T 51100 48000 5 10 1 1 180 0 1
refdes=D1
T 51600 47800 5 8 1 1 0 0 1
value=D1N4004
}
C 51600 45200 1 90 0 diode-1.sym
{
T 51000 45600 5 10 0 0 90 0 1
device=DIODE
T 51100 45700 5 10 1 1 180 0 1
refdes=D2
T 51600 45500 5 8 1 1 0 0 1
value=D1N4004
}
N 51400 47500 51400 46800 4
N 51400 46800 51400 46100 4
N 50900 45200 51400 45200 4
{
T 51200 45000 5 8 1 1 0 0 1
netname=Vee
}
N 51000 48400 51400 48400 4
{
T 51200 48600 5 8 1 1 0 0 1
netname=Vcc
}
T 47100 47700 9 8 1 0 0 0 2
Low pass filter.
3db at 10Hz
C 41900 48400 1 0 0 spice-directive-1.sym
{
T 42000 48700 5 10 0 1 0 0 1
device=directive
T 42000 48800 5 10 1 1 0 0 1
refdes=A2
T 42000 48500 5 10 1 1 0 0 1
value=.model D1N4004 D(Bv=400 Ibv=5u M=.3333 Cjo=30p N=2 Is=18.8n)
}
