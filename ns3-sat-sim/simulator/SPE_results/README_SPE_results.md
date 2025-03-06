###############
# SPE results
###############

The directory ns-3-leo-SPE-results/ contains contains the results of simulations corresponding to "Delay measurement applications" section.

Simulations using ns-3-leo includes the following steps:

* Step 1: Adapt the the parameters in the constellation constants' files must be directly changed in the code: 
```
<hypatia>/ns3-sat-sim/simulator/contrib/leo/
-----/model/
--------leo-starlink-constants.h 
		--> #define LEO_STARLINK_GATEWAY_ELEVATION_ANGLE  25    // deg: 25 or 35
		--> #define LEO_STARLINK_USER_ELEVATION_ANGLE     25    // deg: 25 or 35
		--> #define LEO_STARLINK_GATEWAY_DATA_RATE        "10Mbps"       // Mbps
		--> #define LEO_STARLINK_USER_DATA_RATE        "10Mbps"       // Mbps
--------leo-kuiper-constants.h 
		--> #define LEO_KUIPER_GATEWAY_ELEVATION_ANGLE  30    // deg: 30 or 35
		--> #define LEO_KUIPER_USER_ELEVATION_ANGLE     30    // deg: 30 or 35
		--> #define LEO_KUIPER_GATEWAY_DATA_RATE        "10Mbps"       // Mbps
		--> #define LEO_KUIPER_USER_DATA_RATE        "10Mbps"       // Mbps
--------leo-telesat-constants.h 
		--> #define LEO_TELESAT_GATEWAY_ELEVATION_ANGLE  10    // deg: 10 or 40
		--> #define LEO_TELESAT_USER_ELEVATION_ANGLE     40    // deg: 10 or 40
		--> #define LEO_TELESAT_GATEWAY_DATA_RATE        "10Mbps"       // Mbps
		--> #define LEO_TELESAT_USER_DATA_RATE        "10Mbps"       // Mbps
```
* Step 2 ---> build the ns-3 simulator
It is recommended to build de debug version:
```
sudo bash build.sh --debug_all
```
* Step 3 ---> run the simulations:

** Starlink S1 simulations:

```
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/starlink_s1.csv --constellation=StarlinkGateway --traceFile=starlink_s1_pair1_0001s.log  --precision=0.1 --islRate=10Mbps  --interval=0.001 --nOrbits=72 --nSatsPerOrbit=22 --islEnabled=true --duration=200 --ttlThresh=20  --source=41.01380:28.94970 --destination=-1.28330:36.81667"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/starlink_s1.csv --constellation=StarlinkGateway --traceFile=starlink_s1_pair2_0001s.log  --precision=0.1  --islRate=10Mbps  --interval=0.001 --nOrbits=72 --nSatsPerOrbit=22 --islEnabled=true --duration=200 --ttlThresh=20  --source=14.60420:120.9822 --destination=38.913811:121.602322"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/starlink_s1.csv --constellation=StarlinkGateway --traceFile=starlink_s1_pair3_0001s.log  --precision=0.1  --islRate=10Mbps --interval=0.001 --nOrbits=72 --nSatsPerOrbit=22 --islEnabled=true --duration=200 --ttlThresh=20  --source=-22.90278:-43.20750 --destination=59.929858:30.326228"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/starlink_s1.csv --constellation=StarlinkGateway --traceFile=starlink_s1_pair4_0001s.log  --precision=0.1 --islRate=10Mbps --interval=0.001 --nOrbits=72 --SatsPerOrbit=22  --islEnabled=true --duration=200 --ttlThresh=20  --source=48.853410:2.348800 --destination=55.754996:37.621849"> xx.out 2>&1
```

** Telesat T1 simulations:
```
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/telesat_t1.csv --constellation=TelesatGateway --traceFile=telesat_t1_pair1_0001s.log  --precision=0.1 --islRate=10Mbps  --interval=0.001  --nOrbits=27 --nSatsPerOrbit=13 --islEnabled=true --duration=200 --ttlThresh=20  --source=41.01380:28.94970 --destination=-1.28330:36.81667"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/telesat_t1.csv --constellation=TelesatGateway --traceFile=telesat_t1_pair2_0001s.log  --precision=0.1  --islRate=10Mbps  --interval=0.001 --nOrbits=27 --nSatsPerOrbit=13 --islEnabled=true --duration=200 --ttlThresh=20  --source=14.60420:120.9822 --destination=38.913811:121.602322"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/telesat_t1.csv --constellation=TelesatGateway --traceFile=telesat_t1_pair3_0001s.log  --precision=0.1  --islRate=10Mbps --interval=0.001  --nOrbits=27 --nSatsPerOrbit=13 --islEnabled=true --duration=200 --ttlThresh=20  --source=-22.90278:-43.20750 --destination=59.929858:30.326228"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/telesat_t1.csv --constellation=TelesatGateway --traceFile=telesat_t1_pair4_0001s.log  --precision=0.1 --islRate=10Mbps --interval=0.001   --nOrbits=27 --nSatsPerOrbit=13  --islEnabled=true --duration=200 --ttlThresh=20  --source=48.853410:2.348800 --destination=55.754996:37.621849"> xx.out 2>&1
```

** Kuiper K1 simulations:
```
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/kuiper_k1.csv --constellation=KuiperGateway --traceFile=kuiper_k1_pair1_0001s.log  --precision=0.1 --islRate=10Mbps  --interval=0.001   --nOrbits=34 --nSatsPerOrbit=34 --islEnabled=true --duration=200 --ttlThresh=20  --source=41.01380:28.94970 --destination=-1.28330:36.81667"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/kuiper_k1.csv  --constellation=KuiperGateway --traceFile=kuiper_k1_pair2_0001s.log  --precision=0.1  --islRate=10Mbps  --interval=0.001  --nOrbits=34 --nSatsPerOrbit=34 --islEnabled=true --duration=200 --ttlThresh=20  --source=14.60420:120.9822 --destination=38.913811:121.602322"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/kuiper_k1.csv --constellation=KuiperGateway --traceFile=kuiper_k1_pair3_0001s.log  --precision=0.1  --islRate=10Mbps --interval=0.001   --nOrbits=34 --nSatsPerOrbit=34 --islEnabled=true --duration=200 --ttlThresh=20  --source=-22.90278:-43.20750 --destination=59.929858:30.326228"> xx.out 2>&1
sudo  ./waf --run "leo-delay --destOnly=true --groundFile=contrib/leo/data/orbits/ground_stations_100.csv --orbitFile=contrib/leo/data/orbits/kuiper_k1.csv --constellation=KuiperGateway --traceFile=kuiper_k1_pair4_0001s.log  --precision=0.1 --islRate=10Mbps --interval=0.001    --nOrbits=34 --nSatsPerOrbit=34  --islEnabled=true --duration=200 --ttlThresh=20  --source=48.853410:2.348800 --destination=55.754996:37.621849"> xx.out 2>&1
```

To store the outputs of the diffent simulations, we have created the following directory structure, and the output files are moved to the corresponding directory:
```
<hypatia>/ns3-sat-sim/simulator/SPE-results/ns-3-leo-SPE-results/
-------------/snapshot_100ms/
-----------------/starlink_s1/
---------------------/elevation25
---------------------/elevation35
-----------------/kuiper_k1/
---------------------/elevation30
---------------------/elevation35
-----------------/telesat_t1/
---------------------/elevation10
---------------------/elevation40
-------------/snapshot_100ms/
-----------------/starlink_s1/
---------------------/elevation25
---------------------/elevation35
```
To generate the figures in the paper:

```
python3 plot_delay_results.py snapshot_100ms/kuiper_k1/elevation35/kuiper_k1_pair3_0001s.log  snapshot_100ms/kuiper_k1/elevation35/kuiper_k1_pair3_001s.log snapshot_100ms/kuiper_k1/elevation35/kuiper_k1_pair3_01s.log snapshot_100ms/kuiper_k1/elevation35/kuiper_k1_pair3_1s.log --output=figure_kuiper_pair4_nofiltered.png
python3 plot_delay_results.py snapshot_100ms/starlink_s1/elevation25/starlink_s1_pair4_0001s.log snapshot_100ms/starlink_s1/elevation25/starlink_s1_pair4_001s.log snapshot_100ms/starlink_s1/elevation25/starlink_s1_pair4_01s.log snapshot_100ms/starlink_s1/elevation25/starlink_s1_pair4_1s.log --output=figure_starlink_pair4_nofiltered.png
python3 plot_delay_results.py snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_0001s.log snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_001s.log snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_01s.log snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_1s.log --output=figure_telesat_pair4_nofiltered.png
```

After changing axis limits:
```
python3 plot_delay_results.py snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_0001s.log snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_001s.log snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_01s.log snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_1s.log --output=figure_telesat_pair4_nofiltered-magnified.png
```

To obtained graphs showing delay values after statistical filtering:
```
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/starlink_s1/elevation25/starlink_s1_pair1_0001s.log   snapshot_100ms/starlink_s1/elevation35/starlink_s1_pair1_0001s.log --elevationangle1=25 --elevationangle2=35 --output=figure_starlink_pair1_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/starlink_s1/elevation25/starlink_s1_pair2_0001s.log   snapshot_100ms/starlink_s1/elevation35/starlink_s1_pair2_0001s.log --elevationangle1=25 --elevationangle2=35 --output=figure_starlink_pair2_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/starlink_s1/elevation25/starlink_s1_pair3_0001s.log   snapshot_100ms/starlink_s1/elevation35/starlink_s1_pair3_0001s.log --elevationangle1=25 --elevationangle2=35 --output=figure_starlink_pair3_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/starlink_s1/elevation25/starlink_s1_pair4_0001s.log   snapshot_100ms/starlink_s1/elevation35/starlink_s1_pair4_0001s.log --elevationangle1=25 --elevationangle2=35 --output=figure_starlink_pair4_filtered.png

python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair1_0001s.log   snapshot_100ms/telesat_t1/elevation40/telesat_t1_pair1_0001s.log --elevationangle1=10 --elevationangle2=40 --output=figure_telesat_pair1_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair2_0001s.log   snapshot_100ms/telesat_t1/elevation40/telesat_t1_pair2_0001s.log --elevationangle1=10 --elevationangle2=40 --output=figure_telesat_pair2_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair3_0001s.log   snapshot_100ms/telesat_t1/elevation40/telesat_t1_pair3_0001s.log --elevationangle1=10 --elevationangle2=40 --output=figure_telesat_pair3_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/telesat_t1/elevation10/telesat_t1_pair4_0001s.log   snapshot_100ms/telesat_t1/elevation40/telesat_t1_pair4_0001s.log --elevationangle1=10 --elevationangle2=40 --output=figure_telesat_pair4_filtered.png

python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/kuiper_k1/elevation30/kuiper_k1_pair1_0001s.log   snapshot_100ms/kuiper_k1/elevation35/kuiper_k1_pair1_0001s.log --elevationangle1=30 --elevationangle2=35 --output=figure_kuiper_pair1_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/kuiper_k1/elevation30/kuiper_k1_pair2_0001s.log   snapshot_100ms/kuiper_k1/elevation35/kuiper_k1_pair2_0001s.log --elevationangle1=30 --elevationangle2=35 --output=figure_kuiper_pair2_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/kuiper_k1/elevation30/kuiper_k1_pair3_0001s.log   snapshot_100ms/kuiper_k1/elevation35/kuiper_k1_pair3_0001s.log --elevationangle1=30 --elevationangle2=35 --output=figure_kuiper_pair3_filtered.png
python3 plot_delay_results_filtered_1pair_1pinginterval_2elev.py snapshot_100ms/kuiper_k1/elevation30/kuiper_k1_pair4_0001s.log   snapshot_100ms/kuiper_k1/elevation35/kuiper_k1_pair4_0001s.log --elevationangle1=30 --elevationangle2=35 --output=figure_kuiper_pair4_filtered.png
```



