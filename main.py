'''
HOW IT WORKS?

-> 
'''

from flask import Flask,render_template,request,flash,url_for
import json,os
from werkzeug.utils import secure_filename
from features.extract_pdf import pdf2string as p2s


app =Flask(__name__)
#Default Home page
@app.route('/')
def index():
    return render_template('index.html')

#when you start with search
@app.route('/search', methods=['POST'])
def submit():
    if request.method == 'POST':
        inp_text=str(request.form.get('inputtext'))
        find =str(request.form.get('searchtext'))
        splitter=extract()
        splitter.split_paragraph(inp_text)
        finder=search_engine(splitter)
        
        ret=finder.search(find.lower())
        return json.dumps(ret)

#file upload happens here and files are stores in github repository
@app.route("/handleUpload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    res=p2s.convert_file(f.filename)
    
    return render_template('index.html', disp=res)
class extract:
    def __init__(self):
        self.index=1
        self.word_dictionary=dict()
    
        
    def split_paragraph(self,inline_text):
        
        text=inline_text.rstrip().split("\r\n")
        
        for tokenize in text:
            
            if tokenize=='':
                continue
            self.seperate_text(tokenize,self.index)
            self.index+=1
            
        
    def seperate_text(self,text,ind):
        text=text.lower()
        
        
        for token in text.split():
            if token[-1] in [",",".","!",":",";"]:
                token=token[:-1]


            if token not in self.word_dictionary.keys():
                self.word_dictionary[token]={"paragraph":[ind],"frequency":[1]}
                
            elif ind not in self.word_dictionary[token]["paragraph"]:
                
                self.word_dictionary[token]["paragraph"].append(ind)
                self.word_dictionary[token]["frequency"].append(1)
            else:
                
                index_finder=len(self.word_dictionary[token]["frequency"])-1
                self.word_dictionary[token]["frequency"][index_finder]+=1
        
    def clear_index(self):
        self.word_dictionary.clear()
        return self.word_dictionary

class search_engine:
    
    def __init__(self,db):
        self.data_base=db.word_dictionary
        self.not_found={"result":"Not found"}
   
    def search(self,searcher):
        #print(self.data_base)
        if searcher not in self.data_base.keys():
            return self.not_found
        
        return self.data_base[searcher]
        
if __name__ == "__main__":
    app.secret_key = 'Access-TheYk-Tapsearch'
    app.debug=True
    app.run()
    
    
    
    
    
    
    
    
    
    
   