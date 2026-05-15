# Hurricane Milton Tornado Outbreak Analysis

This project consolidated fragmented National Weather Service tornado survey data following Hurricane Milton into a unified statewide GIS visualization.


Following Hurricane Milton’s tornado outbreak across Florida, I noticed that individual National Weather Service forecast offices were publishing tornado survey maps and damage tracks separately within their own county warning areas (CWAs). While each office provided detailed local surveys, there was no single statewide visualization showing the full extent of the outbreak at the time.

To address this, I consolidated fragmented tornado survey data from multiple National Weather Service Public Information Statements (PNS products) into a unified statewide GIS visualization.

Using Python, PyQGIS, and QGIS, tornado survey coordinates and EF-scale metadata were extracted from operational NWS survey products, organized into a structured CSV dataset, and converted into geospatial tornado-track layers.

The resulting map visualized 39 surveyed tornado tracks identified during the operational post-event survey process across Florida.

Subsequent National Weather Service survey updates later increased the finalized statewide tornado count to 46. This project reflects the operational survey dataset available during the original analysis period.

Hurricane Milton produced the largest documented tornado outbreak associated with a tropical cyclone in modern Florida records, surpassing previous outbreaks such as Hurricane Irma (2017). The outbreak included multiple EF3 tornadoes and widespread tornadic damage across central and southern Florida.



## Workflow

1. Extracted tornado survey metadata from NWS AFOS/PNS products archived through the Iowa State Mesonet.

2. Organized tornado coordinates, EF ratings, and survey metadata into a structured CSV dataset.

3. Used QGIS to integrate tornado-track data with geospatial basemaps, county boundaries, and statewide geographic context layers.

4. Developed a PyQGIS Python workflow to automate tornado-track generation from coordinate-based CSV data.

5. Created geospatial line features representing tornado paths and symbolized tracks by EF intensity within QGIS.

6. 6. Produced a finalized statewide GIS visualization using QGIS layout and mapping tools.


## Tools Used

- Python
- PyQGIS
- QGIS
- CSV datasets
- Iowa State Mesonet AFOS archive
- National Weather Service survey data


## Final Map

![Milton Tornado Map](final_map/milton_tornado_outbreak_map.png)


## Data Sources

Survey information was compiled from National Weather Service Public Information Statements (PNS products) archived through the Iowa State Mesonet.

Primary forecast offices included:

- Melbourne, FL (KMLB)
- Miami, FL (KMFL)
- Tampa Bay/Ruskin, FL (KTBW)

Example archive sources:

- https://mesonet.agron.iastate.edu/wx/afos/p.php?pil=PNSMLB
- https://mesonet.agron.iastate.edu/wx/afos/p.php?pil=PNSMFL
- https://mesonet.agron.iastate.edu/wx/afos/p.php?pil=PNSTBW
- https://mesonet.agron.iastate.edu/wx/afos/p.php?pil=PNSJAX


## Project Goals

This project was designed to explore how geospatial tools and automation can improve the visualization and communication of fragmented operational meteorological survey data.
