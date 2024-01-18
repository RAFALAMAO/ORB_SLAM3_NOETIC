gnss_origin_filename = "evaluation/Ground_truth/EuRoC_left_cam/MH03_GT.txt"

ground_truth_filename = "MH03_GT.txt"

gnss_f = open(gnss_origin_filename, "r") 

i = 0
with open(ground_truth_filename, "w") as f:
    lines = gnss_f.readlines()      
    for line in lines:
        i+=1
        if i == 1:
            continue

        #print(float(line.split(",")[0]), float(line.split(",")[1]), float(line.split(",")[2]), float(line.split(",")[3]))
        f.write(str("%.6f %.7f %.7f %.7f %.7f %.7f %.7f %.7f" % (float(line.split(",")[0])/10e+8, float(line.split(",")[1]), float(line.split(",")[2]), float(line.split(",")[3]), float(line.split(",")[5]), float(line.split(",")[6]), float(line.split(",")[7]), float(line.split(",")[4]))))
        f.write("\n")