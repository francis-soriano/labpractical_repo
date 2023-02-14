# filename: practical.py
# description: a python script created in submission for the Midterm Practical for GEOM73 (Customization of GIS Applications)
# submitted by: Francis Soriano 10283841

import arcpy

print("Setting the workspace...") # Please change the path to YOUR workspace !
workspace = r"D:\\_sandbox\\labpracticals\\labpractical_repo\\programming\\practical_data"
arcpy.env.workspace = workspace
print("Workspace set!")

print("Creating file geodatabase...")
arcpy.management.CreateFileGDB(workspace, "LabPractical")
print("Geodatabase created in workspace!")

print("Importing shapefile into geodatabase...")
shp_file = arcpy.ListFiles("*.shp")[0]
desc = arcpy.Describe(shp_file)
shp_file_path = desc.path
shp_file_name = desc.baseName
gdb_path = workspace + "\\LabPractical.gdb"
arcpy.FeatureClassToGeodatabase_conversion(shp_file, gdb_path)
print("Shapefile imported!")

print("Opening a search cursor on the feature class...")
arcpy.env.workspace = gdb_path # Moving workspace into geodatabase


