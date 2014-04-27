v 20110115 2
C 40000 40000 0 0 0 title-B.sym
C 44000 45400 1 0 0 resistor-1.sym
{
T 44300 45800 5 10 0 0 0 0 1
device=RESISTOR
T 44200 45700 5 10 1 1 0 0 1
refdes=R2
T 44200 45200 5 10 1 1 0 0 1
value=1k
}
C 43100 45400 1 0 0 resistor-1.sym
{
T 43400 45800 5 10 0 0 0 0 1
device=RESISTOR
T 43300 45700 5 10 1 1 0 0 1
refdes=R1
T 43300 45200 5 10 1 1 0 0 1
value=1k
}
C 40400 45600 1 0 0 gnd-1.sym
C 43000 45200 1 0 0 gnd-1.sym
N 40500 47100 44000 47100 4
{
T 42900 47100 5 10 1 1 0 0 1
netname=i
}
N 44000 47100 44000 46900 4
N 44000 46500 44000 45500 4
{
T 44000 46000 5 10 1 1 0 0 1
netname=fb1
}
N 44900 45500 45200 45500 4
N 45200 45500 45200 46700 4
{
T 45200 46200 5 10 1 1 0 0 1
netname=o1
}
N 45200 46700 45000 46700 4
C 47500 47000 1 0 0 vdc-1.sym
{
T 48200 47650 5 10 1 1 0 0 1
refdes=Vcc
T 48200 47850 5 10 0 0 0 0 1
device=VOLTAGE_SOURCE
T 48200 48050 5 10 0 0 0 0 1
footprint=none
T 48200 47450 5 10 1 1 0 0 1
value=DC 5V
}
C 47600 48200 1 0 0 vcc-1.sym
C 44000 46300 1 0 0 aop-spice-1.sym
{
T 45050 46450 5 8 0 0 0 0 1
device=AOP-Standard
T 44700 47100 5 10 1 1 0 0 1
refdes=X1
T 45000 47100 5 8 1 1 0 0 1
value=opamp741
}
C 44300 47100 1 0 0 vcc-1.sym
C 47500 45800 1 0 0 vdc-1.sym
{
T 48200 46450 5 10 1 1 0 0 1
refdes=Vee
T 48200 46650 5 10 0 0 0 0 1
device=VOLTAGE_SOURCE
T 48200 46850 5 10 0 0 0 0 1
footprint=none
T 48200 46250 5 10 1 1 0 0 1
value=DC 5V
}
C 48000 45800 1 180 0 vee-1.sym
C 44700 46300 1 180 0 vee-1.sym
C 47100 46700 1 0 0 gnd-1.sym
N 47800 47000 47200 47000 4
C 40800 49100 1 0 0 spice-include-1.sym
{
T 40900 49400 5 10 0 1 0 0 1
device=include
T 40900 49500 5 10 1 1 0 0 1
refdes=A1
T 41300 49200 5 10 1 1 0 0 1
file=opamp741.mod
}
C 40200 45900 1 0 0 vac-1.sym
{
T 40900 46550 5 10 1 1 0 0 1
refdes=Vin
T 40900 46750 5 10 0 0 0 0 1
device=vac
T 40900 46950 5 10 0 0 0 0 1
footprint=none
T 40900 46350 5 10 1 1 0 0 1
value=dc 0 ac 1
}