# filename: practical.py
# description: a python script created in submission for the Midterm Practical for GEOM73 (Customization of GIS Applications)
# submitted by: Francis Soriano 10283841

import arcpy

print("Setting the workspace...") # Please change the path to YOUR workspace !
workspace = input("Insert your workspace location here: ") # Opted to have this as an input due to me working in different workstations
arcpy.env.workspace = workspace
print("Workspace set!")

print("Creating file geodatabase...") # Creating file geodatabase
gdb_name = input("Insert the name of the file geodatabase here: ") # Opted to have this as an input so I can create new gdbs every time I bug test
arcpy.management.CreateFileGDB(workspace, gdb_name)
print("Geodatabase created in workspace!")

print("Importing shapefile into geodatabase...") # Importing shapefile into geodatabase as a feature class
shp_file = arcpy.ListFiles("*.shp")[0]
gdb_path = workspace + "\\" + gdb_name
arcpy.FeatureClassToGeodatabase_conversion(shp_file, gdb_path)
print("Shapefile imported!")

print("Opening a SearchCursor on the feature class...") # Open a SearchCurson on the feature class in the geodatabase
arcpy.env.workspace = gdb_path # Moving workspace to geodatabase level
# The following section of code is derived from: https://pro.arcgis.com/en/pro-app/latest/arcpy/data-access/searchcursor-class.htm
fc = arcpy.ListFeatureClasses()[0]
fc_fields = ["OID@","SHAPE@XY","Colour"]
with arcpy.da.SearchCursor(fc, fc_fields) as cursor:
    for row in cursor:
        print("Feature {} has a shape of {} and colour {}".format(row[0],row[1],row[2]))
print("SearchCursor inserted! Output above.")

print("Running the 'Get Count' tool...") # Running the Get Count tool
arcpy.env.workspace = workspace # Setting workspace to folder level, where .shp file is
shp_gc = arcpy.management.GetCount(shp_file)
int_shp_gc = int(shp_gc.getOutput(0))
arcpy.env.workspace = gdb_path # Moving workspace to geodatabase level for feature class
fc_gc = arcpy.management.GetCount(fc)
int_fc_gc = int(fc_gc.getOutput(0))
print("'Get Count' tool run!")
# Printing whether or not the number of rows between the shapefile and the feature class are the same
if int_shp_gc == int_fc_gc:
    print(f"The number of rows between the shapefile and the feature class are the same. The shapefile has {shp_gc} rows, while the feature class has {fc_gc} rows.")
else:
    print(f"The number of rows between the shapefile and the feature class are not the same. The shapefile has {shp_gc} rows, while the feature class has {fc_gc} rows.")
