# Model predictiu d'un procés de compra en el sector de l'educació superior

## Introducció

Els diferents canvis que han sofert darrerament el sector de l'educació superior a Espanya arrel de l'entrada en vigor de l’Espai d’Educació Superior i dels canvis demografics que s'han produït als darrers anys així com la disminució de les subvencions per part dels governs a les diferents institucions públiques d'ensenyament, fan que hi hagi un entorn molt competitiu entre les diferents institucions a fi de poder aconseguir nous alumnes per poder desenvolupar la seva activitat. 

Els criteris dels futurs alumnes per acabar seleccionant una institució s’han modificat. A part dels antics criteris que definien les institucions com el prestigi, l’antiguitat, la tradició i l’empleabilitat, s’estan afegint criteris que s’apropen perillosament a un model de negoci més comercial que no, d’una institució educativa. Aquest nous criteris van vinculats, a l’atenció personalitzada, el servei, posicionament en els rankings, satisfacció, preu.

És per aquest motiu, que ens plantegem crear un model predictiu que ajudi a les institucions a millorar la seva eficàcia i eficiciència, a l’hora d’incorporar nous estudiant.  En base a les característiques de les persones que s’apropen demanant informació sobre els diferents programes formatius que ofereixen hem obtingut diferents variables.

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

En una primera mirada de la Matriu de confusió, ens diu que la predicció del nostre model té una precisió d'un 68% i un recall del 65%, un model amb uns resultats millorables però acceptables. No obstant, si baixem una mica aquesta informació i aprofondim en els paràmetres precisió i recall, ens trobem amb el següent:

<img src="https://github.com/jercapstone/UBCapstonePG/blob/master/confusionmatrixRFexp.jpg" />

La variable precision és la precisió del model i ens indicaria,  dels que hem predit com a no matriculats quants hem encertat. En el nostre cas un 73%. També ens indicaria dels que he predit com a matriculats quants he encertat que també en aquest cas seria un 56%. Això ja ens diu que el model encerta molt millor les prediccions dels no matriculats que les prediccions d'estudiants matriculats.

Si aprofondim en la variable recall encara ens trobem amb informació una mica més difícil d'interpretar: dels que al dataset estan codificats com a no matriculats, quants hem predit de forma correcta. En el nostre cas un 95% el que indicaria un encert gairebé perfecte. En canvi si mirem al dataset, dels que eren matriculats quants s'han predit de forma correcta, veiem que aquest percentatge baixa a només el 16%. És a dir, dels que estaven matriculats només hem encertat amb el model que es matricularien en un 16%, el 84% els hem fallat.

Queda clar doncs, que el nostre model l'hauríem de treballar millor incorporant alguna variable més que ens ajudi a ajustar-lo, sobretot pel que fa a la part dels matriculats. Com hem indicat previament,éÉs curiós també que si mirem la mitjana d'aquestes variables realment  no deixen malament el model. Ens quedem amb un precision average  i un recall average del 68 i 71 respectivament.


## Variables que expliquen el model

El darrer output que hem analitzat del classificador Random Forest és veure quines són les variables que està utilitzant per construir el model.

<img src="https://github.com/jercapstone/UBCapstonePG/blob/master/variablesRF.jpg" />

En aquest cas veiem que de les 27 variables que teníem (26 si traiem la variable que volíem explicar) estem explicant el model només amb 9. D'aquestes 9 hi ha tres que tenen una mica més pes que la resta.

<img src="https://github.com/jercapstone/UBCapstonePG/blob/master/variablesRFexp.jpg" />

Aquestes variables són la regió, que com hem explicat al principi indica la comunitat autònoma de l'usuari que ha realitzat el contacte amb la Universitat i que pesa un 33%, l'idioma del producte comprat i el producte comprat. Amb el coneixement que tenim del negoci, podem dir que el pes d'aquestes variables és esperat sobretot pel que fa a la regió ja que a la institució analitzada així com a la resta d'institucions d'educació superior d l'estat el pes territorial de les instituciosn encara és molt gran entre els estudiants a l'hora de decidir-se per buscar un centre on cursar els estudis superiors.


<buscar algun document, o alguna referència a aquest tema per posar-ho com a font??>



## K-means

Hem aplicat un segon model de classificació al nostre dataset per veure si el resultat era millor i aconseguiem afinar el model de predicció.

