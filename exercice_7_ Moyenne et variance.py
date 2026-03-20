import numpy as np

notes = np.array([8, 12, 15, 10, 14, 9, 17, 11])

#rechnen wir die Durchschnitt

n = len(notes)
durchschnitt = 0
for note in notes:
    durchschnitt += (note/len(notes))
print("Durchschnitt:",durchschnitt)


#rechnen wir jetzt die Varianz

varianz = 0
for note in notes:
    varianz += (((note - durchschnitt)**2)/n)
print("Varianz:",varianz)


# jetzt nutzen wir die Numpy-Funktionen
print(np.mean(notes))
print((np.var(notes)))

