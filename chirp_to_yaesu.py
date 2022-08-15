#!/usr/bin/env python

import csv
import argparse

def addEmptyLine(foo, lineNumber):
    templine = str(lineNumber) + ",,,,,,,,,,,,,,0,,0"
    foo.append(templine.split(","))
    return foo

# Adding the command line flags
parser = argparse.ArgumentParser(description="This tool converts a chirp csv file to a Yaesu importable csv file.")
parser.add_argument('--input', '-i', required = True)
parser.add_argument('--output', '-o', default="Yaesu-import.csv")
parser.add_argument('--band', '-b', default='A', choices = ['A', 'B'], help='Specify the A or B band')
args = parser.parse_args()

ftline = []
chirpFile = []
numlines = 0
inputFile = args.input
outputFile = args.output
if args.band == 'A':
    band = "0"
else :
    band = "1"

# Open the Chirp file and create the Yaesu formatted array
with open(inputFile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Location"] == "0":  # TD skip bad chirp CSV export defaults
            continue
        while numlines + 1 != int(row["Location"]): # TD skip missing lines in input, preserve holes!
            numlines += 1
            chirpFile = addEmptyLine(chirpFile, numlines)
        if row["Tone"] in ("Tone", "TSQL") or (row['Frequency'] != None and row["Tone"] == ''):
            numlines += 1
            ftline.append(str(numlines))
            ftline.append(row['Frequency'])
            if row['Offset'] == "OFF":
                ftline.append(row['Frequency'])
            else :
                freq = float( row['Frequency'] )
                if row['Duplex'] == "-" :
                    freq = freq - float( row['Offset'] )
                elif row['Duplex'] == "+":
                    freq = freq + float( row['Offset'] )
                ftline.append(str(freq))
            ftline.append(row['Offset'])
            if row['Duplex'] in [ '+', '-' ] :
                ftline.append(row['Duplex'] + "RPT")
            else :
                ftline.append( "OFF" )
            ftline.append(row['Mode'])
            ftline.append(row['Name'][0:8])
            if row["Tone"] == "Tone" :
                ftline.append("TONE ENC")
            elif row["Tone"] == "TSQL" :
                ftline.append("TONE SQL")
            else :
                ftline.append("OFF")
            ftline.append(row['rToneFreq'] + " Hz")
            ftline.append(row['DtcsCode'])
            ftline.append("1500 Hz")
            ftline.append("HIGH")
            ftline.append("OFF")
            if row['Mode'] == "NFM":
                ftline.append("12.5KHz")
            else :
                ftline.append("25.0KHz")
            ftline.append("0")
            ftline.append(row['Comment'])
            ftline.append(band)

            chirpFile.append(ftline)
            ftline = []
        else:
            # If it's not Tone, Don't do anything now, just add an empty line
            # This will have to handle DCS stuff one day.
            numlines += 1
            chirpFile = addEmptyLine(chirpFile, numlines)

# For some reason Yaesu import CSV file expects 500 lines,
# filling the rest with empty lines here

for line in range(numlines+1, 501):
    chirpFile = addEmptyLine(chirpFile, line)

# Writing the file to Yaesu importable CSV file.
with open(outputFile, "w") as csvWriter:
    writer = csv.writer(csvWriter, delimiter=",")
    for line in chirpFile:
        writer.writerow(line)
