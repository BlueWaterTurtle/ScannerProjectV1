I've figured out how to rename files and successfully added the code. Now I need to figure out how to duplicate and name the file. I'll have to do this in a new directory as the "waves" directory will trigger the "rename" code if I add anything to it. 

This script will pull information from a scanned image and add that as a pdf to the "finished Waves" folder, using the information decoded from the barcode to name the document

code has been added to ensure these documents will not be overwritten. 

I added a delay to the initial conversion, I had to because the scanner seems like it didn't let go of the file, or maybe it just didn't finish with the file in a timely enough manner and the script just didn't do anything with the file. Adding a 5 second delay fixed the issue. 


The process I settled on is to have the scanner setup to add scanned documents to "C:\users\public\documents\waves".
The document is set to be saved as .PNG because the barcode reading library was designed to read from image files not PDF's.
The script will wait 5 seconds and scan the image for barcodes and decode/store the information then add a copy to the folder "C:\users\public\documents\processedWaves", naming the document with the data decoded from the barcode. 
Finally the document is converted to .PDF and copied to the folder "C:\users\public\documents\finishedWaves" where the user will knows to look for them. 

Future versions should look to delete the documents in the "Waves" and "finishedWaves" folders after they're done being processed. Currently they'll need to be manually deleted to prevent storage capacity issues. 

I could probably reduce the delay as low as 1 or 2 seconds without issue, but, more testing will be required. 
