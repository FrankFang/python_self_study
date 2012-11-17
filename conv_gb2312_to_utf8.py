# -*- coding: utf-8 -*-
import os
import shutil
import re
import sys
import chardet
import codecs

def getFileListToConvert( dir ):
    filelist = {}
    for root, dirs, files in os.walk(dir):
        filelist[root] = []
        for f in files:
            fullpath = os.path.join(root,f)
            filelist[root].append(fullpath)
    return filelist;

def convToUtf8To(srcDir,desDir):
    filelist = getFileListToConvert(srcDir) 
    for r in filelist:
        for f in filelist[r]:
            newFile = desDir + f.replace(srcDir,'/') 
            maniFile = newFile + '.temp'
            if not os.path.exists(r.replace(srcDir,desDir)):
                os.mkdir(r.replace(srcDir,desDir))
            shutil.copyfile(f, maniFile)
            oldFile = codecs.open(maniFile,'r')
            content = oldFile.read()
            oldFile.close()
            os.remove(maniFile)
            oldEncoding = chardet.detect(content)['encoding']
            content = content.decode(oldEncoding)
            codecs.open(newFile,'w',encoding='utf8').write(content)
            print 'converted to: ' , newFile

def main():
    srcDir = sys.argv[1]
    desDir = sys.argv[2]
    if not os.path.exists(desDir):
        os.mkdir(desDir)

    convToUtf8To(srcDir,desDir)
    print('Done')

def process_bak_files(action='restore'):
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if f.lower().endswith('.java.bak'):
                source = os.path.join(root, f)
                target = os.path.join(root, re.sub('\.java\.bak$', '.java', f, flags=re.IGNORECASE))
                try:
                    if action == 'restore':
                        shutil.move(source, target)
                    elif action == 'clear':
                        os.remove(source)
                except Exception, e:
                    print source

if __name__ == '__main__':
    # process_bak_files(action='clear')
    main( )
