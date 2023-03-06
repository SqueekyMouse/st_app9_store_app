import pandas as pd
from fpdf import FPDF
# commit: implemented article, invoice classes Sec41

df=pd.read_csv('articles.csv',
               dtype={'id':str,'name':str,'price':float,'in stock':int})


class Article:
    def __init__(self,art_id) -> None:
        self.art_id=art_id
        self.name=df.loc[df['id']==art_id,'name'].squeeze().title()
        self.price=df.loc[df['id']==art_id,'price'].squeeze()
    
    def availability(self):
        stock=df.loc[df['id']==self.art_id,'in stock'].squeeze()
        if stock>0:
            return(True)
        else:
            return(False)

    def buy(self):
        stock=df.loc[df['id']==self.art_id,'in stock'].squeeze()
        df.loc[df['id']==self.art_id,'in stock']=stock-1
        df.to_csv('articles.csv',index=False)


class Invoice:
    def __init__(self,article) -> None:
        self.article=article
        
    def print(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr. {self.article.art_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")
        print("Invoice printed")


print(df)
article_id=input('Enter article id to purchase: ')
article=Article(art_id=article_id)

if article.availability():
    article.buy()
    invoice=Invoice(article)
    invoice.print()
else:
    print('Item not avaialable.')