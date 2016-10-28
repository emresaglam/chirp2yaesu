This code converts Chirp export file in CSV format to Yaesu's import CSV format. (I only tested this on FTM-400XDR application)

Use this code at your own discretion. It's not tested on all Yaesu programs.

# TODO

- So far only Tone mode is supported, add DTCS, etc...
- Better error handling
 
# SOFAR

- Fixed a problem with enabling Tone SQL mode. (TONE ENC)
- Added basic argument parsing
- Better code commenting
- Add better csv writing