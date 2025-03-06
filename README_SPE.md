##################################################################################
# SPE paper - A comprehensive review of ns-3-based simulator: Hypatia and ns-3-leo
##################################################################################

LEO satellite constellations are redefining the concept of global connectivity, opening up a new world of op-
portunities for communication services and applications. The emergence of LEO satellites is ushering in a
new era of innovation, where new complex technologies are being developed, and the use of appropriate sim-
ulation environments is an essential part of this. LEO constellations promise low-latency, high-bandwidth
Internet but require robust simulation tools due to their dynamic nature and the integration of numerous ter-
restrial and space nodes. 

In this paper, we review ns-3-based simulation frameworks widely referenced in
relevant research work in the field of LEO constellation communications. We provide a technical overview,
highlighting strengths and limitations, and offering valuable knowledge of the overall simulation tools for
researchers focusing on high-level end-to-end communication aspects over LEO constellations.


In this work, Hypatia and ns-3-leo simulators are used.

-------------
Hypatia
-------------

Hypatia was presented in:

Kassing S, Bhattacherjee D, Águas A, Saethre J, Singla A. Exploring the "Internet from space" with Hypatia. In: Proceedings of the ACM Internet Measurement Conference. 2020:214-229. doi: 10.1145/3419394.3423635

Instructions to install, build and run Hypatia can be read in README.md file in this directory
https://github.com/snkas/hypatia can also be consulted

Simulations using Hypatia includes the following steps:

* Step 1 ---> use satgenpy to generate satellite network dynamic state over time
Instructions can be found in <hypatia>/paper/satellite_networks_state/README.md
Also, read  <hypatia>/satgenpy/SPE_results/README_SPE_results.md 

* Step 2 ---> build ns-3 simulator
Instructions can be found in `<hypatia>/ns3-sat-sim/README.md`
It is recommended to build de debug version:
>> sudo bash build.sh --debug_all

* Step 3 ---> running ns-3 experiments
Instructions can be found in `<hypatia>/paper/ns3_experiments/README.md` 
Also, read <hypatia>/paper/satellite_network_state/gen_data/README_SPE_results.md
Also, read <hypatia>/paper/ns3_experiments/a_b/SPE_results/README_SPE_results.md

-------------
ns-3-leo
-------------

ns-3-leo was presented in: 

Schubert T, Wolf L, Kulau U. ns-3-leo: Evaluation Tool for Satellite Swarm Communication Protocols. IEEE Access. 2022;10:11527-11537. doi:
10.1109/ACCESS.2022.3146770

ns-3-leo simulator is implemented as a module of ns3, available at https://gitlab.ibr.cs.tu-bs.de/tschuber/ns-3-leo
The path to the ns-3-leo code is:
<hypatia>/ns3-sat-sim/simulator/contrib/leo
Read <hypatia>/ns3-sat-sim/simulator/contrib/leo/README_SPE.md

Simulations using ns-3-leo includes the following steps:

* Step 1 ---> build the ns-3 simulator
It is recommended to build de debug version:
>> sudo bash build.sh --debug_all

* Step 2 --> running ns-3-leo experiments
To execute the simulations described in the paper:

** Starlink S1 simulations:

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/starlink_s1.csv --constellation=StarlinkGateway --traceFile=starlink_s1_pair1_0001s.log  --precision=0.1 --islRate=10Mbps  --interval=0.001 --nOrbits=72 --nSatsPerOrbit=22 --islEnabled=true --duration=200 --ttlThresh=20  --source=41.01380:28.94970 --destination=-1.28330:36.81667"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/starlink_s1.csv --constellation=StarlinkGateway --traceFile=starlink_s1_pair2_0001s.log  --precision=0.1  --islRate=10Mbps  --interval=0.001 --nOrbits=72 --nSatsPerOrbit=22 --islEnabled=true --duration=200 --ttlThresh=20  --source=14.60420:120.9822 --destination=38.913811:121.602322"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/starlink_s1.csv --constellation=StarlinkGateway --traceFile=starlink_s1_pair3_0001s.log  --precision=0.1  --islRate=10Mbps --interval=0.001 --nOrbits=72 --nSatsPerOrbit=22 --islEnabled=true --duration=200 --ttlThresh=20  --source=-22.90278:-43.20750 --destination=59.929858:30.326228"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/starlink_s1.csv --constellation=StarlinkGateway --traceFile=starlink_s1_pair4_0001s.log  --precision=0.1 --islRate=10Mbps --interval=0.001 --nOrbits=72 --SatsPerOrbit=22  --islEnabled=true --duration=200 --ttlThresh=20  --source=48.853410:2.348800 --destination=55.754996:37.621849"> xx.out 2>&1

** Telesat T1 simulations:

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/telesat_t1.csv --constellation=TelesatGateway --traceFile=telesat_t1_pair1_0001s.log  --precision=0.1 --islRate=10Mbps  --interval=0.001  --nOrbits=27 --nSatsPerOrbit=13 --islEnabled=true --duration=200 --ttlThresh=20  --source=41.01380:28.94970 --destination=-1.28330:36.81667"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/telesat_t1.csv --constellation=TelesatGateway --traceFile=telesat_t1_pair2_0001s.log  --precision=0.1  --islRate=10Mbps  --interval=0.001 --nOrbits=27 --nSatsPerOrbit=13 --islEnabled=true --duration=200 --ttlThresh=20  --source=14.60420:120.9822 --destination=38.913811:121.602322"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/telesat_t1.csv --constellation=TelesatGateway --traceFile=telesat_t1_pair3_0001s.log  --precision=0.1  --islRate=10Mbps --interval=0.001  --nOrbits=27 --nSatsPerOrbit=13 --islEnabled=true --duration=200 --ttlThresh=20  --source=-22.90278:-43.20750 --destination=59.929858:30.326228"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/telesat_t1.csv --constellation=TelesatGateway --traceFile=telesat_t1_pair4_0001s.log  --precision=0.1 --islRate=10Mbps --interval=0.001   --nOrbits=27 --nSatsPerOrbit=13  --islEnabled=true --duration=200 --ttlThresh=20  --source=48.853410:2.348800 --destination=55.754996:37.621849"> xx.out 2>&1

** Kuiper K1 simulations:
>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/kuiper_k1.csv --constellation=KuiperGateway --traceFile=kuiper_k1_pair1_0001s.log  --precision=0.1 --islRate=10Mbps  --interval=0.001   --nOrbits=34 --nSatsPerOrbit=34 --islEnabled=true --duration=200 --ttlThresh=20  --source=41.01380:28.94970 --destination=-1.28330:36.81667"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/kuiper_k1.csv  --constellation=KuiperGateway --traceFile=kuiper_k1_pair2_0001s.log  --precision=0.1  --islRate=10Mbps  --interval=0.001  --nOrbits=34 --nSatsPerOrbit=34 --islEnabled=true --duration=200 --ttlThresh=20  --source=14.60420:120.9822 --destination=38.913811:121.602322"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/kuiper_k1.csv --constellation=KuiperGateway --traceFile=kuiper_k1_pair3_0001s.log  --precision=0.1  --islRate=10Mbps --interval=0.001   --nOrbits=34 --nSatsPerOrbit=34 --islEnabled=true --duration=200 --ttlThresh=20  --source=-22.90278:-43.20750 --destination=59.929858:30.326228"> xx.out 2>&1

>>sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/kuiper_k1.csv --constellation=KuiperGateway --traceFile=kuiper_k1_pair4_0001s.log  --precision=0.1 --islRate=10Mbps --interval=0.001    --nOrbits=34 --nSatsPerOrbit=34  --islEnabled=true --duration=200 --ttlThresh=20  --source=48.853410:2.348800 --destination=55.754996:37.621849"> xx.out 2>&1

Also read <hypatia>/ns3-sat-sim/simulator/SPE_results/README_SPE.md

