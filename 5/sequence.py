class Sequence(object):
    def __init__(self, string : str) -> None:
        self.sequence = string  

    def transcribe(self)->None: 
        raise NameError
    
    def hamming_distance(self, string2 : str) -> int: 
        count = 0
        if len(self.sequence) != len(string2):
            raise ValueError("Строки разной длины")
        else:
            for i in range(min(len(self.sequence), len(string2))):
                if self.sequence[i] != string2[i]:
                    count += 1
        count += abs(len(self.sequence) - len(string2))
        return(count)
    
        
    
        
class DNA(Sequence):  

    def count_nucleotides(self) -> dict:
        count_A : int = self.sequence.count('A')
        count_T : int = self.sequence.count('T')
        count_G : int = self.sequence.count('G')
        count_C : int = self.sequence.count('C')
        return{'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
        

    def transcribe(self) -> str:    
        transcribe_dna = self.sequence.replace('T', 'U')
        return(transcribe_dna)
    

    def complement_dna(self) -> str:
        complement_dna = self.sequence
        complement_dna = complement_dna.replace('A', '1')
        complement_dna = complement_dna.replace('T', 'A')
        complement_dna = complement_dna.replace('C', '3')
        complement_dna = complement_dna.replace('G', 'C')
        complement_dna = complement_dna.replace('1', 'T')
        complement_dna = complement_dna.replace('3', 'G')
        return(complement_dna)
        

class RNA(Sequence): 
    def count_nucleotides(self) -> dict:
        count_A : int = self.sequence.count('A')
        count_U : int = self.sequence.count('U')
        count_G : int = self.sequence.count('G')
        count_C : int = self.sequence.count('C')
        return{'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C}

    def transcribe(self) -> str:
        transcribe_rna = self.sequence.replace('U', 'T')
        return(transcribe_rna)
    

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

y2 = y.count_nucleotides()    #выводит количество нуклеотидов каждого типа 
print(y2)





