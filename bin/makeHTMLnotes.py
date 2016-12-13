# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import sys, getopt, os, shutil
import codecs

def main(argv):
    inputdir = ''
    outputdir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["idir=","odir="])
    except getopt.GetoptError:
        print 'test.py -i <inputdir> -o <outputdir>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputdir> -o <outputdir>'
            sys.exit()
        elif opt in ("-i", "--idir"):
            inputdir = arg
        elif opt in ("-o", "--odir"):
            outputdir = arg

    print 'Input directory is ', inputdir
    print 'Output directory is ', outputdir


    dirsUMD = [dir for dir in os.listdir(inputdir) if dir.split()[0].isdigit()]
    dirsUMD = [expandDirAndMove(inputdir, dir, outputdir) for dir in dirsUMD]
    dirsUMD = [dir for sublist in dirsUMD for dir in sublist]
    dirsUMD.sort();

    print dirsUMD

    classes = open(outputdir + 'classes.html', 'w')
    writeTOC(classes, outputdir, dirsUMD, 'Greenberg\'s Notes', lambda path, s: s + u"/toc.html", lambda path, s: s)

    for dir in os.listdir(outputdir):
        dirpath = outputdir + dir
        if os.path.isdir(dirpath):
            toc = codecs.open(dirpath + '/'  + 'toc.html', 'w', encoding='utf-8')
            pages = [page for page in os.listdir(dirpath) if page.isdigit()]
            pages.sort(key = int)
            writeTOC(toc, dirpath, pages, dir, lambda path, s: s + u"/index.html", findPageTitle)

def findPageTitle(path, dir):
    page = ET.parse(path + '/' + dir + '/'  + 'meta.xml').getroot()
    name = page.get('name')
    if len(name) == 0:
        return u"Untitled"
    else:
        return page.get('name')

def expandDirAndMove(prefix, dir, outdir):
    predir = dir.split()[0]
    if len(predir) == 4:
        dirsunder = os.listdir(os.path.join(prefix,dir))
        for dirunder in dirsunder:
            copyOver(prefix + dir + '/' + dirunder, os.path.join(outdir,dirunder))
        return dirsunder
    else:
        copyOver(prefix + dir, os.path.join(outdir, dir))
        return [dir]

def copyOver(src, dst):
    print 'Trying to copy to ' + dst
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(src,dst)

def writeTOC(file, path, dirs, title, fDir, fName):
    tab = u"    "
    file.write(u"<html>")
    file.write(tab + u"<h1>" + title + u"</h1>")
    file.write(tab + u"<ul>")
    for dir in dirs:
        file.write(tab*2 + u"<li>" + u"<a href=\"./" + fDir(path, dir) + u"\">" + fName(path, dir) + u"</a>" + u"</li>")
    file.write(tab + u"</ul>")
    file.write(u"</html>")




if __name__ == "__main__":
    main(sys.argv[1:])
