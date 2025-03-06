################################################
### SPE-paper : modifications in ns-3-leo module
################################################

As detailed in the paper, some modifications have been made to the original ns-3-leo code 
to make the simulation environment similar to Hypatia.

The following are the affected files.
Changes can be located searching "//SPE-modification" comments in the code. 

<hypatia>/ns3-sat-sim/simulator/contrib/leo/
-----/examples/
--------leo-delay-tracing-example.cc  (modified)
		--> The leo-delay program has been modified to be able to import from 
		a text  file (the same one used by Hypatia) the list of GWs and their location.
		The name of the file (ground_station_100.csv) is passed as a parameter in the 
		command line when launching the simulation.
		--> The leo-delay program has been also modified to populate ARP tables
		as done in Hypatia.
		--> nOrbits and nSatsPerOrbit as command line parameters to be used in the +grid topology implementation
-----/data/orbits/
--------ground_stations_100.csv (added)
		--> List of 100 GWs used in the simulations (from Hypatia).
--------kuiper_k1.csv (added)
               --> Parameters of Kuiper K1 constellation	
--------starlink_s1.csv (added)
               --> Parameters of Starlink S1 constellation     
--------telesat_t1.csv (added)
               --> Parameters of Telesat T1 constellation                                    
-----/helper/
--------leo-channel-helper.cc (modified)
		--> To allow the use of the Kuiper constellation, which was not initially
		considered by ns-3-leo. 
-----/model/
--------leo-kuiper-constants.h (added)
		--> A file defining the Kuiper constellation's constants.
--------isl-mock-channel.cc (modified)
		--> To implement the +grid topology. 

		
In order the perform the different simulations, some parameters in the constellation constants' files must be directly changed in the code: 

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

