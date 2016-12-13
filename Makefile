target:
	python bin/makeHTMLnotes.py -i ../Dropbox/NotesPlus/AutoBackup/Notebooks/ -o ./
	git add *
	git commit -m "Updated Webpage"
	git push
