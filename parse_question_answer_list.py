from pprint import pprint

question_answers = """1. How many sisters does Gabrielle have? 1 sister
2. How many kitty children do Gabrielle & Sal have? 2 kitty children
3. Gabs favorite food? Sushi 
4. Gabs favorite movie? Mr. Right 
5. Gabs favorite show? NCIS
6. Gabs favorite color? Green 
7. Names of their kitties? Mel & Mable 
8. Where did gabs and sal meet? Ithaca college 
9. Birthday? January 5th 
10. Fav alcoholic drink? Lemon Drop
11. Where they got engaged? Atlantis, The Bahamas 
12. Fav disney movie? Brave 
13. What does her family call her? Gabs 
14. Job? Social worker 
15. Favorite food as a kid? Lobster 
16. Favorite actor? Sydney Sweeney
17. Type of music she loves? Dance/ House
18. What is Gab’s allergic to? Wheat/ Gluten
19. Favorite video game? Mine- craft 
20. Favorite flower? Car- nations 
21. Wedding date? October 7th 
22. Gabs middle name? Nicole 
23. Favorite dessert? Flourless Chocolate cake 
24. Favorite comedian? Tom Segura
25. Chocolate or vanilla? Chocolate 
26. How long have Gabs and Sal been together? 7 years 
27. Favorite season? Winter 
28. What is Gab’s biggest pet peve? Non turn- blinker users
29. Hidden talent? Florist
30. Dream Job? Nanny
31. First Job? Camp Counselor"""

qa_list = question_answers.split('\n')

def qa_list_to_dict(li):
    def split_question_answer(i):
        _qa = i[3:]
        _q, _a = _qa.split('? ')
        _q = _q.strip() + "?"
        _a = _a.strip()
        
        return _q, _a
    
    qa_dict = dict([split_question_answer(qa) for qa in li])
    
    return qa_dict

qa_dict = qa_list_to_dict(qa_list)
pprint(qa_dict)
    


    
    
    


