import pandas as pd
import numpy as np
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import random
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Segoe Script', 'segoesc.ttf'))

infile = r'C:\Users\spcra\Desktop\projects\bingo cards\jettemplate_HK641516_1.pdf'


output = PdfFileWriter()

def make_bingo_cards(n):
    
    qa_dict = {'Birthday?': 'January 5th',
             'Chocolate or vanilla?': 'Chocolate',
             'Dream Job?': 'Nanny',
             'Fav alcoholic drink?': 'Lemon Drop',
             'Fav disney movie?': 'Brave',
             'Favorite actor?': 'Sydney Sweeney',
             'Favorite comedian?': 'Tom Segura',
             'Favorite dessert?': 'Flourless Chocolate cake',
             'Favorite flower?': 'Car- nations',
             'Favorite food as a kid?': 'Lobster',
             'Favorite season?': 'Winter',
             'Favorite video game?': 'Mine- craft',
             'First Job?': 'Camp Counselor',
             'Gabs favorite color?': 'Green',
             'Gabs favorite food?': 'Sushi',
             'Gabs favorite movie?': 'Mr. Right',
             'Gabs favorite show?': 'NCIS',
             'Gabs middle name?': 'Nicole',
             'Hidden talent?': 'Florist',
             'How long have Gabs and Sal been together?': '7 years',
             'How many kitty children do Gabrielle & Sal have?': '2 kitty children',
             'How many sisters does Gabrielle have?': '1 sister',
             'Job?': 'Social worker',
             'Names of their kitties?': 'Mel & Mable',
             'Type of music she loves?': 'Dance/ House',
             'Wedding date?': 'October 7th',
             'What does her family call her?': 'Gabs',
             'What is Gab’s allergic to?': 'Wheat/ Gluten',
             'What is Gab’s biggest pet peve?': 'Non turn- blinker users',
             'Where did gabs and sal meet?': 'Ithaca college',
             'Where they got engaged?': 'Atlantis, The Bahamas'}
    
    question_list = list(qa_dict.keys())
    answer_list = list(qa_dict.values())

    for i in range(n):
        
        bingo_table = random.sample(answer_list,25)
        bingo_table2 = random.sample(answer_list,25)
    
        packet = io.BytesIO()
        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont('Segoe Script', size=9.5)
        # can.drawString((.6+5.5) * inch, inch*(1.3+0), "Hello World") #.6 * inch, inch*1.3 # (.6+0.85) * inch, inch*(1.3+0.85) x+5.5 for second sheet
        # can.save()
        
        i = -1
        
        for x in range(5):
            
            for y in range(5):
                
                i+=1
                
                if i == 12:
                    str1 = str2 = "Excited For The Wedding!"
                else:
                    str1 = bingo_table[i]
                    str2 = bingo_table2[i]
                    
                s= -1

                spl_list = str1.split(' ')
                if len(spl_list) < 4:
                    spl_list = \
                        [' '] * int(np.floor((4 - len(spl_list))/2)) \
                            + spl_list \
                            + [' '] * int(np.ceil((4 - len(spl_list))/2))
                spl_list = [f"{s:^15}" for s in spl_list] 
                                   
                for spl in spl_list:
                    
                    s+=1
                    
                    can.drawString((1+0.75*x) * inch, (2.1+0.75*y-0.12*s)*inch, spl)
                    
                s= -1
                    
                spl_list = str2.split(' ')
                if len(spl_list) < 4:
                    spl_list = \
                        [' '] * int(np.floor((4 - len(spl_list))/2)) \
                            + spl_list \
                            + [' '] * int(np.ceil((4 - len(spl_list))/2))
                spl_list = [f"{s:^15}" for s in spl_list] 
                
                for spl in spl_list:
                    
                    s+=1
                    
                    can.drawString((6+0.75*x) * inch, (2.1+0.75*y-0.12*s)*inch, spl)
                
        can.save()
    
        #move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
    
    # read your existing PDF
        
        # add the "watermark" (which is the new pdf) on the existing page
        existing_pdf = PdfFileReader(open(infile, "rb"))
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        
make_bingo_cards(20)

# finally, write "output" to a real file

outfile = r'C:\Users\spcra\Desktop\projects\bingo cards\Gabs Bingo Cards.pdf'

outputStream = open(outfile, "wb")
output.write(outputStream)
outputStream.close()


