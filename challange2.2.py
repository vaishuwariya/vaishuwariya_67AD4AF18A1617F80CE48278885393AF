def averageRuns(runs, matches, notout):
 
    # Calculate number of
    # dismissals
    out = matches - notout;
 
    # check for 0 times out
    if (out == 0):
        return -1;
 
    # Calculate batting average
    avg = runs // out;
 
    return avg;
 
# Driver Program
runs = 60000;
matches = 650;
notout = 350;
 
avg = averageRuns(runs, matches, notout);
 
if (avg == -1):
    print("NA");
else:
    print(avg);