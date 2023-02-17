# filename: practical.py
# description: a python script created in submission for the Midterm Practical for GEOM73 (Customization of GIS Applications)
# submitted by: Francis Soriano 10283841

import arcpy

print("Setting the workspace...") # Please change the path to YOUR workspace !
workspace = input("Insert your workspace location here: ") # Opted to have this as an input due to me working in different workstations
arcpy.env.workspace = workspace
print("Workspace set!")

print("Creating file geodatabase...")
gdb_name = input("Insert the name of the file geodatabase here: ") # Opted to have this as an input so I can create new gdbs every time I bug test
arcpy.management.CreateFileGDB(workspace, gdb_name)
print("Geodatabase created in workspace!")

print("Importing shapefile into geodatabase...")
shp_file = arcpy.ListFiles("*.shp")[0]
desc = arcpy.Describe(shp_file)
shp_file_path = desc.path
shp_file_name = desc.baseName
gdb_path = workspace + "\\" + gdb_name
arcpy.FeatureClassToGeodatabase_conversion(shp_file, gdb_path)
print("Shapefile imported!")

print("Opening a search cursor on the feature class...")
feature_class = arcpy.ListFiles()[0]


