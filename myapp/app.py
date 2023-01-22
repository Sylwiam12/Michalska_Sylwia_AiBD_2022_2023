
def text_contain_word(word: str, text: str):
    return word in text

def bubblesort(tab):
    for el in range(len(tab)):
         for k in range(0, len(tab)-el-1):
            if tab[k] > tab[k+1]:
                tab[k], tab[k+1] = tab[k+1], tab[k]
    return tab
