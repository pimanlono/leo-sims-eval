###
###  Released under the MIT License (MIT) --- see ../LICENSE
###  Copyright (c) 2014 Ankit Singla, Sangeetha Abdu Jyothi, Chi-Yao Hong,
###  Lucian Popa, P. Brighten Godfrey, Alexandra Kolla, Simon Kassing
###

#####################################
### STYLING

# Terminal (gnuplot 4.4+); Swiss neutral Helvetica font
#set terminal pdfcairo font "Helvetica, 24" linewidth 1.5 rounded dashed
set terminal postscript eps enhanced color font "Helvetica, 24" linewidth 1.5 rounded dashed
set encoding utf8

# Line style for axes
set style line 80 lt rgb "#808080"

# Line style for grid
set style line 81 lt 0  # Dashed
set style line 81 lt rgb "#999999"  # Grey grid

# Grey grid and border
set grid back linestyle 81
set border 3 back linestyle 80
set xtics nomirror
set ytics nomirror

# Line styles
#set style line 1 lt rgb "#2177b0" lw 1.4 pt 2 ps 0
#set style line 2 lt rgb "#fc7f2b" lw 1.4 pt 2 ps 0
set style line 1 lt rgb "#2177b0" 
set style line 2 lt rgb "#fc7f2b" 
set style line 3 lt rgb "#2f9e37" lw 2.4 pt 3 ps 0
set style line 4 lt rgb "#d42a2d" lw 2.4 pt 4 ps 1.4
set style line 5 lt rgb "#80007F" lw 2.4 pt 5 ps 1.4
set style line 6 lt rgb "#8a554c" lw 2.4 pt 6 ps 1.4
set style line 7 lt rgb "#e079be" lw 2.4 pt 0 ps 1.4
set style line 8 lt rgb "#7d7d7d" lw 2.4 pt 0 ps 1.4
set style line 9 lt rgb "#000000" lw 2.4 pt 0 ps 1.4

# Output
set output "[OUTPUT-FILE]"

#####################################
### AXES AND KEY

# Axes labels
set xlabel "Time (s)" font ",20" # Markup: e.g. 99^{th}, {/Symbol s}, {/Helvetica-Italic P}
set ylabel "Ping RTT (ms)" font ",20"

# Axes ranges
set xrange [0:199]       # Explicitly set the x-range [lower:upper]
set yrange [0:150]       # Explicitly set the y-range [lower:upper]

set xtics font ",20"
set ytics font ",20"


#set xtics {0,100,200}
# set ytics <start>, <incr> {,<end>}
# set format x "%.2f%%"  # Set the x-tic format, e.g. in this case it takes 2 sign. decimals: "24.13%""

# For logarithmic axes
# set log x           # Set logarithmic x-axis
# set log y           # Set logarithmic y-axis
# set mxtics 3        # Set number of intermediate tics on x-axis (for log plots)
# set mytics 3        # Set number of intermediate tics on y-axis (for log plots)

# Font of the key (a.k.a. legend)
set key font ",20"
set key reverse
set key top right Left
set key spacing 2

#####################################
### PLOTS
set datafile separator ","
plot    "[DATA-FILE1]" every 25 using ($3/1000000000):($4/1000000) title "Minimum elevation angle: [GRADO1]º " w lp ls 1, \
    "[DATA-FILE2]" every 25 using ($3/1000000000):($4/1000000) title "Proposed elevation angle: [GRADO2]º" w lp ls 2, \
