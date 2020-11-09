#https://docs.python.org/3/library/csv.html
import csv
import bpy
with open ("fy20_adc_data_file_88_degrees.csv", newline="") as lunar_data:
    for row in csv.reader(lunar_data):
        latitude = (float(row[0])+88)*1850;
        longitude = (float(row[1])+88)*1850;
        height = (float(row[2])+88)*1850;
        slope = row[3];
        bpy.ops.mesh.primitive_sphere_add(location=(latitude, longitude, height));
