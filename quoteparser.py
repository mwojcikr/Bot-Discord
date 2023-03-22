
from random import randint

#parsing copy pasted quotes from https://www.goodreads.com/author/quotes/879.Plato
def parse_good_reads(file,type="w",author="unknown"):        
    with open(file,"r",encoding='utf-8') as f:
        text = f.read()
        text = str(text)
        text = text.split("Like")
        for i in range(len(text)):
            text[i] = text[i].split("tags")
            text[i] = text[i][0].split("―")
    with open("quotes.txt",type,encoding="utf-8") as new:
        for quote in text:
            if len(quote[0]) > 10 :
                new.write(f"\n {quote[0]} - {author} ::")

def get_quote():   
    with open("quotes.txt","r",encoding = 'utf-8') as f:
        quotes = f.read().split("::")
        N = len(quotes)
        return quotes[randint(0,N-1)]


#def author_to_camel_case(message):
#    author = message
#    names = author.split('!addauthor ')[1].split(' ')
#    author = ''
#    for i in range(0,len(names)):
#        names[i] = names[i][0].upper() + names[i][1:len(names[i])].lower()
#        author = author + names[i] + " "
#    return author
#
#def add_author_quotes_from(name):
#    
#    pass




if __name__ == "__main__":
    pass
   

