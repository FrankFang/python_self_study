# -*- coding: utf-8 -*-
import os
import shutil
import re
import sys
import chardet
import codecs

def convertToUtf8(srcDir,desDir):
  suffixiList = ('.shtml','.html','.css','.js')
  dirDict = os.walk(srcDir)
  for root,dirs,files in dirDict:
    for aFilePath in files if aFilePath.endswith(): 
      oldPath =  os.path.join(root,aFilePath)
      newPath = oldPath.replace(srcDir,desDir)
      tempPath = newPath+'.temp'
      newDir = root.replace(srcDir,desDir)
      if not os.path.exists(newDir):
        os.mkdir(newDir)

      shutil.copyfile(oldPath,tempPath)
      tempFile = codecs.open(tempPath)
      content = tempFile.read()
      tempFile.close()
      os.remove(tempPath)
      oldEncoding = chardet.detect(content)['encoding']
      content = content.decode(oldEncoding)
      codecs.open(newPath,'w',encoding='utf8').write(content)
      print('  converted successfully from '+oldEncoding+': '+newPath)

def main():
  srcDir = sys.argv[1]
  desDir = sys.argv[2]
  if not os.path.exists(desDir):
    os.mkdir(desDir)

  convertToUtf8(srcDir,desDir)
  print('Done :)')

if __name__ == '__main__':
  main()

