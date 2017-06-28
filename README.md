# Model predictiu d'un procés de compra en el sector de l'educació superior

## Participants al projecte

Aquest projecte ha estat realitzat per Enrique Rodríguez, Jordi Palau i Raúl Zafra.

## Introducció

Els diferents canvis que han sofert darrerament el sector de l'educació superior a Espanya arrel de l'entrada en vigor de l’Espai d’Educació Superior i dels canvis demografics que s'han produït als darrers anys així com la disminució de les subvencions per part dels governs a les diferents institucions públiques d'ensenyament, fan que hi hagi un entorn molt competitiu entre les diferents institucions a fi de poder aconseguir nous alumnes per poder desenvolupar la seva activitat. 

Els criteris dels futurs alumnes per acabar seleccionant una institució s’han modificat. A part dels antics criteris que definien les institucions com el prestigi, l’antiguitat, la tradició i l’empleabilitat, s’estan afegint criteris que s’apropen perillosament a un model de negoci més comercial que no, d’una institució educativa. Aquest nous criteris van vinculats, a l’atenció personalitzada, el servei, posicionament en els rankings, satisfacció, preu.

És per aquest motiu, que ens plantegem crear un model predictiu que ajudi a les institucions a millorar la seva eficàcia i eficiciència, a l’hora d’incorporar nous estudiant.  En base a les característiques de les persones que s’apropen demanant informació sobre els diferents programes formatius que ofereixen hem obtingut diferents variables.

## Descripció del projecte

Ens hem enfrontat a un dataset amb dades referents a una campanya de matriculació a una institució de formació superior. Al dataset, corresponent a dades d'impactes de cuatre campanyes diferents, teníem informació molt variada que categoritzava els diferents impactes que la institució ha rebut.

Tenim informació diversa com identificador de l'usuari que ha fet l'impacte, producte al qual ha fet l'interés, diferents estats referents als diferents passos del procés de compra, canal pel qual s'ha adreçat per primera vegada a la institució en el procés de compra, dades geogràfiques, de gènere, etc.

Al dataset, també teníem l'estat final de l'impacte al final de campanya, sent la variable més important la que determinava si l'usuari havia acabat comprant el producte pel qual s'havia interessat o no.

La nostra idea de projecte ha estat netejar una mica la base de dades, fer un petit descriptiu de l'arxiu en base a les diferents variables que tenim al dataset i finalment crear un classificador que ens ajudi a predir per campanyes futures quins impactes s'acabaran convertint en matrícula en funció de les diferents característiques de que disposem i quins no.

Això ens permetria categoritzar els diferents impactes rebuts i prioritzar mitjançant accions de dinamització dels mateixos aquells que potser no tenim tant clar la seva compra sobre aquells que ja de ben inici el model ens dona la classificació com a impacte que acabarà convertint.

### Dades descriptives del nostre dataset

Primer de tot, hem fet un descriptiu bàsic del nostre dataset on hem vist quantes dades nul·les tenim per cadascuna de les nostres variables.

El nostre dataset consta de 27 variables que podem agrupar en variables d'usuari (identificador del mateix, país, comunitat autònoma, data de naixement i gènere), variables de producte d'interès (producte, àrea d'estudis del producte, subàrea d'estudis del producte, tipologia del producte i l'idioma de docència del producte), variables referents a l'interés de l'usuari (identificador de l'impacte, data creació impacte, estat de l'impacte, justificació, punt d'entrada de l'impacte, canal pel qual ha entrat, tipus de campanya i semestre d'entrada del lead), variables referents al cicle de maduració del mateix lead, als diferents estats pel que passa (data accés, data connexió, data proposta, etc.) i per últim la variable que volem predir referida a cada usuari, si s'ha matriculat o no.

<img src="https://jercapstone.github.io/UBCapstonePG/descriptive.jpg" />

Tenim un total de 133.240 registres referents a 4 campanyes diferents de matrícula, tot i que com es veu en la imatge anterior hi ha moltes variables on no està completa tota la informació.

### Primers dubtes: treballem a nivell d'impacte o a nivell d'usuari?

Una de les primeres preguntes que ens vam fer era si era més adequat treballar a nivell d'impacte o a nivell d'usuari. És a dir, el dataset el tenim a nivell d'impacte però pot ser que un únic individu faci més d' un impacte en una mateixa campanya i finalment acabi convertint en un dels impactes fets però obviament no en tots. Pot interessar-se per més d'un producte de formació però finalment acabar comprant un de sol.

L'anàlisi que hem acabat aplicant i sobre el que aplicarem el model de classificació serà en una visió a nivell d'usuari ja que finalment les accions de priorització a l'hora de dinamitzar els leads es fan a aquest nivell, a nivell d'usuari.

Per fer això hem aplicat un groupby que ens ha permès donar-li la volta al fitxer de dades que teníem per treballar i canviar la visió de les mateixes.

## Agrupació en segments (per k=3 fins a 8) amb KMeans

Hem agrupat els usuaris en funció de l'activitat generada en campanya. La metodologia utilitzada ha estat KMeans per a un número de segments entre 3 i 8.

El resultat obtingut ha estat que cap variable d'activitat presenta diferències significatives entre grups. La única variable que presenta diferències significatives entre grups ha estat l'edad (prèviament normalitzada).

<img src="https://jercapstone.github.io/UBCapstonePG/kmeans.jpg" />

## K Nearest Neighbours

La nostra hipòtesis de partida ha estat si podem realitzar un model que ens predigui si un estudiant es matricularà o no en funció de l' activitat generada durant el procés de campanya de matriculació

El primer que hem fet ha estat aplicar un model de predicció també senzill. Hem aplicat el model de classificació bàsic Nearest Neighbours al nostre dataset per veure si aconseguim un model de predicció amb uns bons resultats.

Aquest model el que fa és classificar els diferents casos dintre del model en funció de les distàncies dels casos que té al voltant

### Crossvalidation

Els accuracy que ens trobem en aquest model per cada train que realitzem són baixos en general:

<img src="https://jercapstone.github.io/UBCapstonePG/crossvalidationKN.jpg" />

### Matriu de confusió

La matriu de confusió que ens trobem en el model de Nearest Neighbours ens està donant resultats poc precisos.

<img src="https://jercapstone.github.io/UBCapstonePG/confusionmatrixKN.jpg" />

El precission average és d'un 0.55 i el recall average és del 0.52. Si aprofondim una mica en aquests paràmetres veiem el següent:

<img src="https://jercapstone.github.io/UBCapstonePG/confusionmatrixKNexp.jpg" />

Si mirem els paràmetres que indiquen la qualitat del model, de forma general veiem que són fàcilment millorables. La variable precision és la precisió del model i ens indicaria el següent:  dels que hem predit com a no matriculats quants hem encertat. En el nostre cas tenim un precision de 0.68 en aquest col·lectiu. També ens indicaria dels que he predit com a matriculats quants he encertat que també en aquest cas seria un 0.26. 

Si aprofondim en la variable recall encara ens trobem amb més informació: dels que al dataset estan codificats com a no matriculats, quants hem predit de forma correcta. En el nostre cas un 60%. En canvi si mirem al dataset, dels que eren matriculats quants s'han predit de forma correcta, veiem que aquest percentatge baixa a només el 33%. És a dir, dels que estaven matriculats només hem encertat amb el model que es matricularien en un 33%, la resta els hem fallat.

Això demostraria que el model serveix millor per predir els no matriculats que per predir els matriculats.

Intentem millorar una mica el model i apliquem un procés d' snooping:

<img src="https://jercapstone.github.io/UBCapstonePG/confusionmatrixKN2.jpg" />

<img src="https://jercapstone.github.io/UBCapstonePG/confusionmatrixKN2exp.jpg" />

Veiem que amb aquest procés el model millora molt passant a tenir uns precision average de 0.64 i un recall average de 0.65.

## Arbre de decisió simple

Seguint amb la nostra hipòtesis de partida de si podem realitzar un model que ens predigui si un estudiant es matricularà o no en funció de l' activitat generada durant el procés de campanya de matriculació, hem continuat aplicant un Arbre de decisió simple.

Hem executat codi en python i ens ha donat el següent resultat:

<img src="https://jercapstone.github.io/UBCapstonePG/decisiontree.jpg" />

La interpretació d'aquest gràfic és jeràrquica, seguint l'eix des de dalt cap a baix on va indicant el número de node asociats a la variable que el formen i els nodes següents que pengen de cada branca.

Veiem que les variables que més determinen el model són la regió (la primera variable, Node 0), l'idioma del producte comprat (que penja del Node 0 i és el Node 1), el producte comprat en sí (Node 2 que penja del Node 1) i el canal (Node 3 que també penja del Node 1). Ens quedaríem amb aquestes variables com els principals factors identificats. 

### Matriu de confusió
 
 La matriu de confusió resultant de l'arbre de decisió és la següent.

<img src="https://jercapstone.github.io/UBCapstonePG/confusionmatrixDT.jpg" />

En una primera mirada de la Matriu de confusió, ens diu que la predicció del nostre model té una precisió d'un 67% i un recall del 71%, un model amb uns resultats millorables però acceptables. No obstant, si baixem una mica aquesta informació igual que hem fet al model de K Nearest Neighbours, i aprofondim en els paràmetres precisió i recall, ens trobarem amb alguna sorpresa:

<img src="https://jercapstone.github.io/UBCapstonePG/confusionmatrixDTexp.jpg" />

La variable precision, tal com deiem, és la precisió del model i ens indicaria dels que hem predit com a no matriculats quants hem encertat. En el nostre cas, en aquest model un 0.72. També ens indicaria dels que he predit com a matriculats quants he encertat que també en aquest cas seria un 0.54. Això ja ens diu igual que al KNN que el model encerta molt millor les prediccions dels no matriculats que les prediccions d'estudiants matriculats.

Si aprofondim en la variable recall encara ens trobem amb informació una mica més difícil d'interpretar: dels que al dataset estan codificats com a no matriculats, prediem de forma correcta un 95% el que indicaria un encert gairebé perfecte. En canvi si mirem al dataset dels que eren matriculats quants s'han predit de forma correcta, veiem que aquest percentatge baixa a només el 15%. És a dir, dels que estaven matriculats només hem encertat amb el model que es matricularien en un 15%, el 85% els hem fallat.

Queda clar doncs, que el nostre model l'hauríem de treballar millor incorporant alguna variable més que ens ajudi a ajustar-lo, sobretot pel que fa a la part dels matriculats. Com hem indicat previament, és curiós també que si mirem la mitjana d'aquestes variables realment  no deixen malament el model. Ens quedem amb un precision average  i un recall average del 67 i 71 respectivament.

## Random Forest

Intentarem millorar el classificador que hem obtingut amb el K Nearest Neighbours i l'Arbre de Decisió aplicant un altre classificador una mica més complexe. És un classificador molt fàcil d'aplicar però amb una dificultat afegida a l'hora d'interpretar els resultats.

### Crossvalidation

Apliquem el classificador que hem utilitzat per tal de definir el nostre model predictiu. Primer de tot el que fem és carregar les nostres dades aplicant un crossvalidation on hem aplicat un folds=10 indicant així que dividirem el nostre dataset en 10 parts aleatòries per tal de realitzar l'entrenament del nostre model.

Un cop aplicat això ens trobem amb el nostre primer resultat sorpresa:

<img src="https://jercapstone.github.io/UBCapstonePG/crossvalidationRF.jpg" />

El que ens ha sorprés és trobar-nos amb unes diferències tant elevades entre els accuracys dels diferents entrenaments que hem realitzat. Ens trobem accuracys que van entre el 0.53 o 0.54 que ens trobem a les proves realitzades en 3a, 2a i 5a posició i accuracys que volten 0.97 o 0.98 que són els que s'assignen a les proves 7a, 8a i 9a. És a dir, les proves realitzades al final tenen una accuracy molt superior a les realitzades al principi. 

Aquest resultat ens ha sorprès per que podria indicar que el dataset està ordenat per alguna variable que indica que les dades del final prediuen millor el model que les del principi. A priori aquesta hipòtesi no ha estat buscada i podria ser que potser les dades de les darreres proves siguin dades de campanyes més properes en el temps on potser la qualitat de les dades són una mica més bones que les de campanyes més antigues.


### Matriu de confusió

Analitzem ara la matriu de confusió on trobarem resultats semblants als que ens hem trobat en l'arbre de decisió. Aparentment una matriu que dona uns resultats que a priori podríem considerar que no són dolents a l'hora de definir el model però on trobarem sorpreses:


<img src="https://jercapstone.github.io/UBCapstonePG/confusionmatrixRF.jpg" />

En una primera mirada de la Matriu de confusió, ens diu que la predicció del nostre model té una precisió d'un 68% i un recall del 65%, un model amb uns resultats millorables però acceptables. No obstant, igual que ens havíem trobat en els arbres de decisió, si baixem una mica aquesta informació i aprofondim en els paràmetres precisió i recall, ens trobem amb el següent:

<img src="https://jercapstone.github.io/UBCapstonePG/confusionmatrixRFexp.jpg" />

Dels que hem predit com a no matriculats hem encertat un 73% i dels que hem predit com a matriculats n'hem encertat un 56%. Això ja ens diu que el model encerta molt millor les prediccions dels no matriculats que les prediccions d'estudiants matriculats.

Si aprofondim en la variable recall ens trobem amb la mateixa situació extranya que teníem al model d'arbres de decisió, dels que al dataset estan codificats com a no matriculats hem predit de forma correcta un 95% el que indicaria un encert gairebé perfecte. En canvi si mirem dels que eren matriculats quants s'han predit de forma correcta, veiem que aquest percentatge baixa a només el 16%. És a dir, dels que estaven matriculats només hem encertat amb el model que es matricularien en un 16%, el 84% els hem fallat.

Queda clar doncs, que el nostre model, al igual que el de l'arbre de decisió l'hauríem de treballar millor incorporant alguna variable més que ens ajudi a ajustar-lo, sobretot pel que fa a la part dels matriculats. Com hem indicat també al model d'arbres de decisió, és curiós també que si mirem la mitjana d'aquestes variables realment  no deixen malament el model. Ens quedem amb un precision average  i un recall average del 68 i 71 respectivament.


### Variables que expliquen el model

El darrer output que hem analitzat del classificador Random Forest és veure quines són les variables que està utilitzant per construir el model.

<img src="https://jercapstone.github.io/UBCapstonePG/variablesRF.jpg" />

En aquest cas veiem que de les 27 variables que teníem (26 si traiem la variable que volíem explicar) estem explicant el model només amb 9. D'aquestes 9 hi ha tres que tenen una mica més pes que la resta.


<img src="https://jercapstone.github.io/UBCapstonePG/variablesRFexp.jpg" />

Aquestes variables són la regió, que com hem explicat al principi indica la comunitat autònoma de l'usuari que ha realitzat el contacte amb la Universitat i que pesa un 33%, l'idioma del producte comprat i el producte comprat. Amb el coneixement que tenim del negoci, podem dir que el pes d'aquestes variables és esperat sobretot pel que fa a la regió ja que a la institució analitzada així com a la resta d'institucions d'educació superior d l'estat el pes territorial de les instituciosn encara és molt gran entre els estudiants a l'hora de decidir-se per buscar un centre on cursar els estudis superiors.

## Conclusions

Les principals conclussions extretes del treball que hem realitzat, són les següents:

<ul>Hem aplicat tres models per intentar predir si un usuari que s'apropa a una Universitat durant un procés de campanya de matriculació s'acabarà matriculant o no, en base a l'activitat generada durant el procés.
<ul>Els models aplicats són un model d'Arbres de decisió, el model de Nearest Neighbours i el model Random Forest.
<ul>Un cop aplicats els tres models podem dir, que els tres models són molt millorables ja que en cap dels tres hem obtingut uns nivells de bonança del model òptim tot i que entre els tres podem dir que el que millor funciona és el Random Forest.
<ul>En el Random Forest les variables que més influeixen en el model són la regió, el producte comprat i l'idioma del producte comprat.
<ul>El Random Forest prediu millor els estudiants que no es matricularan que els que es matricularan.
<ul>A nivell general, podem dir que existeix relació entre el perfil socio-demogràfic i la intenció de matrícula.
<ul>També existeix relació entre l' activitat generada durante el procés de matrícula i la intenció de matrícula.
<ul>Així doncs, és possible trobar un model predictiu de la intenció de matrícula a partir del perfil demogràfic de la persona interesada i l' activitat generada durant el procés de matrícula.

## Properes passes

Com a properes passes que ens posem, tenim les següents fites:

<ul>Analitzar la consistència de les dades per millorar la qualitat de la informació tractada.
<ul>Generar noves variables derivades de les que disposem actualment.
<ul>Identificar variables que permetin millorar la capacitat predictiva dels models.
<ul>Continuar avaluant mètodes de segmentació d'usuaris i de predicció del comportament.


