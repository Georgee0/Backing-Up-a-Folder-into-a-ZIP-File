# Backing-Up-a-Folder-into-a-ZIP-File

Say you’re working on a project whose files you keep in a folder. You’re worried about losing your work, so you’d
liketo create ZIP file “snapshots” of the entire folder. You’d like to keep different versions, so you want the ZIP
file’s filename to increment each time it is made; for example, filename_1.zip, filename_2.zip, filename_3.zip, and
so on. You could do this by hand, but it is rather annoying, and you might accidentally misnumber the ZIP files’ names.
It would be much simpler to run a program that does this boring task for you.

The program:
1- Figure out the Zip file's name
2- Create the new Zip file
3- Walk the Directory Tree and Add to the ZIP File
