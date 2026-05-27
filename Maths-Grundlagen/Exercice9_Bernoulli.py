import numpy as np

# Simulieren wir 1000 würfe einer Münze (p=0.5)
data = np.random.binomial(n=1, p=0.5, size=1000)

print(np.mean(data)) # mann kann bemerken , dass diese Durchschnitt nähe von 0.5 ist
print(np.var(data)) # mann kann bemerken , dass diese Varienz nähe von 0.5(1-0.5) ist


#jetzt P = 0.3
data = np.random.binomial(n=1, p=0.3, size=1000)

print(np.mean(data)) # mann kann bemerken , dass diese Durchschnitt nähe von 0.3 ist
print(np.var(data)) # mann kann bemerken , dass diese Varienz nähe von 0.3(1-0.3) ist

'''
merken wir , dass die Varienz maximal ist, wenn P=0.5 —
wenn die Unsicherheit groß ist. je mehr p von 0.5 (nähe von 0 oder 1) erweitert ist , 
desto die Varienz abnimmt denn die Ergebnis wird Vorhersehbar. 

'''