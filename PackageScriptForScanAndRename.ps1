# this is the script to package python scripts into a portable .exe. make changes as needed. 
pyinstaller `
--clean <#fresh package, doesn't use existing files. This gives a permissions error if the working directory isn't cleaned#> `
--onefile <#this line ensures just one singe .exe#>`
--debug=imports <# this line adds logging to the building process#>`
--hidden-import=pyzbar.pyzbar `
--hidden-import=fitz.frontend `
--hidden-import=fitz.tools `
--hidden-import=fitz.commandline `
--add-binary "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\scanner\libzbar-64.dll;." `
--add-binary "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\scanner\libiconv.dll;." `
--add-binary "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\scanner\msvcp120.dll;." `
--distpath "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\temp" `
--workpath "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\temp" `
scanAndRenameWithCleanup.py