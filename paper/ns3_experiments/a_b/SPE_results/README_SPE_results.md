###############
# SPE results
###############

>> The directory snapshot_100ms/ contains contains the results of simulations corresponding to "Delay measurement applications" section.

>> To perform the different simulations, you have to adapt the file run_list.py and execute the three steps indicated in the Hypatia documentation:
    step_1_generate_runs.py
    step_2_runs.py
    step_3_generate_plots.py
    
It is important to remember that, in order to carry out a given simulation, it is necessary to have previously executed satgenpy, or, if applicable, to have recovered the required satgenpy outputs from the directory paper/satellite_network_state/SPE_results to the directory paper/satellite_network_state/gen_data (read README_SPE_results.md in gen_data for detailed info).
    
Outputs of each simulation are stores in pdf/, data/, and runs/ directories.

At the execution of each new simulation, these directories are overwritten. Therefore, to avoid losing the obtained results, after performing a particular simulation, the content of pdf/, data/, and runs/ directories have been moved to the corresponding directory within snapshot_100ms.

>> To represent in the same graph the results obtained in the simulations with the minimum and proposed elevation angles, we have programmed the files: plot_ping_2elevations.py and plot_ping_time_vs_rtt_2elevations.plt

Being located in plotting_results_2elevation_angles directory, the list of commands to obtain the twelve graphs corresponging to the 4 src-dst pairs using each constallation is:

python3 plot_ping_2elevations.py ../snapshot_100ms/telesat_t1/elevation10/ping-interval-1ms/telesat_1015_isls_365_to_447_pings/logs_ns3/ ../snapshot_100ms/telesat_t1/elevation40/ping-interval-1ms/telesat_1015_isls_365_to_447_pings/logs_ns3/ . . 365 447 1 10 40
python3 plot_ping_2elevations.py ../snapshot_100ms/telesat_t1/elevation10/ping-interval-1ms/telesat_1015_isls_368_to_436_pings/logs_ns3/ ../snapshot_100ms/telesat_t1/elevation40/ping-interval-1ms/telesat_1015_isls_368_to_436_pings/logs_ns3/ . . 368 436 1 10 40
    python3 plot_ping_2elevations.py ../snapshot_100ms/telesat_t1/elevation10/ping-interval-1ms/telesat_1015_isls_369_to_424_pings/logs_ns3/ ../snapshot_100ms/telesat_t1/elevation40/ping-interval-1ms/telesat_1015_isls_369_to_424_pings/logs_ns3/ . . 369 424 1 10 40
    python3 plot_ping_2elevations.py ../snapshot_100ms/telesat_t1/elevation10/ping-interval-1ms/telesat_1015_isls_375_to_372_pings/logs_ns3/  ../snapshot_100ms/telesat_t1/elevation40/ping-interval-1ms/telesat_1015_isls_375_to_372_pings/logs_ns3/ . . 375 372 1 10 40
    python3 plot_ping_2elevations.py ../snapshot_100ms/starlink_s1/elevation25/ping-interval-1ms/starlink_550_isls_1598_to_1680_pings/logs_ns3/ ../snapshot_100ms/starlink_s1/elevation35/ping-interval-1ms/starlink_550_isls_1598_to_1680_pings/logs_ns3/ . . 1598 1680 1 25 35
    python3 plot_ping_2elevations.py ../snapshot_100ms/starlink_s1/elevation25/ping-interval-1ms/starlink_550_isls_1601_to_1669_pings/logs_ns3/ ../snapshot_100ms/starlink_s1/elevation35/ping-interval-1ms/starlink_550_isls_1601_to_1669_pings/logs_ns3/ . . 1601 1669 1 25 35
    python3 plot_ping_2elevations.py ../snapshot_100ms/starlink_s1/elevation25/ping-interval-1ms/starlink_550_isls_1602_to_1657_pings/logs_ns3/ ../snapshot_100ms/starlink_s1/elevation35/ping-interval-1ms/starlink_550_isls_1602_to_1657_pings/logs_ns3/ . . 1602 1657 1 25 35
    python3 plot_ping_2elevations.py ../snapshot_100ms/starlink_s1/elevation25/ping-interval-1ms/starlink_550_isls_1608_to_1605_pings/logs_ns3/ ../snapshot_100ms/starlink_s1/elevation35/ping-interval-1ms/starlink_550_isls_1608_to_1605_pings/logs_ns3/ . . 1608 1605 1 25 35
    python3 plot_ping_2elevations.py ../snapshot_100ms/kuiper_k1/elevation30/ping-interval-1ms/kuiper_630_isls_1170_to_1252_pings/logs_ns3/ ../snapshot_100ms/kuiper_k1/elevation35/ping-interval-1ms/kuiper_630_isls_1170_to_1252_pings/logs_ns3/ . . 1170 1252 1 30 35
    python3 plot_ping_2elevations.py ../snapshot_100ms/kuiper_k1/elevation30/ping-interval-1ms/kuiper_630_isls_1173_to_1241_pings/logs_ns3/ ../snapshot_100ms/kuiper_k1/elevation35/ping-interval-1ms/kuiper_630_isls_1173_to_1241_pings/logs_ns3/ . . 1173 1241 1 30 35
    python3 plot_ping_2elevations.py ../snapshot_100ms/kuiper_k1/elevation30/ping-interval-1ms/kuiper_630_isls_1174_to_1229_pings/logs_ns3/ ../snapshot_100ms/kuiper_k1/elevation35/ping-interval-1ms/kuiper_630_isls_1174_to_1229_pings/logs_ns3/ . . 1174 1229 1 30 35
    python3 plot_ping_2elevations.py ../snapshot_100ms/kuiper_k1/elevation30/ping-interval-1ms/kuiper_630_isls_1180_to_1177_pings/logs_ns3/ ../snapshot_100ms/kuiper_k1/elevation35/ping-interval-1ms/kuiper_630_isls_1170_to_1252_pings/logs_ns3/ . . 1180 1177 1 30 35


The structure of the directory is:

plot_ping_2elevations.py and plot_ping_time_vs_rtt_2elevations.plt


SPE_results/
--snapshot_100ms/
-----kuiper_k1/
---------elevation30/
--------------ping_interval_1ms/
------------------pdf/
------------------data/
------------------kuiper_630_isls_1173_to_1241_pings/
------------------kuiper_630_isls_1180_to_1177_pings/
------------------kuiper_630_isls_1170_to_1252_pings/
------------------kuiper_630_isls_1174_to_1229_pings/
---------elevation35/
--------------ping_interval_1ms/
------------------pdf/
------------------data/
------------------kuiper_630_isls_1173_to_1241_pings/
------------------kuiper_630_isls_1180_to_1177_pings/
------------------kuiper_630_isls_1170_to_1252_pings/
------------------kuiper_630_isls_1174_to_1229_pings/
-----telesat_t1/
---------elevation10/
------------------pdf/
------------------data/
------------------telesat_1015_isls_365_to_447_pings/
------------------telesat_1015_isls_368_to_436_pings/
------------------telesat_1015_isls_368_to_436_pings/
------------------telesat_1015_isls_368_to_436_pings/
---------elevation40/
------------------pdf/
------------------data/
------------------pdf/
------------------data/
------------------telesat_1015_isls_365_to_447_pings/
------------------telesat_1015_isls_368_to_436_pings/
------------------telesat_1015_isls_368_to_436_pings/
------------------telesat_1015_isls_368_to_436_pings/
-----starlink_s1/
---------elevation25/
------------------pdf/
------------------data/
------------------pdf/
------------------data/
------------------starlink_550_isls_1598_to_1680_pings/
------------------starlink_550_isls_1601_to_1669_pings/
------------------starlink_550_isls_1601_to_1669_pings/
------------------starlink_550_isls_1608_to_1605_pings/
---------elevation35/
------------------pdf/
------------------data/
------------------pdf/
------------------data/
------------------starlink_550_isls_1598_to_1680_pings/
------------------starlink_550_isls_1601_to_1669_pings/
------------------starlink_550_isls_1601_to_1669_pings/
------------------starlink_550_isls_1608_to_1605_pings/
--plotting_results_2elevation_angles directory/
-----plot_ping_2elevations.py
-----plot_ping_time_vs_rtt_2elevations.plt
-----{*.eps --> generated graphical files}
