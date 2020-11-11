import csv
import bpy 
END = 0;
lunar_data = open("fy20_adc_data_file_88_degrees.csv", newline="");
def plot_data(start, end, start2=0, end2=0):
    #(reset screen)
    line_number = 0;
    draw = False;
    for row in csv.reader(lunar_data):
        line_number += 1;
        if (isinstance(start, int)):
            if (line_number >= start && end == 0):
                draw = True;
            elif (line_number >= start && line_number <= end):
                draw = True;
            else:
                draw == False;
        elif (isinstance(start, float)):
            if (row[0] == start && row[1] == end):
                draw = True;
            if (row[0] == start2 && row[1] == end2):
                draw = False;
        if (draw == True):
            latitude = (float(row[0])+88)*1850;
            longitude = (float(row[1])+88)*1850;
            height = (float(row[2])+88)*1850;
            slope = row[3];
            bpy.ops.mesh.primitive_sphere_add(location=(latitude, longitude, height));
            
            
plot_data(0, END); #plot all lines
plot_data(-89.232, 54.794,  -89.200, 120.690); #plot from (-89.232, 54.794) to (-89.2, 120.69)
