#!/usr/bin/env python2

#encoding:utf-8
# Author: Debapriya Das
# Purpose: Example for detecting language using a stopwords based approach


import sys

try:
    from nltk.tokenize import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print '[!] You need to install nltk (http://nltk.org/index.html)'



#----------------------------------------------------------------------
def _calculate_languages_ratios(text):
    """
    Calculate probability of given text to be written in several languages and
    return a dictionary that looks like {'french': 2, 'spanish': 4, 'english': 0}
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Dictionary with languages and unique stopwords seen in analyzed text
    @rtype: dict
    """

    languages_ratios = {}

    '''
    nltk.wordpunct_tokenize() splits all punctuations into separate tokens
    
    >>> wordpunct_tokenize("That's thirty minutes away. I'll be there in ten.")
    ['That', "'", 's', 'thirty', 'minutes', 'away', '.', 'I', "'", 'll', 'be', 'there', 'in', 'ten', '.']
    '''

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) # language "score"

    return languages_ratios


#----------------------------------------------------------------------
def detect_language(text):
	"""
	Calculate probability of given text to be written in several languages and
	return the highest scored.
	It uses a stopwords based approach, counting how many unique stopwords
	are seen in analyzed text.
    
    @param text: Text whose language want to be detected
    
    @type text: str
    
    @return: Most scored language guessed
    
    @rtype: str
    """
    ratios = _calculate_languages_ratios(text)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language



if __name__=='__main__':
	'''
	giving the program a try!!!!!
	
	'''
	text = "INFORMACIÓN EN ESPAÑOL Una Lectura en español acerca de las cábalas de Año Nuevo en Chile y el significado de estas tradiciones. Incluye afiches a todo color y en blanco y negro (para imprimir). CONTENIDO: Este pack contiene 11 Páginas: Afiche – A Todo Color con texto – (1 página) Afiche – A Todo Color sin texto – (1 página) Afiche – Blanco y Negro con texto – (1 página) Afiche – Blanco y Negro sin texto – (1 página) Lectura – Cábalas de Año Nuevo en Chile – (1 página) Una explicación de cada tradición Preguntas de Comprensión – Cábalas de Año Nuevo en Chile – (3 páginas) Espacio para escribir – (1 página) Respuestas para los profesores – (2 páginas) NIVEL: Intermedio (CEFR – B1 Level) EDAD: Desde los 12 años hasta adultos "

    language = detect_language(text)

    print language
