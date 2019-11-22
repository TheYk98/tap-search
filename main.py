from flask import Flask
app =Flask(__name__)
@app.route('/')
def index():
    return "<h1>#Theyk</h1>"

class extract:
    def __init__(self):
        self.index=1
        self.inverted_index=dict([])
    
        
    def split_paragraph(self,inline_text):
        #on asuumption that there is an equal spaced paragraph
        text=inline_text.split("\n\n")
        for tokenize in text:
            self.seperate_text(tokenize,self.index)
            self.index+=1

        
            
    def seperate_text(self,string,index):
        string=string.lower()
        freq=1
        for token in string.split():
            #if the token isn't present, add to the dictionary           
            if token not in self.inverted_index.keys():
                self.inverted_index[token]=[[index,freq]]
            #increase the frequency if it belongs to the same para
            
            elif index<=len(self.inverted_index[token]) and self.inverted_index[token][index-1][0]==index:
                self.inverted_index[token]=[[index,self.inverted_index[token][index-1][1]+1]]
            
            #else, append the frequency and para id
            else:
                self.inverted_index[token].append([index,freq])
        #print(self.inverted_index)
    
    def clear_index(self):
        self.inverted_index.clear()
        return self.inverted_index

class search_engine:
    def __init__(self,db):
        self.data_base=db
    def search(self,searcher):
        if searcher not in self.data_base.keys():
            return "{\"error\":\"Not found\"}"
        return self.data_base[searcher]
        
if __name__ == "__main__":
    obj=extract()
    file=open("sample.txt")
    text2=file.read()
    obj.split_paragraph(text2)
    text_recog=search_engine(obj.inverted_index)
    



