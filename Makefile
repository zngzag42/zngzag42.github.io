#notesSource = ../Dropbox/NotesPlus/AutoBackup/Notebooks/
notesSource = ~/Library/Mobile\ Documents/iCloud~com~viettran~NotePlus/Documents/Notebooks/

target:
	python bin/makeHTMLnotes.py -i $(notesSource) -o ./
	-rm ./Makefile~ || true
	git add *
	git commit -m "Updated Webpage"
	git push publish || true
	git push


test:
	python bin/makeHTMLnotes.py -i $(notesSource) -o ./
