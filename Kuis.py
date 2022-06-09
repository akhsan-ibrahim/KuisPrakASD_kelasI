#Akhsan Ibrahim
#L200200253

#1
import re
i1 = '@Akhsan2_sas'
pola = r'@[\w]+[\d]+\_*'
cocok = re.findall(pola,i1)
if not cocok:
    print('FAILED')
elif cocok[0] != i1:
    print('FAILED')
else:
    print('PASS')

#2
e1 = """We are hiring Test/QA Engineers with 1-3 years of experience in Manual Testing(Web, Mobile & API). If anyone((Especially who lost the job due to COVID) looking for a change, please share me the resume at mailmesiva25@gmail.com
Company:Open Financial Technologies
Location: Bangalore
Note: Fintech Experience would be a higher priority
"""
pola2 = r'[\w.-]+@[\w.-]+'
cocok2 = re.findall(pola2, e1)
print(cocok2)

#3
class _SimpulPohonBiner(object):
    def __init__(self,data) -> None:
        self.data = data
        self.kiri = None
        self.kanan = None

A = _SimpulPohonBiner(1)
B = _SimpulPohonBiner(2)
C = _SimpulPohonBiner(3)
D = _SimpulPohonBiner(4)
E = _SimpulPohonBiner(5)

A.kiri = B; A.kanan = C
C.kiri = D; C.kanan = E

def terluarkiri(sub):
    if sub is not None:
        terluarkiri(sub.kiri)
        print(sub.data)

def terluarkanan(sub):
    if sub is not None:
        print(sub.data)
        terluarkanan(sub.kanan)

def terluar(sube):
    terluarkiri(sube)
    terluarkanan(sube)

terluar(A)