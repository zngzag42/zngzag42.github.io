target:
	python bin/makeHTMLnotes.py -i ../Dropbox/NotesPlus/AutoBackup/Notebooks/ -o ./
	-rm ./Makefile~
	git add *
	git commit -m "Updated Webpage"
	git push

test:
	python bin/makeHTMLnotes.py -i ../Dropbox/NotesPlus/AutoBackup/Notebooks/ -o ./
