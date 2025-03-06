import argparse
import re
import matplotlib.pyplot as plt
import os

# Configuración del parser de argumentos
parser = argparse.ArgumentParser(description="Plot a grah delay vs time")
parser.add_argument('files', metavar='F', type=str, nargs=4, help="Files to be used")
parser.add_argument('--output', type=str, default='graph.png', help="Output file name (default 'graph.png')")
args = parser.parse_args()

colours=['blue','red','green','yellow']
ping_interval=['0.001 s','0.01 s','0.1 s','1 s']

x_min,x_max=20,30 #None,None
y_min,y_max=0,150 #None,None

plt.figure(figsize=(10,6))

# To extract values
pattern = re.compile(r"([\d\.eE\+\-]+)ns:/NodeList/\d+/ApplicationList/\d+/(\S+):(\d+):\d+:\+([\d\.eE\+\-]+)ns")

for i, file in enumerate(args.files):
   sending_times=[]
   delays=[]

   # Read file line by line
   try:
       with open(file, "r") as file:
           for line in file:
               match = pattern.search(line.strip())  
               if match:
                   try:
                       receiving_time = float(match.group(1))  # First value: receiving time
                       delay = float(match.group(4))  # Last value: delay

                       # Obtain the sending time
                       sending_time = (receiving_time - delay)/1e9

                       sending_times.append(sending_time)
                       delays.append(delay/1e6)
                   except ValueError:
                       pass  # Ignore if values are not valid

   except FileNotFoundError:
       print(f"Error: File '{file}' not found.")
       exit()

   # Create the graph
   if sending_times and delays:
    plt.scatter(sending_times, delays, color=colours[i], label='packet interval: '+ping_interval[i], marker='x',linewidth=0.5)
    #plt.plot(sending_times, delays, color=colours[i], label=ping_interval[i], linewidth=0.5)
   else:
    print("No data found in the file.")
    
if x_min is not None and x_max is not None:
   plt.xlim(x_min,x_max)

if y_min is not None and y_max is not None:
   plt.ylim(y_min,y_max)


plt.xlabel('Time (s)', fontsize=20)
plt.ylabel('Delay (ms)', fontsize=20)
plt.grid(True)
plt.legend(fontsize=20)

plt.savefig(args.output)

print(f"Graph saved as: {args.output}")
plt.show()


