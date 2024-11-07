Grafo semplice, pesato e non orientato (Graph)
Nodi: tutti i geni con campo essential = 'Essential'
Archi: Un arco collega due geni diversi solo se tale coppia (indipendentemente dall’ordine) appare nella tabella interactions. 
Si ignorino gli archi di tipo “cappio”, cioè le connessioni di un gene con se stesso.
Per definire il peso dell’arco si parta dalla 
correlazione fra i geni (tabella interactions, campo Expression_Corr) e si consideri il peso
• pari al valore assoluto di tale correlazione se i due geni non appartengono allo stesso 
cromosoma (campo Chromosome della tabella genes)
• pari al doppio del valore assoluto di tale correlazione se i due geni appartengono allo 
stesso cromosoma

Selezionare poi un gene dal menu a tendina e calcolare i geni adiacenti
