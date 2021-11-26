class PatentesService: #ingresa una patente y retorna el ID asociado a la patente

    def __init__(self, patente_code):
        self.patente = patente_code

    def find_letter_position(self):
        abecedary = "abcdefghijklmnopqrstuvwxyz"
        assert len(self.patente)==7, "Error: length invalid"
        for i in range(0,4):
            assert self.patente[0].lower() in abecedary, "Error 400: Bad request"
        for i in range(4,7):
            assert self.patente[i].isnumeric(),"Error 400: Bad request"

        list_patente_code = list(self.patente)
        id = abecedary.index(list_patente_code[0].lower())*26000*26*26 \
             + abecedary.index(list_patente_code[1].lower())*26000*26 \
             + abecedary.index(list_patente_code[2].lower())*26000 \
             + abecedary.index(list_patente_code[3].lower())*1000 \
             + int(list_patente_code[4])*100 \
             + int(list_patente_code[5])*10 \
             + int(list_patente_code[6]) \
             + 1
        return id

class IdService: # ingresa el ID y retorna la patente

    def __init__(self,patente_id):
        self.id = int(patente_id)-1

    def find_code(self):
        patente = ['A','A','A','A',0,0,0]
        abecedary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        assert self.id+1<=456976000 \
            and self.id>=0,'Error 400: Patente dont exist'

        if self.id >= 26000*26*26:
            letter = abecedary[int(self.id/(26000*26*26))]
            self.id = self.id%(26000*26*26)
            patente[0] = letter
        if self.id >= 26000*26:
            letter = abecedary[int(self.id/(26000*26))]
            self.id = self.id%(26000*26)
            patente[1] = letter
        if self.id >= 26000:
            letter = abecedary[int(self.id/26000)]
            self.id = self.id%26000
            patente[2] = letter
        if self.id >= 1000:
            letter = abecedary[int(self.id/1000)]
            self.id = self.id%1000
            patente[3] = letter
        if self.id >= 100:
            patente[4] = int(self.id/100)
            self.id = self.id%100
        if self.id >= 10:
            patente[5] = int(self.id/10)
            self.id = self.id%10
        if self.id < 10:
            patente[6] = int(self.id)
        patente_end = "".join(map(str,patente))
        return patente_end