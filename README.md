# Rename files
A function to rename consecutively numbered files in a directory by padding with zeros to ensure consistent filename numbering length.

For example, the following files are renamed:

| From | To |
|:---- |:-- |
|photo-1.jpg|photo-01-jpg|
|photo-2.jpg|photo-02-jpg|
|photo-3.jpg|photo-03-jpg|
|photo-edited-1.jpg|photo-edited-01.jpg|
|photo-edited-2.jpg|photo-edited-02.jpg|
|photo-edited-3.jpg|photo-edited-03.jpg|

The separator string and amount of padding can be changed. In the example above, a hyphen ('-') identifies the ending counter suffix, and the numbers are padded to two-digits. The results of the files renamed and not renamed are outputted.

The following are example filenames that would not be renamed (with a specified padding of 2 and a hypen as the separator string):
- photo.jpg
- photo-ver2.jpg
- photo-23.jpg
- photo-.jpg

All files in all subdirectories of the specified directory can also be chosen to be renamed. Directories are not renamed.
