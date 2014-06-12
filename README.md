# Google News Parser

gnp (Google News Parser) is a simple python module to parse news articles from google news website
It offers output in json format for all available editions, along with location overloading.
Also, it offers search results of news article for user supplied text.

## Install Steps:
    pip install gnp

## Basic Usage:

### Get news for Google News Indian Edition
    >>> import gnp
    >>> a = gnp.get_google_news(gnp.EDITION_ENGLISH_INDIA)


### Get news for Google News US Version as if browsing from London,UK
    >>> import gnp
    >>> b = gnp.get_google_news(gnp.EDITION_ENGLISH_US,geo='London,UK')

### Get news for search Query "What's happening on earth".
####    Default you get results for 'Barack Obama'

    >>> import gnp
    >>> c = gnp.get_google_news_query("What's happening on earth")

### Method to write to flatfile

    >>> import gnp
    >>> d = gnp.get_google_news(gnp.EDITION_ENGLISH_INDIA)

    >>> import codecs
    >>> import json

    >>> j = json.dumps(d, indent=4, ensure_ascii=False )
    >>> f = codecs.open( 'news.json', 'w', encoding='utf-8')
    >>> f.write(j.decode('utf-8'))
    >>> f.close()

####List of Editions Available::

         Edition Name         |             Region             
------------------------------|--------------------------------
 EDITION_SPANISH_ARGENTINA    | Argentina                      
 EDITION_ENGLISH_AUSTRALIA    | Australia                      
 EDITION_DUTCH_BELGIUM        | België                         
 EDITION_FRENCH_BELGIUM       | Belgique                       
 EDITION_ENGLISH_BOTSWANA     | Botswana                       
 EDITION_PORTUGESE_BRAZIL     | Brasil                         
 EDITION_ENGLISH_CANADA       | Canada English                 
 EDITION_FRENCH_CANADA        | Canada Français                
 EDITION_CZECH_CZECH_REPUBLIC | Česká republika                
 EDITION_SPANISH_CHILE        | Chile                          
 EDITION_SPANISH_COLUMBIA     | Colombia                       
 EDITION_SPANISH_CUBA         | Cuba                           
 EDITION_DEUTSCH_DEUTSCHLAND  | Deutschland                    
 EDITION_SPANISH_SPAIN        | España                         
 EDITION_SPANISH_US           | Estados Unidos                 
 EDITION_ENGLISH_ETHIOPIA     | Ethiopia                       
 EDITION_FRENCH_FRANCE        | France                         
 EDITION_ENGLISH_GHANA        | Ghana                          
 EDITION_ENGLISH_INDIA        | India                          
 EDITION_ENGLISH_IRELAND      | Ireland                        
 EDITION_ENGLISH_ISREAL       | Israel English                 
 EDITION_ITALIAN_ITALY        | Italia                         
 EDITION_ENGLISH_KENYA        | Kenya                          
 EDITION_HUNGARIAN_HUNGARY    | Magyarország                   
 EDITION_ENGLISH_MALAYSIA     | Malaysia                       
 EDITION_FRENCH_MORACCO       | Maroc                          
 EDITION_SPANISH_MEXICO       | México                         
 EDITION_ENGLISH_NAMIBIA      | Namibia                        
 EDITION_DUTCH_NEDERLAND      | Nederland                      
 EDITION_ENGLISH_NEW_ZEALAND  | New Zealand                    
 EDITION_ENGLISH_NIGERIA      | Nigeria                        
 EDITION_NORSK_NORWAY         | Norge                          
 EDITION_DEUTSCH_AUSTRIA      | Österreich                     
 EDITION_ENGLISH_PAKISTAN     | Pakistan                       
 EDITION_SPANISH_PERU         | Perú                           
 EDITION_ENGLISH_PHILIPPINES  | Philippines                    
 EDITION_POLISH_POLAND        | Polska                         
 EDITION_PORTUGUESE_PORTUGAL  | Portugal                       
 EDITION_GERMAN_SWITZERLAND   | Schweiz                        
 EDITION_FRENCH_SENEGAL       | Sénégal                        
 EDITION_ENGLISH_SINGAPORE    | Singapore                      
 EDITION_ENGLISH_SOUTH_AFRICA | South Africa                   
 EDITION_FRENCH_SWITZERLAND   | Suisse                         
 EDITION_SWEDISH_SWEDEN       | Sverige                        
 EDITION_ENGLISH_TANZANIA     | Tanzania                       
 EDITION_TURKISH_TURKEY       | Türkiye                        
 EDITION_ENGLISH_UK           | U.K.                           
 EDITION_ENGLISH_US           | U.S.                          
 EDITION_ENGLISH_UGANDA       | Uganda                       
 EDITION_SPANISH_VENEZUELA    | Venezuela                   
 EDITION_VIETNAMESE_VIETNAM   | Việt Nam (Vietnam)         
 EDITION_ENGLISH_ZIMBABWE     | Zimbabwe                  
 EDITION_GREEK_GREECE         | Ελλάδα (Greece)          
 EDITION_RUSSIAN_RUSSIA       | Россия (Russia)                
 EDITION_SERBIAN_SERBIA       | Србија (Serbia)                
 EDITION_RUSSIAN_UKRAINE      | Украина / русский (Ukraine)    
 EDITION_UKRAINIAN_UKRAINE    | Україна / українська (Ukraine) 
 EDITION_HEBREW_ISRAEL        | ישראל (Israel)                 
 EDITION_ARABIC_UAE           | الإمارات (UAE)                  
 EDITION_ARABIC_SAUDI_ARABIA  | السعودية (KSA)                    
 EDITION_ARABIC_ARAB_WORLD    | العالم العربي (Arabic)             
 EDITION_ARABIC_LEBANON       | لبنان (Lebanon)                  
 EDITION_ARABIC_EGYPT         | مصر (Egypt)                    
 EDITION_HINDI_INDIA          | हिन्दी (India)                 
 EDITION_TAMIL_INDIA          | தமிழ் (India)                    
 EDITION_TELUGU_INDIA         | తెలుగు (India)                   
 EDITION_MALAYALAM_INDIA      | മലയാളം (India)                 
 EDITION_KOREAN_SOUTH_KOREA   | 한국 (Korea)                   
 EDITION_CHINESE_CHINA        | 中国 (China)                    
 EDITION_CHINESE_TAIWAN       | 台灣 (Taiwan)                   
 EDITION_JAPANESE_JAPAN       | 日本 (Japan)                    
 EDITION_JAPANESE_HONG_KONG   | 香港 (Hong Kong)                

Copyright (c) 2014, Manuel David Pandian



