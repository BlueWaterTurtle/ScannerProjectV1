I've figured out how to rename files and successfully added the code. Now I need to figure out how to duplicate and name the file. I'll have to do this in a new directory as the "waves" directory will trigger the "rename" code if I add anything to it. 

Ignore what's above. 
This script will pull information from a scanned image and add that as a pdf to the "finished Waves" folder, using the information decoded from the barcode to name the document

code has been added to ensure these documents will not be overwritten. 

I added a delay to the initial conversion, I had to because the scanner seems like it didn't let go of the file, or maybe it just didn't finish with the file in a timely enough manner and the script just didn't do anything with the file. Adding a 5 second delay fixed the issue. 
