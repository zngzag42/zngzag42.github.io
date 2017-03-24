# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import sys, getopt, os, shutil
import codecs
import string

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
    writeTOC(classes, outputdir, dirsUMD, 'Greenberg\'s Notes', lambda path, s: s + u"/toc.html", lambda path, s: s, "simplestyle.css", "", "")

    for dir in os.listdir(outputdir):
        dirpath = outputdir + dir
        if os.path.isdir(dirpath):
            toc = codecs.open(dirpath + '/'  + 'toc.html', 'w', encoding='utf-8')
            pages = [page for page in os.listdir(dirpath) if page.isdigit()]
            pages.sort(key = int)
            writeTOC(toc, dirpath, pages, dir, lambda path, s: s + u"/index.html", findPageTitle, "../simplestyle.css", "../classes.html", "Classes")

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
    for dirunder in os.listdir(dst):
        pagepath = os.path.join(dst,dirunder)
        if os.path.isdir(pagepath):
            indexfile = open(os.path.join(dst,dirunder) + "/index.html", "r")
            outindexfile = open(os.path.join(dst,dirunder) + "/index.html.tmp", "w")
            title = findPageTitle(dst,dirunder)
            writeIndex(indexfile, outindexfile,title)
            os.rename(os.path.join(dst,dirunder) + "/index.html.tmp", os.path.join(dst,dirunder) + "/index.html")

def writeIndex(infile, outfile,title):
    tab = u"    "
    for line in infile:
        if line.find("page.js") >= 0:
            outfile.write(tab + u"<script type=\"text/javascript\" src=\"../../page.js\"></script>" + u"\n")
        elif line.find("<head>") >= 0:
            outfile.write(line)
            titleline = tab + u"<title>" +  title +  u"</title>" + u"\n"
            outfile.write(titleline.encode('utf-8'))
        else:
            outfile.write(line)

def writeTOC(file, path, dirs, title, fDir, fName, stylelink, backlink, backname):
    tab = u"    "
    file.write(u"<html>" + u"\n")
    file.write(u"<link rel=\"stylesheet\" href=\""+ stylelink + "\">" + u"\n")
    file.write(tab + u"<h1>" + title + u"</h1>" + u"\n")
    if not(len(backlink) == 0):
        file.write(tab + u"<a href=\"./" + backlink + u"\">" + backname + u"</a>" + u"\n")
    file.write(tab + u"<ul>" + u"\n")
    for dir in dirs:
        file.write(tab*2 + u"<li>" + u"<a href=\"./" + fDir(path, dir) + u"\">" + fName(path, dir) + u"</a>" + u"</li>" + u"\n")
    file.write(tab + u"</ul>" + u"\n")
    file.write(u"</html>" + u"\n")




if __name__ == "__main__":
    main(sys.argv[1:])
