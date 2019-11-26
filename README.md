# Tap-search
Tap search word finder. Upload a file or copy paste any number of paragraphs no matter how many new lines you leave for each paragraph and get a api for the frequency of occurence and the paragraph number. Tap-search runs on gunicorn web server that lets multiple users access at the same time.
corn web server that lets multiple users access at the same time.
# File Upload
Tap-search uses PyPDF2 for converting pdf to texts. This is bundled up with features package that lets you to convert pdf to text no matter the number of pages.

# API
Tap-search gives you the api for the Paragraph number and the frequency of occurence in each paragraph so that you can find out if the word is present or not

## if the word is present at paragraph 1&2 with 1 time each, you get a response
```javascript
{"Paragraph":[1,2],"Frequency":[1,1]}
```
## else,
```javascript
{"Result":"Not found"}
```


# Understanding API

tap-search gives you the result as 
```javascript
{"Paragraph":[],"Frequency":[]}
```

where paragraph list index = frequency list index , so it's even more easier to find the occurence at each paragraph.

# How does it work?
The optimized search on tap-search works on inverted index. This allows you to create a in-memory database so you get a fast access to the database

# Updates
The update will be on the image processing part. Tap search will in future allows you to upload files with text as an image an expect the same speedy search.

# The code that extracts text from PDF
Tap search uses user defined package
```python
from features.extract_pdf import pdf2string 
```
pdf2string obviously is a class that contains ```convert_file()``` function ,extracts the file and concatenates all the text in all the pages of the uploaded pdf.This works under pypdf2
install pypdf2 using pip3 comand line
```python 
pip install PyPDF2
```


# Usecases
* Check your resume Compatibility
* Check if a particular word along with frequency ,is present in a file or not 

