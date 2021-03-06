import csv
import bpy

csvfile = open('C:/Users/xgman/Downloads/output.csv')
inFile = csv.reader(csvfile, delimiter=',', quotechar='"');
data = [];
for row in inFile:
    row[0] = (float(row[0])+88)*1850
    row[1] = (float(row[1])+88)*1850
    row[2] = (float(row[2])+88)*1850
    data.append(row);


 
# make mesh
vertices = data;
edges = []
faces = []
new_mesh = bpy.data.meshes.new('new_mesh')
new_mesh.from_pydata(vertices, edges, faces)
new_mesh.update()
# make object from mesh
new_object = bpy.data.objects.new('new_object', new_mesh)
# make collection
new_collection = bpy.data.collections.new('new_collection')
bpy.context.scene.collection.children.link(new_collection)
# add object to scene collection
new_collection.objects.link(new_object)
