
###############
# SPE results
###############

This folder contains the graphs used in the section "Impact of snapshot interval in satgenpy"

They are obtained by running:
 python3 file_for_plotting_histogram_isls.py
 python3 file_for_plotting_histogram_relays.py

The necessary data files are: 
graphs_starlink/elevation35/graphs_isls/200s/path/data/histogram_missed_path_changes.txt
graphs_kuiper/elevation35/graphs_isls/200s/path/data/histogram_missed_path_changes.txt
graphs_telesat/elevation40/graphs_isls/200s/path/data/histogram_missed_path_changes.txt


These files are obtained after the execution of: 

python3 -m satgen.post_analysis.main_analyze_time_step_path ./00_SPE_results/graficas_starlink/elevation35/graficas_relays/ /home/pilar/hypatia/paper/satellite_networks_state/gen_data/SPE_24_proposed_elevation_angle/starlink_550_isls_none_ground_stations_top_100_algorithm_free_one_only_gs_relays/ 100,1000,10000 200
python3 -m satgen.post_analysis.main_analyze_time_step_path ./00_SPE_results/graficas_telesat/elevation40/graficas_relays/ /home/pilar/hypatia/paper/satellite_networks_state/gen_data/SPE_24_proposed_elevation_angle/telesat_1015_isls_none_ground_stations_top_100_algorithm_free_one_only_gs_relays/ 100,1000,10000 200
python3 -m satgen.post_analysis.main_analyze_time_step_path ./00_SPE_results/graficas_kuiper/elevation35/graficas_relays/ /home/pilar/hypatia/paper/satellite_networks_state/gen_data/SPE_24_proposed_elevation_angle/Kuiper_630_isls_none_ground_stations_top_100_algorithm_free_one_only_gs_relays/ 100,1000,10000 200


The values used are those obtained after running satgenpy from the corresponding scripts for the simulations, located at hypatia/paper/satellite_network_state
