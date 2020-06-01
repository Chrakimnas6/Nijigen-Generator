import thulac, random as rd

beginnings = ['呐~','诶多诶多~','诶多~','哑巴里~','阿诺~']
endings =['的说♡','呐......?♡', '呐☆~！']
symbols = ['♡','★', '♪', '☆', '......','!']

def converter(splited_text):
    converted = ""
    for idx, comb in enumerate(splited_text): # enumerate here just in case for the future ues
        text_type = comb.split('_')
        text = text_type[0]
        typee = text_type[1]
        if typee[0] == 'n':
            converted += nouns(text)
        else:
            converted += common(text)

    converted = beginning() + converted + ending()
    return converted

def nouns(text):
    return '「' + text + '」'

def common(text):
    if (rd.random() > 0.3):
        text += symbols[rd.randint(0, len(symbols) - 1)]
    return text

def beginning():
    return beginnings[rd.randint(0,len(beginnings) - 1)]

def ending():
    return endings[rd.randint(0, len(endings) - 1)]

if __name__ == "__main__":
    thu1 = thulac.thulac()
    sen = input("Input your sentence: ")
    text = thu1.cut(sen, text=True)
    splited_text = text.split()
    #print(splited_text)

    converted = converter(splited_text)

    print(converted)