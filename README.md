## Pàgina del Projecte final de Postgrau d'Introducció en Data Science and Big Data 

En aquesta web parlarem del nostre projecte.

## Participants al projecte

Aquest projecte ha estat realitzat per Enrique Rodríguez, Jordi Palau i Raúl Zafra.

## Descripció del projecte

Ens hem enfrontat a un dataset amb dades referents a una campanya de matriculació a una institució de formació superior. Al dataset, corresponent a dades d'impactes de cuatre campanyes diferents, teníem informació molt variada que categoritzava els diferents impactes que la institució ha rebut.

Tenim informació diversa com identificador de l'usuari que ha fet l'impacte, producte al qual ha fet l'interés, diferents estats referents als diferents passos del procés de compra, canal pel qual s'ha adreçat per primera vegada a la institució en el procés de compra, dades geogràfiques, de gènere, etc.

Al dataset, també teníem l'estat final de l'impacte al final de campanya, sent la variable més important la que determinava si l'usuari havia acabat comprant el producte pel qual s'havia interessat o no.

La nostra idea de projecte ha estat netejar una mica la base de dades, fer un petit descriptiu de l'arxiu en base a les diferents variables que tenim al dataset i finalment crear un classificador que ens ajudi a predir per campanyes futures quins impactes s'acabaran convertint en matrícula en funció de les diferents característiques de que disposem i quins no.

Això ens permetria categoritzar els diferents impactes rebuts i prioritzar mitjançant accions de dinamització dels mateixos aquells que potser no tenim tant clar la seva compra sobre aquells que ja de ben inici el model ens dona la classificació com a impacte que acabarà convertint.

### Dades descriptives del nostre dataset

Primer de tot, hem fet un descriptiu bàsic del nostre dataset on hem vist quantes dades nul·les tenim per cadascuna de les nostres variables.

El nostre dataset consta de 27 variables que podem agrupar en variables d'usuari (identificador del mateix, país, comunitat autònoma, data de naixement i gènere), variables de producte d'interès (producte, àrea d'estudis del producte, subàrea d'estudis del producte, tipologia del producte i l'idioma de docència del producte), variables referents a l'interés de l'usuari (identificador de l'impacte, data creació impacte, estat de l'impacte, justificació, punt d'entrada de l'impacte, canal pel qual ha entrat, tipus de campanya i semestre d'entrada del lead), variables referents al cicle de maduració del mateix lead, als diferents estats pel que passa (data accés, data connexió, data proposta, etc.) i per últim la variable que volem predir referida a cada usuari, si s'ha matriculat o no.

<img src="https://github.com/jercapstone/UBCapstonePG/blob/master/descriptive.jpg" />

Tenim un total de 133.240 registres referents a 4 campanyes diferents de matrícula.







<Posar algun gràfic més amb algun histograma de les dades o algun gràfic de creuament de dues variables??>











### Primers dubtes: treballem a nivell d'impacte o a nivell d'usuari?

Una de les primeres preguntes que ens vam fer era si era més adequat treballar a nivell d'impacte o a nivell d'usuari. És a dir, el dataset el tenim a nivell d'impacte però pot ser que un únic individu faci més d' un impacte en una mateixa campanya i finalment acabi convertint en un dels impactes fets però obviament no en tots. Pot interessar-se per més d'un producte de formació però finalment acabar comprant un de sol.

L'anàlisi que hem acabat aplicant i sobre el que aplicarem el model de classificació serà en una visió a nivell d'usuari ja que finalment les accions de priorització a l'hora de dinamitzar els leads es fan a aquest nivell, a nivell d'usuari.

Per fer això hem aplicat un groupby que ens ha permès donar-li la volta al fitxer de dades que teníem per treballar i canviar la visió de les mateixes.

## Random Forest


### Crossvalidation

Apliquem el primer classificador que hem utilitzat per tal de definir el nostre model predictiu: el random forest. Primer de tot el que fem és carregar les nostres dades aplicant un crossvalidation on hem aplicat un folds=10 indicant així que dividirem el nostre dataset en 10 parts per tal de realitzar l'entrenament del nostre model.

Un cop aplicat això ens trobem amb el nostre primer resultat sorpresa:

<img src="https://github.com/jercapstone/UBCapstonePG/blob/master/crossvalidationRF.jpg" />

El que ens ha sorprés és trobar-nos amb unes diferències tant elevades entre els accuracys dels diferents entrenaments que hem realitzat. Ens trobem accuracys que van entre el 0.53 o 0.54 que ens trobem a les proves realitzades en 3a, 2a i 5a posició i accuracys que volten 0.97 o 0.98 que són els que s'assignen a les proves 7a, 8a i 9a. És a dir, les proves realitzades al final tenen una accuracy molt superior a les realitzades al principi. 

Aquest resultat ens ha sorprès per que podria indicar que el dataset està ordenat per alguna variable que indica que les dades del final prediuen millor el model que les del principi. A priori aquesta hipòtesi no ha estat buscada i podria ser que potser les dades de les darreres proves siguin dades de campanyes més properes en el temps on potser la qualitat de les dades són una mica més bones que les de campanyes més antigues.





<posar un gràfic descriptiu de les dades però per campanyes per validad aquesta hipòtesi?? Si no refer el darrer paràgraf>





### Matriu de confusió

Un segon output en que ens fixem del model és la matriu de confusió. Aparentment una matriu que dona uns resultats que a priori podríem considerar que no són dolents a l'hora de definir el model:

<img src="https://github.com/jercapstone/UBCapstonePG/blob/master/confusionmatrixRF.jpg" />






```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/jercapstone/UBCapstonePG/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
