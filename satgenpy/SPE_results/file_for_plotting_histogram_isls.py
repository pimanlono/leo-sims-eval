import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba

# Function to read data from a file
def read_data(file):
    with open(file, "r") as f:
        lines = f.readlines()

    # Extract granularity
    granularity = list(map(int, lines[0].split()[1:]))

    #Dictionary to store data
    data = {}

    # Leer los valores de frecuencia
    for line in lines[1:]:
        parts = line.split()
        key = parts[0]  # "1000ms" o "10000ms"
        values = [float(x) * 100 for x in parts[1:]]  
        data[key] = values

    return granularity,data

# Define input files (one per scenario)
files = {
    "S1": "graficas_starlink/elevation35/graficas_isls/200s/path/data/histogram_missed_path_changes.txt",
    "K1": "graficas_kuiper/elevation35/graficas_isls/200s/path/data/histogram_missed_path_changes.txt",
    "T1": "graficas_telesat/elevation40/graficas_isls/200s/path/data/histogram_missed_path_changes.txt"
}

# Read data from each file
scenarios = {}
for scenario, file in files.items():
    granularity,data = read_data(file)
    scenarios[scenario] = {"granularity": granularity, "data": data}

limite_x_min, limite_x_max = 0, 10

# Plotting parameters
width = 0.5  
separation_scenarios = 2 

plt.figure(figsize=(7.5, 5))

# X-axis positions
position_x_total = []  
labels_x = []  

colors_base=['blue','green','purple']
colors_manual=['blue','lightblue','green','lightgreen','grey','lightgrey']


def light_color(color, factor=1.5):
    rgba = to_rgba(color)
    return (min(rgba[0] * factor, 1), min(rgba[1] * factor, 1), min(rgba[2] * factor, 1), rgba[3])

def dark_color(color, factor=0.9):
    rgba = to_rgba(color)
    return (rgba[0] * factor, rgba[1] * factor, rgba[2] * factor, rgba[3])

# Iterate over each scenario and assing a separate position
offset = 0  # Initial X displacement 

i=0

for scenario, data in scenarios.items():
    granularity = np.array(data["granularity"])

    indices = [i for i, g in enumerate(granularity) if limite_x_min <= g <= limite_x_max]
    filtered_granularity = [granularity[i] for i in indices]

    # Filtrar también los valores de frecuencia
    filtered_data = {key: [data["data"][key][i] for i in indices] for key in data["data"]}

    # Convert granularity to numpy to displacement
    granularity_numpy = np.array(filtered_granularity)

    # Assing color to scenario 
    color1=colors_manual[i%len(colors_manual)]
    color2=colors_manual[i%len(colors_manual)+1]

    #Plot displaced bars within each group 
    plt.bar(granularity_numpy + offset - width/2, filtered_data["1000ms"], width=width, label=f"{scenario}-1s vs 100ms", alpha=0.7,color=color1)
    plt.bar(granularity_numpy + offset + width/2, filtered_data["10000ms"], width=width, label=f"{scenario}-10s vs 100ms", alpha=0.7, color=color2)

    # Save X positions for labels
    position_x_total.extend(granularity_numpy + offset)
    labels_x.extend(filtered_granularity)

    offset += max(filtered_granularity) + separation_scenarios

    i=i+2


plt.xticks(position_x_total, labels_x, rotation=0)
plt.yticks(np.arange(0,100,10))

plt.xlabel("Number of path changes missed", fontsize=14)
plt.ylabel("Percentage of src-dst pairs", fontsize=14)
plt.title("algorithm_one_only_over_isls", fontsize=14)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

output_file="./figure_histogram_missed_changes_isls.png"
plt.savefig(output_file)

plt.show()

