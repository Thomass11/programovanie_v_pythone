import re

# Napíšte funkciu, ktorá zanalyzuje vstup, oddelí dáta:
# osobne cislo, meno, priezvisko, cele meno, email, tyzdenny fond vydeleny 60, datum zaciatku zamestnanca a vypise na konzolu
import_text = """
91001;Alena;Young;Alena Young;Alena.Young@email.com;2400;2021-06-01;NULL
91002;Klara;Old;Klara Old;Klara.Old@email.com;1800;2020-06-01;NULL
91003;Sona;Smart;Sona Smart;Sona.Smart@email.com;1200;2022-06-01;NULL
91001;Alena;Young;Alena Young;Alena.Young@email.com;2400;2020-08-15;NULL
91002;Klara;Old;Klara Old;Klara.Old@email.com;2400;2020-06-01;NULL
91003;Sona;Smart;Sona Smart;Sona.Smart@email.com;1200;2020-06-01;NULL
50101;Marah;Durimeh;Marah Durimeh;Marah.Durimeh@email.com;2400;2020-09-01;NULL
50102;Old;Firehand;Old Firehand;Old.Firehand@email.com;2400;2021-09-01;NULL
50103;Sam;Hawkens;Sam Hawkens;Sam.Hawkens@email.com;2400;2020-09-01;NULL
50104;Old;Shatterhand;Old Shatterhand;Old.Shatterhand@email.com;2400;2020-09-01;NULL
50105;Vinnetou;V.;Vinnetou V.;Vinnetou.V.@email.com;2400;2020-09-01;NULL
50106;Dalibor;Vrana;Dalibor Vrana;Dalibor.Vrana@email.com;2400;2021-09-01;NULL
50107;Pan;Parizek;Pan Parizek;Pan.Parizek@email.com;2400;2020-09-01;NULL
50108;Erna;Parizkova;Erna Parizkova;Erna.Parizkova@email.com;2400;2020-09-01;NULL
50109;Marena;Skopkova;Marena Skopkova;Marena.Skopkova@email.com;1800;2020-09-01;NULL
50110;Vladimir;Skopek;Vladimir Skopek;Vladimir.Skopek@email.com;2400;2020-09-01;NULL
50111;Blazena;Skopkova;Blazena Skopkova;Blazena.Skopkova@email.com;2400;2020-09-01;NULL
50112;Venca;Konopnik;Venca Konopnik;Venca.Konopnik@email.com;2400;2020-09-01;NULL
50113;Otik;Rakosnik;Otik Rakosnik;Otik.Rakosnik@email.com;2400;2020-09-01;NULL
50114;Karel;Pavek;Karel Pavek;Karel.Pavek@email.com;2400;2020-09-01;NULL
50115;Josef;Turek;Josef Turek;Josef.Turek@email.com;2400;2020-09-01;NULL
50116;Jana;Turkova;Jana Turkova;Jana.Turkova@email.com;2400;2020-09-01;NULL
50117;Zuzana;Petrova;Zuzana Petrova;Zuzana.Petrova@email.com;2400;2020-09-01;NULL
50118;Olino;Zrubec;Olino Zrubec;Olino.Zrubec@email.com;2400;2020-09-01;NULL
50119;Bela;Strinkova;Bela Strinkova;Bela.Strinkova@email.com;2400;2020-09-01;NULL
50120;Maja;Petrova;Maja Petrova;Maja.Petrova@email.com;1800;2020-09-01;NULL
10201;Sirius;Black;Sirius Black;Sirius.Black@email.com;2400;2021-08-15;NULL
10202;Death;Eater;Death Eater;Death.Eater@email.com;1200;2022-01-01;NULL
"""

# Príklad výstupu:
# -----------------------
# Personal number: 91001
# Name: Alena
# Name: Young
# Full name: Alena Young      
# Email: Alena.Young@email.com
# Weekly fund: 40.0
# Employment start: 01.06.2021
# -----------------------
