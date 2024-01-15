# FDR

This Python script reads data captured by the CAN_Listener and writes it into a flat file (.csv) into the ~/fdr_data/ folder at preconfigured intervals

Prerequisites:
CAN_Listeners script running https://github.com/ExperimentalAvionics/can_listener

## Release Notes: ##

### 2024-01-15 ###
* Added code to handle the timing issue when the "messages" table is not created yet when the FDR is trying to read it.

### 2021-10-20 ###
* Changed the way filename created. Now a new log file will be created every time the system started. New filename structure: fdr_YYYY-MM-DD_HHMISS.csv

### 2021-06-17 ###
* Minor change: log frequency chnged from 5 seconds to every 2 seconds
