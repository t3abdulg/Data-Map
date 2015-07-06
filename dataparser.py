"""
Programmed By: Tawfeeq Abdul Gaffoor
"""

import csv
import json
import math

popdata = []
areadata = []
a = []

def zeroOrint(string):
    if string:
        return int(round(float(string)))
    else:
        return 0
    
    
with open('CountryInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open ('PopData.js' , 'a') as file:
        file.write("var PopulationData ={};");
        file.write("\n")
        file.close();
    for row in reader:
        if row[' Coord']:   
            with open ('PopData.js' , 'a') as file:
                file.write("PopulationData." + str(row['ISO 3166-1 A2']) + ' =')
                file.write ("[")
                file.write(str({'Title' : "Non-Urban", "data" : zeroOrint(row[' Population']) - zeroOrint(row[' Urban Population']) }))
                file.write(",")
                file.write(str({'Title' : "Urban", "data" : row[' Urban Population']}))
                file.write ("];") 
                
                
with open('CountryInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open ('InitData.js' , 'a') as file:
            file.write("var dataSets = [[");
            file.write("\n")
            file.close();    
    for row in reader:
        if row[' Coord']:         
            with open ('InitData.js' , 'a') as file:
                file.write(json.dumps({"id" : str(row['ISO 3166-1 A2']), "value" : zeroOrint(row[' Population']), "selectable" : True}, sort_keys = True, separators = (',', ':')))
                file.write(",")
                file.close()
    with open ('InitData.js' , 'a') as file:
        file.write("]]")
        file.close()
                

with open('CountryInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open ('AreaData.js' , 'a') as file:
                file.write("var AreaData ={};");
                file.write("\n")
                file.close();     
    for row in reader:
        if row[' Coord']:   
            with open ('AreaData.js' , 'a') as file:
                file.write("AreaData." + str(row['ISO 3166-1 A2']) + ' =')
                file.write ("[")
                file.write(str({'Title' : "Land", "data" : zeroOrint(row[' Land (sq km)'])}))
                file.write(",")
                file.write(str({'Title' : "Water", "data" : zeroOrint(row[' Water (sq km)'])}))
                file.write ("];") 
                
                
with open('CountryInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open ('GDPData.js' , 'a') as file:
        file.write("var GDPData= {};")
        file.write("\n")
        file.close()
    for row in reader:
        if row[' Coord']:   
            with open ('GDPData.js' , 'a') as file:
                file.write("GDPData." + str(row['ISO 3166-1 A2']) + ' =')
                file.write ("[")
                file.write(str({'Area' : "World", "GDP" : 13100}))
                file.write(",")
                file.write(str({'Area' : str(row['ISO 3166-1 A2']), "GDP" : zeroOrint(row[' GDP'])}))
                file.write ("];")   


with open('CountryInfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open ('BRData.js' , 'a') as file:
        file.write("var BRDData ={};")
        file.write("\n")
        file.close
    for row in reader:
        if row[' Coord']:   
            with open ('BRData.js' , 'a') as file:
                file.write("BRDData." + str(row['ISO 3166-1 A2']) + ' =')
                file.write ("[")
                file.write(str({'title' : "Death", "value" : str(row[' Death ( per 1000)'])}))
                file.write(",")
                file.write(str({'title' : "Birth", "value" : str(row[' Birth (per 1000)'])}))
                file.write ("];") 
                



    





