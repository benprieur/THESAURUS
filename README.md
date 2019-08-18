# Données thésaurus fr.wiktionary vers une base MySQL

Ce code Python consiste en consolider les données issues du Wiktionnaire, qui concernent les thésaurus en français, dans une base MySQL.
* Une table TREVISION contient toutes les révisions (éditions).
* Une table TUSER contient toutes les users (ip ou non) impliqués dans l'édition de thésaurus en français.
* Une table TTHESAURUS contient tous les thésaurus en français de fr.wiktionary.

Ce code est utilisé/repris par un client web de visualisation, THESAURUS-web.

Au 18 août 2019, il existe 416 thésaurus en français sur fr.wikt édités par 389 édit.eur.rice.s (IP ou compte inscrit) hors bot, pour un total de 8 012 éditions.
