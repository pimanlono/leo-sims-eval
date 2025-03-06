import sys
from exputil import *


def plot_ping(logs_ns3_dir1,logs_ns3_dir2, data_out_dir, pdf_out_dir, from_id, to_id, interval_ns, grado1, grado2):
    local_shell = LocalShell()

    # Create the output directories if they don't exist yet
    local_shell.make_full_dir(data_out_dir)
    local_shell.make_full_dir(pdf_out_dir)

    # Read in pingmesh CSV - elevation1
    pingmesh_csv_columns1 = read_csv_direct_in_columns(
        logs_ns3_dir1 + "/pingmesh.csv",
        "pos_int,pos_int,pos_int,pos_int,int,int,int,int,int,string"
    )
    num_entries1 = len(pingmesh_csv_columns1[0])
    from_list1 = pingmesh_csv_columns1[0]
    to_list1 = pingmesh_csv_columns1[1]
    ping_no_list1 = pingmesh_csv_columns1[2]
    send_request_timestamp_list1 = pingmesh_csv_columns1[3]
    reply_timestamp_list1 = pingmesh_csv_columns1[4]
    receive_reply_timestamp_list1 = pingmesh_csv_columns1[5]
    latency_to_there_ns_list1 = pingmesh_csv_columns1[6]
    latency_from_there_ns_list1 = pingmesh_csv_columns1[7]
    rtt_ns_list1 = pingmesh_csv_columns1[8]
    arrived_list1 = pingmesh_csv_columns1[9]



    # Read in pingmesh CSV
    pingmesh_csv_columns2 = read_csv_direct_in_columns(
        logs_ns3_dir2 + "/pingmesh.csv",
        "pos_int,pos_int,pos_int,pos_int,int,int,int,int,int,string"
    )
    num_entries2 = len(pingmesh_csv_columns2[0])
    from_list2 = pingmesh_csv_columns2[0]
    to_list2 = pingmesh_csv_columns2[1]
    ping_no_list2 = pingmesh_csv_columns2[2]
    send_request_timestamp_list2 = pingmesh_csv_columns2[3]
    reply_timestamp_list2 = pingmesh_csv_columns2[4]
    receive_reply_timestamp_list2 = pingmesh_csv_columns2[5]
    latency_to_there_ns_list2 = pingmesh_csv_columns2[6]
    latency_from_there_ns_list2 = pingmesh_csv_columns2[7]
    rtt_ns_list2 = pingmesh_csv_columns2[8]
    arrived_list2 = pingmesh_csv_columns2[9]


    # Find all entries for our pair
    ping_results1 = []
    prev_ping_no1 = -1
    for i in range(num_entries1):
        if from_list1[i] == from_id and to_list1[i] == to_id:

            # Some checks
            if ping_no_list1[i] != prev_ping_no1 + 1:
                raise ValueError("Ping number must be incrementally ascending")
            prev_ping_no1 += 1
            if arrived_list1[i] == "YES":
                is_lost1 = False
            elif arrived_list1[i] == "LOST":
                is_lost1 = True
            else:
                raise ValueError("Invalid value for arrival: " + arrived_list1[i])

            # If lost
            if is_lost1:
                if reply_timestamp_list1[i] != -1 \
                        or receive_reply_timestamp_list1[i] != -1 \
                        or latency_to_there_ns_list1[i] != -1 \
                        or latency_from_there_ns_list1[i] != -1 \
                        or rtt_ns_list1[i] != -1:
                    raise ValueError("Is lost so invalid timestamps should all be -1")
            else:
                parse_positive_int(str(reply_timestamp_list1[i]))
                parse_positive_int(str(receive_reply_timestamp_list1[i]))
                parse_positive_int(str(latency_to_there_ns_list1[i]))
                parse_positive_int(str(latency_from_there_ns_list1[i]))
                parse_positive_int(str(rtt_ns_list1[i]))

            # Add to ping results found
            ping_results1.append({
                "ping_no": ping_no_list1[i],
                "send_request_timestamp": send_request_timestamp_list1[i],
                "reply_timestamp": reply_timestamp_list1[i],
                "receive_reply_timestamp": receive_reply_timestamp_list1[i],
                "latency_to_there_ns": latency_to_there_ns_list1[i],
                "latency_from_there_ns": latency_from_there_ns_list1[i],
                "rtt_ns": rtt_ns_list1[i],
                "is_lost": is_lost1
            })



    # Find all entries for our pair
    ping_results2 = []
    prev_ping_no2 = -1
    for i in range(num_entries2):
        if from_list2[i] == from_id and to_list2[i] == to_id:

            # Some checks
            if ping_no_list2[i] != prev_ping_no2 + 1:
                raise ValueError("Ping number must be incrementally ascending")
            prev_ping_no2 += 1
            if arrived_list2[i] == "YES":
                is_lost2 = False
            elif arrived_list2[i] == "LOST":
                is_lost2 = True
            else:
                raise ValueError("Invalid value for arrival: " + arrived_list2[i])

            # If lost
            if is_lost2:
                if reply_timestamp_list2[i] != -1 \
                        or receive_reply_timestamp_list2[i] != -1 \
                        or latency_to_there_ns_list2[i] != -1 \
                        or latency_from_there_ns_list2[i] != -1 \
                        or rtt_ns_list2[i] != -1:
                    raise ValueError("Is lost so invalid timestamps should all be -1")
            else:
                parse_positive_int(str(reply_timestamp_list2[i]))
                parse_positive_int(str(receive_reply_timestamp_list2[i]))
                parse_positive_int(str(latency_to_there_ns_list2[i]))
                parse_positive_int(str(latency_from_there_ns_list2[i]))
                parse_positive_int(str(rtt_ns_list2[i]))

            # Add to ping results found
            ping_results2.append({
                "ping_no": ping_no_list2[i],
                "send_request_timestamp": send_request_timestamp_list2[i],
                "reply_timestamp": reply_timestamp_list2[i],
                "receive_reply_timestamp": receive_reply_timestamp_list2[i],
                "latency_to_there_ns": latency_to_there_ns_list2[i],
                "latency_from_there_ns": latency_from_there_ns_list2[i],
                "rtt_ns": rtt_ns_list2[i],
                "is_lost": is_lost2
            })

    # Data RTT file
    print("TIME VS. RTT")
    data_rtt_filename1 = "%s/ping_%d_to_%d_rtt1.csv" % (data_out_dir, from_id, to_id)
    with open(data_rtt_filename1, "w+") as out_file:
        for val in ping_results1:
            if val["is_lost"]:
                out_file.write("%d,%d,%d,0\n" % (from_id, to_id, val["send_request_timestamp"]))
            else:
                out_file.write("%d,%d,%d,%d\n" % (from_id, to_id, val["send_request_timestamp"], val["rtt_ns"]))

    # Data RTT file
    print("TIME VS. RTT")
    data_rtt_filename2 = "%s/ping_%d_to_%d_rtt2.csv" % (data_out_dir, from_id, to_id)
    with open(data_rtt_filename2, "w+") as out_file:
        for val in ping_results2:
            if val["is_lost"]:
                out_file.write("%d,%d,%d,0\n" % (from_id, to_id, val["send_request_timestamp"]))
            else:
                out_file.write("%d,%d,%d,%d\n" % (from_id, to_id, val["send_request_timestamp"], val["rtt_ns"]))



    # Show what is produced
    print(" > Data line format..... [from_id],[to_id],[send_request_timestamp (ns)],[measured_rtt (ns); 0 if lost]")
    print(" > Produced data file... " + data_rtt_filename1)
    # Show what is produced
    print(" > Data line format..... [from_id],[to_id],[send_request_timestamp (ns)],[measured_rtt (ns); 0 if lost]")
    print(" > Produced data file... " + data_rtt_filename2)

    # Plot time vs. rtt
    pdf_rtt_filename = "%s/ping_time_vs_rtt_%d_to_%d.eps" % (pdf_out_dir, from_id, to_id)
    local_shell.copy_file("plot_ping_time_vs_rtt_2elevations.plt", "temp.plt")
    local_shell.sed_replace_in_file_plain("temp.plt", "[OUTPUT-FILE]", pdf_rtt_filename)
    local_shell.sed_replace_in_file_plain("temp.plt", "[DATA-FILE1]", data_rtt_filename1)
    local_shell.sed_replace_in_file_plain("temp.plt", "[DATA-FILE2]", data_rtt_filename2)
    local_shell.sed_replace_in_file_plain("temp.plt", "[GRADO1]",grado1)
    local_shell.sed_replace_in_file_plain("temp.plt", "[GRADO2]",grado2)
    local_shell.perfect_exec("gnuplot temp.plt")
    local_shell.perfect_exec("gnuplot temp.plt")
    local_shell.remove("temp.plt")
    print(" > Produced plot........ " + pdf_rtt_filename)
    print("")



def main():
    args = sys.argv[1:]
    if len(args) != 9:
        print("Must supply exactly six arguments")
        print("Usage: python plot_ping.py [logs_ns3 directory] [logs_ns3_directory] [data_out_dir] [pdf_out_dir] "
              "[from_node_id] [to_node_id] [interval_ns (for out-of-order counting)] [elevation1] [elevation2]")
        exit(1)
    else:
        plot_ping(
            args[0],
            args[1],
            args[2],
            args[3],
            int(args[4]),
            int(args[5]),
            int(args[6]),
            args[7],
            args[8]
        )


if __name__ == "__main__":
    main()
