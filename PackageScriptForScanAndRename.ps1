# this is the script to package python scripts into a portable .exe. make changes as needed. 
 #I found out that if you want to use separate lines for scripts like this one you need to add a "`" to the end of the line. It's important to know that you need to make sure it the last character on the line, not even a space can follow. I'm sure a comment can't follow either, but I'm not really sure. Better not take the chance. 
pyinstaller `
--clean <#fresh package, doesn't use existing files. This gives a permissions error if the working directory isn't cleaned#> `
--onefile <#this line ensures just one singe .exe#>`
--debug=imports <# this line adds logging to the building process#>`
--hidden-import=pyzbar.pyzbar `
--hidden-import=fitz.frontend `
--hidden-import=fitz.tools `
--hidden-import=fitz.commandline `
--add-binary "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\scanner\libzbar-64.dll;." <# Ensure this dll is pulled into the package. I used this as a temporary directory just for this script, same with the two lines below. #> `
--add-binary "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\scanner\libiconv.dll;." `
--add-binary "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\scanner\msvcp120.dll;." `
--distpath "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\temp" <# This line and teh below are likely not necessary, I've added them because I was getting a permissions issue. I beleive the issue was related to the "--clean" parameter above. #> `
--workpath "C:\Users\ToddBonner\OneDrive - Levata\Documents\.Useful Scripts\temp" `
scanAndRenameWithCleanup.py
