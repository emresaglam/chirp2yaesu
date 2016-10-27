import csv
import argparse

parser = argparse.ArgumentParser(description="This tool converts a chirp csv file to a Yaesu importable csv file")
parser.add_argument('--input', '-i', required = True)
parser.add_argument('--output', '-o', default="Yaesu-import.csv")
args = parser.parse_args()


ftline = []
numlines = 0
with open(args.input) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Tone"] == "Tone":
                numlines = int(row['Location'])+1
                ftline.append(str(numlines))
                ftline.append(row['Frequency'])
                ftline.append('')
                ftline.append(row['Offset'])
                ftline.append(row['Duplex'] + "RPT")
                ftline.append(row['Mode'])
                ftline.append(row['Name'])
                ftline.append("TONE ENC")
                ftline.append(row['rToneFreq'] + " Hz")
                ftline.append(row['DtcsCode'])
                ftline.append("1500 Hz")
                ftline.append("HIGH")
                ftline.append("OFF")
                ftline.append("25.0KHz")
                ftline.append("0")
                ftline.append(row['Comment'])
                ftline.append("0")

                print ",".join(ftline)
                ftline = []
        else:
            # If it's not Tone, Don't do anything now, just add an empty line
            # This will have to handle DCS stuff one day.
            print str(numlines+1) + ",,,,,,,,,,,,,,0,,0"

for line in range(numlines+1, 501):
    print str(line) + ",,,,,,,,,,,,,,0,,0"
