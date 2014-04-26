*******************************
* Begin .SUBCKT model         *
* spice-sdb ver 4.28.2007     *
*******************************
.SUBCKT opamp741 Ip In Vee Vcc O2 
*==============  Begin SPICE netlist of main design ============
.model D1N4004 D(Bv=400 Ibv=5u M=.3333 Cjo=30p N=2 Is=18.8n)
D2 Vee O2 D1N4004 
D1 O2 Vcc D1N4004 
* begin vcvs expansion, e<name>
Eout O1 0 G2 0 1
Isense_Eout G2 0 dc 0
IOut_Eout O1 0 dc 0
* end vcvs expansion
* begin vcvs expansion, e<name>
Egain G1 0 Ip In 100k
Isense_Egain Ip In dc 0
IOut_Egain G1 0 dc 0
* end vcvs expansion
Cbw 0 G2 31.85nf  
Rout O1 O2 75  
Rbw G1 G2 0.5M  
Rin In Ip 2meg  
.ends opamp741
*******************************
