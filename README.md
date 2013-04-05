ST2-plugin-Insert-File-Here
===========================

This is a plugin for Sublime Text 2 (OSX Mountain Lion) that inserts the contents of a file / template (e.g., *.txt, *.tex, etc.) at the current caret position.  The form files need to be LF endings, not CR, and I used UTF-8 encoding in my testing.

It is an unofficial modification of https://github.com/mneuhaus/SublimeFileTemplates

Having been word processing for the past quarter century, I missed the "insert file here" feature in ST2.  I did not want to convert my entire form file directory into snippets or xml files (incorporating the contents of my forms, or referencing the paths to my own forms).

With this plugin, my form files can remain anywhere I choose and modified directly wtihout the need to fiddle with snippets.  I do use snippets, but I also enjoy simply inserting a non-snippet file at the caret position.

The only bug I see so far is the inability to translate a double-slash \\\ in the form file correctly -- it gets inserted instead as just a single-slash \\. In my LaTex form files, the double-slash \\\ represents a line ending, or a new line if preceded by a ~. I'm not yet sure how to fix it, except perhaps to insert an extra slash at each occurrence in the actual form file that I know will be inserted. The form files need to be LF endings and I'm using UTF-8 encoding -- CR endings are not translated properly.
