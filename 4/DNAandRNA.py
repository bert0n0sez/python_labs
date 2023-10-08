class DNA(object):
    def __init__(self, string : str) -> None:
        self.string = string  


    def count_nucleotides(self) -> dict:
        count_A : int = self.string.count('A')
        count_T : int = self.string.count('T')
        count_G : int = self.string.count('G')
        count_C : int = self.string.count('C')
        return{'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
        

    def transcribe(self) -> str:      # А на У менять типо РНК 
        transcribe_dna = self.string.replace('T', 'U')
        return(transcribe_dna)
    

    def complement_dna(self) -> str:
        complement_dna = self.string
        complement_dna = complement_dna.replace('A', '1')
        complement_dna = complement_dna.replace('T', 'A')
        complement_dna = complement_dna.replace('C', '3')
        complement_dna = complement_dna.replace('G', 'C')
        complement_dna = complement_dna.replace('1', 'T')
        complement_dna = complement_dna.replace('3', 'G')
        return(complement_dna)
    

    def hamming_distance(self, string2 : str) -> int: 
        string2: str
        count = 0
        for i in range(min(len(self.string), len(string2))):
            if self.string[i] != string2[i]:
                count += 1
        count += abs(len(self.string) - len(string2))
        return(count)


class RNA(object):
    def __init__(self, string : str) -> None:
        self.string = string 


    def transcribe(self) -> str:
        trans_rna = self.string.replace('U', 'T')
        return(trans_rna)

        
x = DNA(input())


x1 = x.count_nucleotides() 
print(x1)                 #выводит количество нуклеотидов каждого типа


x2 = x.transcribe()
print(x2)                 #выводит цепь, где все нуклеотиды А заменены на U 


x3 = x.complement_dna()
print(x3)                #выводит комплиментарную цепь 


x4 = x.hamming_distance(input())
print(x4)                #сначала надо ввести с клавиатуры новую цепь ДНК, функция посчитает отличия между новой и "старой"


y = RNA(input())


y1 = y.transcribe()    #выводит цепь, где нуклеотиды U заменены на T 
print(y1)
