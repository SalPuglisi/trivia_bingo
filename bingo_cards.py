import pandas as pd
import numpy as np
from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import random
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont

def make_bingo_cards(n):
    # set font
    pdfmetrics.registerFont(TTFont('Segoe Script', 'segoesc.ttf'))
    # choose bingo card template
    infile = r'jettemplate_HK641516_1.pdf'
    # initialize pdf writer
    output = PdfWriter()
    
    # question/answer list as dict - only answers are relevant for filling the card
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
    # decompose q/a dict into lists of questions and answers
    question_list = list(qa_dict.keys())
    answer_list = list(qa_dict.values())
    # for each bingo card, randomize answer list, fill into bingo card template using pdf watermark
    for i in range(n):
        
        bingo_table = random.sample(answer_list,25)
        bingo_table2 = random.sample(answer_list,25)
    
        packet = io.BytesIO()
        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont('Segoe Script', size=9.5)
        
        i = -1
        
        for x in range(5):
            
            for y in range(5):
                
                i+=1
                
                if i == 12:
                    str1 = str2 = "Free Space!"
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
        new_pdf = PdfReader(packet)
    
    # read your existing PDF
        
        # add the "watermark" (which is the new pdf) on the existing page
        existing_pdf = PdfReader(open(infile, "rb"))
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    return output

def write_bingo_cards(output, outfile):
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()

if __name__=="__main__":
    n = 10
    cards = make_bingo_cards(n)
    write_bingo_cards(cards, r'bingo_cards_filled.pdf')
    print(f"Created {n} bingo cards")
