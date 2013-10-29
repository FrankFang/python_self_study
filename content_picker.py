# -*- coding: utf-8 -*-
from __future__ import print_function
from nvd3 import pieChart
import re
import urllib2

__author__ = 'frank'

page = urllib2.urlopen('http://www.cnblogs.com/seer/p/3395888.html').read() + '<link href=xxxx>'


def convert(_page):
    return _page


def get_page_charset(_page):
    return _page


charset = get_page_charset(page)
page_in_utf8 = convert(page)


def consistent_newline(_str):
    return _str.replace('\r\n', '\n').replace('\r', '\n')


def wipe_html_tags(_page_in_utf8):
    my_flag = re.IGNORECASE
    _content = re.sub(r'<!DOCTYPE.*?>', '', _page_in_utf8, flags=my_flag)
    _content = re.sub(r'<(\s|/)*?html.*?>', '', _content, flags=my_flag)
    _content = re.sub(r'<\s*?head.*?>(.*?\n)+.*?</+?head>', '', _content, flags=my_flag)
    _content = re.sub(r'<.*?link[^\n]*', '', _content, flags=my_flag)
    _content = re.sub(r'<\s*?script.*?>(.|\n)*?</+?script.*?>', '', _content, flags=my_flag)
    _content = re.sub(r'<\s*?style.*?>(.|\n)*?</+?style.*?>', '', _content, flags=my_flag)
    _content = re.sub(r'<!--(.|\n)*?-->', '', _content, flags=my_flag)
    _content = re.sub(r'&.{1,5};|&#.{1,5};', '', _content, flags=my_flag)
    _content = re.sub(r'<.*?>', '', _content, flags=my_flag)
    _content = re.sub(r'$\s*?\n', '\n', _content, flags=my_flag)
    return _content


page_with_consistent_newline = consistent_newline(page_in_utf8)
page_without_html_tag = wipe_html_tags(page_with_consistent_newline)

lines = page_without_html_tag.split('\n')

block_length_array = [len(a) + len(b) + len(c) for a, b, c in zip(lines, lines[1:], lines[2:])]

#print ([(bl, lines[index]) for index, bl in enumerate(block_length_array)])

#print(block_length_array)

content = ''
start = 0
end = 0
for index, block_length in enumerate(block_length_array):
    #print(index, block_length)
    current_content = ''
    current_start = index
    for index2, block_length2 in enumerate(block_length_array[index:]):
        #print('-', index2, block_length2)
        if block_length2 != 0:
            current_content += lines[index + index2] + '\n'
        else:
            #print('block_length ', block_length2)
            #print(index2, '-', lines[index2])
            current_end = index2
            break
    if len(current_content) > len(content):
        start = current_start
        end = current_end
        content = current_content

#print(start)
#print(end)
print(content)

output_file = open('/Users/frank/test/test.html', 'w')

header = 'pieChart'
chart = pieChart(name=header, color_category='category20c', height=450, width=450)
chart.set_containerheader("\n\n<h2>" + header + "</h2>\n\n")

#Create the keys
xdata = range(0, len(block_length_array))
ydata = block_length_array

#Add the serie
extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
chart.buildhtml()
output_file.write(chart.htmlcontent)

#close Html file
output_file.close()