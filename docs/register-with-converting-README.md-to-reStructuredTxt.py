import pandoc
import os

doc = pandoc.Document()
doc.markdown = open('README.md').read()
with open('README.txt','w+') as f:
    f.write(doc.rst)
os.system("python setup.py register")
os.remove('README.txt')
