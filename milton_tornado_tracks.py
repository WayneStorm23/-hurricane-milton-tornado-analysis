import csv
from qgis.core import QgsFeature, QgsGeometry, QgsPointXY, QgsVectorLayer, QgsProject, QgsField
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QColor

# Create a new line layer
layer = QgsVectorLayer("LineString?crs=EPSG:4326", "Tornado Tracks", "memory")
pr = layer.dataProvider()

# Add fields 
pr.addAttributes([QgsField("EF", QVariant.String)])
layer.updateFields()

# Use raw string for the path to  CSV file
csv_file_path = r'C:\Users\Wayne Morley\Downloads\yessirr.csv'

# Add tornado tracks from CSV
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        start_lat = float(row['start_lat'])
        start_lon = float(row['start_lon'])
        end_lat = float(row['end_lat'])
        end_lon = float(row['end_lon'])
        EF = row['EF']

        # Create a line feature
        feature = QgsFeature()
        line = QgsGeometry.fromPolylineXY([QgsPointXY(start_lon, start_lat), QgsPointXY(end_lon, end_lat)])
        feature.setGeometry(line)
        feature.setAttributes([EF])
        
        pr.addFeature(feature)

# Update the layer's extents 
layer.updateExtents()
QgsProject.instance().addMapLayer(layer)

# Define the color and line thickness for each EF scale
symbol = layer.renderer().symbol()
symbol.setWidth(1.5)  # Set line thickness 

categories = []

# Define color and style for each EF category
ef_colors = {
    'U': QColor(169, 169, 169),  # EF Unknown - Light Grey
    '0': QColor(0, 255, 255),    # EF-0 - Bright Teal
    '1': QColor(0, 255, 0),      # EF-1 - Green
    '2': QColor(255, 255, 0),    # EF-2 - Yellow
    '3': QColor(255, 165, 0),    # EF-3 - Orange
    '4': QColor(255, 0, 0),      # EF-4 - Red
    '5': QColor(255, 105, 180)   # EF-5 - Pink
}

for ef, color in ef_colors.items():
    # Create a category for each EF scale 
    category = QgsRendererCategory(ef, QgsSymbol.defaultSymbol(layer.geometryType()), f"EF-{ef}")
    category.symbol().setColor(color)
    category.symbol().setWidth(1.5)  # Adjust thickness 
    categories.append(category)

# Set categorized renderer
renderer = QgsCategorizedSymbolRenderer("EF", categories)
layer.setRenderer(renderer)

# Refresh layer to apply new styling
layer.triggerRepaint()
