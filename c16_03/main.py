# Données :
note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

print(notes)

# question 4 : 
# a/ calculez la moyenne de eleve1 :


moyenne = sum(note[2] for note in notes)/len(notes)
print(moyenne)


notes =notes[0:5]
moyenne_elev1 = sum(note[2] for note in notes)/len(notes)
print(moyenne_elev1)

# b/ calculez la moyenne de eleve1 en maths
notes = [note1, note3, note6]

moyenne_elev1_maths =sum(note[2] for note in notes)/len(notes)
print(moyenne_elev1_maths)

# c/ Créer une fonction "moyenne_tuples" qui calcule la moyenne de d'un élève dans une matière.

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur

def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)

onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

def moyenne_tuples(Note,eleve,matiere):
  return sum(note[2] for note in notes)/len(notes)