import argparse
import re
import matplotlib.pyplot as plt
import statistics

# Configuración del parser de argumentos
parser = argparse.ArgumentParser(description="Plot a grah delay vs time")
parser.add_argument('files', metavar='F', type=str,nargs=2, help="Files to be used")
parser.add_argument('--output', type=str,default="graph_filtered.png", help="output file name")
parser.add_argument('--elevationangle1', type=str,default="undefined", help="min elevation angle")
parser.add_argument('--elevationangle2', type=str,default="undefined", help="proposed elevation angle")
args=parser.parse_args()

colours=['#2177b0','#fc7f2b']
x_min,x_max=0,200
y_min,y_max=0,100
output_file="graph_filtered.png"

textangle=['Minimum elevation angle: ','Proposed elevation angle: ']
angle=[args.elevationangle1, args.elevationangle2]

# To extract values
pattern = re.compile(r"([\d\.eE\+\-]+)ns:/NodeList/\d+/ApplicationList/\d+/(\S+):(\d+):\d+:\+([\d\.eE\+\-]+)ns")

plt.figure(figsize=(10,6))

for i,file in enumerate(args.files):
   sending_times=[]
   delays=[]

   #Read file line by line
   try:
       with open(file, "r") as file:
           for line in file:
               match = pattern.search(line.strip())  
               if match:
                   try:
                       receiving_time = float(match.group(1))  # First value: receiving time
                       delay = float(match.group(4))  # Last value: delay

                       # Obtain sending time
                       sending_time = (receiving_time - delay)/1e9

                       sending_times.append(sending_time)
                       delays.append(delay/1e6)
                   except ValueError:
                       pass  # Ignored if not valid values
   except FileNotFoundError:
       print(f"Error: File '{file}' not found.")
       exit()

   # Filter values using IQR (Inter-Quartile Range)
   if sending_times and delays:
       # Obtain Q1,Q3
       Q1_sending = statistics.quantiles(sending_times, n=4)[0]
       Q3_sending = statistics.quantiles(sending_times, n=4)[2]
       IQR_sending = Q3_sending - Q1_sending
    
       Q1_delay = statistics.quantiles(delays, n=4)[0]
       Q3_delay = statistics.quantiles(delays, n=4)[2]
       IQR_delay = Q3_delay - Q1_delay

       # Limits to filter outliers
       limit_lower_sending = Q1_sending - 1.5 * IQR_sending
       limit_upper_sending = Q3_sending + 1.5 * IQR_sending

       limit_lower_delay = Q1_delay - 1.5 * IQR_delay
       limit_upper_delay = Q3_delay + 1.5 * IQR_delay

       # Filtered data (without outliers)
       filtered_data = [(te, re) for te, re in zip(sending_times, delays)
                       if limit_lower_sending <= te <= limit_upper_sending
                       and limit_lower_delay <= re <= limit_upper_delay]

       filtered_sending_times, filtered_delays = zip(*filtered_data) if filtered_data else ([], [])

       # Create the graph
       if filtered_sending_times and filtered_delays:
          plt.scatter(filtered_sending_times, filtered_delays, color=colours[i],marker='x', label=textangle[i]+angle[i])
          #plt.plot(filtered_sending_times, filtered_delays, color=colours[i], label='Delay vs. Time (without outliers)')
   else:
      print("No data found in the file")
      #plt.plot([], [], color=colours[i], label=textangle[i] + angle[i])
      plt.axhline(y=0, color=colours[i], label=textangle[i] + angle[i])

if x_min is not None and x_max is not None:
   plt.xlim(x_min,x_max) 
if y_min is not None and y_max is not None:
   plt.ylim(y_min,y_max)

plt.xlabel('Time (s)',fontsize=20)
plt.ylabel('Delay (ms)',fontsize=20)
plt.grid(True)
plt.legend(fontsize=20)

plt.savefig(args.output)

print(f"Graph saved as: {args.output}")
plt.show()

