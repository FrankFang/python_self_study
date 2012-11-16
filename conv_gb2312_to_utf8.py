# -*- coding: utf-8 -*-
import os
import shutil
import re
import sys
import chardet

print(chardet.detect(open("./gb2312/demo.txt").read()));
