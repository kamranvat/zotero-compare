# zotero-compare
Simple script that compares two zotero folders (exported as .json) and tells you how many titles occur in both of them.

## What it does
The script can either be used to check for common titles between two exported Zotero folders, or check for duplicates within a single one. 
Either way, it will print the respective number of titles as well as the titles themselves to the console.
## How to use
### Get folders:
- Clone this repository to your device
- Open Zotero and right-click a folder of your choice
- Click ```Export Collection...```, make sure the format is set to ```CSL JSON```
- Save the exported file into the ```./jsons``` directory of this repository
- Repeat for at least one more folder
  
### Check for common titles:
- Run ```python compare.py``` from your console in the directory of this repo to compare two .json files
- If you have more than two files in the folder, you will be prompted to choose which files to compare

### Check for duplicates within a file:
- To check for duplicates within a file, run ```python compare.py -d```
- All files will be checked and their respective number of duplicates, as well as the titles, will be printed.
