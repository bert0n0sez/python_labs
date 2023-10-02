class DNA(object):
    def __init__(self, string : str) -> None:
        self.string = string  

    def count_nucleotides(self) -> dict:
        count_A : int = self.string.count('A')
        count_T : int = self.string.count('T')
        count_G : int = self.string.count('G')
        count_C : int = self.string.count('C')
        return{'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
        
        
'''
    def transcribe(self) -> str:      # А на У менять типо РНК становится
        trans_str : list = self.string
        index_T = self.string.index('T')
        trans_str.insert(index_T, 'Y')
        return(trans_str)
    


    def complement_dna(self) -> str:
        compl_dna : list = self.string
        index_A = self.string.index('A')
        index_T = self.string.index('T')
        index_G = self.string.index('G')
        index_C = self.string.index('C')
        compl_dna.insert(index_A, 'T')
        compl_dna.insert(index_T, 'A')
        compl_dna.insert(index_G, 'C')
        compl_dna.insert(index_C, 'G')
        return(compl_dna)
    



    def hamming_distance(self, string2 : str) -> int:
         self.string 
         string2        # количество различий между цепью в DNA и написанной с клавы 
        

class RNA(object):
    def __init__(self, string : str) -> None:
        self.string = string 
    def transcribe(self) -> str:

        
x.hamming_distance(input())

'''
x = DNA('ATGC')


D = x.count_nucleotides()
print(D)


