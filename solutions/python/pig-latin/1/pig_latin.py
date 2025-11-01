def translate(text):
    #test = "apple xray yttria pig chair thrush quick square my rhythm"
    vowels = "aeiou"
    words= text.split()
    sen = ""
    for word in words:
        if word[0] in vowels or word.startswith(('xr', 'yt')):
            word += 'ay'
            #print("IF ", word)
            
        else:
            for i in range(len(word)):
                if word.endswith('ay') == False:
                    if word[i] in vowels:
                        
                        if word[i] == 'u' and word[i-1] == 'q':
                            word = word[i+1:] + word[:i+1] + 'ay'
                            #print("Else - IF1", word)
        
        
                        if word.endswith('ay') == False:
                            word = word[i:] + word[:i] + 'ay'
                            #print("Else - IF2", word)
                    if i != 0:
                        if word[i] == 'y' and word[i-1] not in vowels:
                            word = word = word[i:] + word[:i] + 'ay'
                            #print("Else - IF3", word)
    
        sen += word + " "
    
    return(sen.rstrip())