This code converts Chirp export file in CSV format to Yaesu's import CSV format. (I only tested this on [FTM-400XDR application](https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=249&encProdID=227201D29C822AEFF8482F3367495319&DivisionID=65&isArchived=0))

Use this code at your own discretion. It's not tested on all Yaesu programs.

# HOW

1. Download Chirp and create a station list. 
2. Export this station as a CSV file. (You can name it Chirp-export.csv)
3. Download the chirp2yaesu package from github.com
4. Run it as: python chirp_to_yaesu.py -o Yaesu-import.csv -i Chirp-export.csv
5. Use Yaesu-import.csv file to import the configuration in the Yaesu's own software.

I'll have some screenshots soon.

# TODO

- So far only Tone mode is supported, add DTCS, etc...
- Better error handling
 
# SOFAR

- Fixed a problem with enabling Tone SQL mode. (TONE ENC)
- Added basic argument parsing
- Better code commenting
- Add better csv writing
