import wikipedia
import pickle
import emoji
import random



QnA = {}
unseen = []



def cleanText(string):
    string = string.replace('?','')
    string = string.replace('!','')
    string = string.replace('|','')
    string = string.replace(',',' ')
    string = string.replace('??','')
    string = string.replace('???','')
    string = string.replace('????','')
    string = string.replace('.','')
    string = string.replace(':','')
    string = string.replace(';','')
    string = string.replace('/','')
    string = string.replace('\\','')
    string = string.replace('\'','')
    string = string.replace('  ',' ')
    string = string.replace('   ',' ')
    string = string.replace('.','')
    string = string.replace('..','')
    string = string.replace('...','')
    string = string.replace('....','')
    string = string.replace('-','')
    string = string.replace('_','')
    string = string.lower()
    return string



def searchDB(ques):
    ans = '-1'
    file = open('data_file.db','rb')
    QnA = pickle.load(file)
    try:
        ans = QnA[ques]
    except:
        pass
    return ans



def searchWIKI(word):
    lst = wikipedia.search(word)
    string = "====Pages found:====\n"
    for i in range(len(lst)):
        string+= str(i+1)+". "+lst[i]+'\n'
    string +='\n\n\n\n'
    string +='printing information for: '+lst[0]+'\n'
    string +='=======================================\n'
    wiki_page = wikipedia.page(lst[0])
    lines = wiki_page.content.split('.')
    for i in range(10):
        string = string+str(lines[i])+'.'
    return string



def main(word):
    try:
        #handle emoji
        if emoji.emoji_count(word) > 0:
            return '🤷🏻‍♀️🤷🏻‍♀️🤷🏻‍♀️🤷🏻‍♀️🤷🏻‍♀️🤷🏻‍♀️🤷🏻‍♀️🤷🏻‍♀️'

        #handle mathematical operations
        try:
            return eval(word)
        except:
            pass
        
        #handle comma
        if word == '.':
            return '.'

        
        #handle joke
        if word == 'tell me a joke':
            word = "joke " + str(random.randrange(1,11))
        
        
        word = cleanText(word)

        #hangle wiki
        if word[0:4] == 'wiki':
            ans = "There was an error trying to parse the output."
            try:
                ans = searchWIKI(word[5:])
            except:
                pass
            return ans

        #handle speaking
        ans = searchDB(word)

        #handle unformatted wiki
        if ans == '-1':
            try:
                wiki_page = wikipedia.page(word)
                ans = wiki_page.content.split('.')[0:12]
                return ans
            except:
                pass
        

        if ans == '-1':
            file1 = open('unseen.db','wb')
            unseen.append(word)
            pickle.dump(unseen,file1)
            ans = "I don't know the answer to this message. Sorry."
        return ans


    except:
        return 'I am an idiot. The main function crashed! 🤷🏻‍♀️ \nmeanwhile if you want me to tell you a joke, white - tell me a joke'