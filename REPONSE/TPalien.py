# -*- coding: utf-8 -*-

from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?
q1={gardien.Nom for gardien in BaseGardiens }

### Question 2 : quel est l'ensemble des villes d'origine des agents?
q2= { agent.Ville for agent in BaseAgents }

### Question 3 : quel est l'ensemble des triplets (no de cabine,alien,gardien) pour chaque cabine?
q3={ (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine }

### Question 4 : quel est l'ensemble des couples (alien,allée) pour chaque alien?
q4={ (alien.Nom, cabine.NoAllee) for alien in BaseAliens for cabine in BaseCabines if alien.NoCabine==cabine.NoCabine }

### Question 5 : quel est l'ensemble de tous les aliens de l'allée 2?
q5={ (alien.Nom) for alien in BaseAliens for cabine in BaseCabines if alien.NoCabine==cabine.NoCabine and cabine.NoAllee=='2'}

### Question 6 : quel est l'ensemble de toutes les planètes dont sont originaires les aliens habitant une cellule de numéro pair?
q6={ (alien.Planete) for alien in BaseAliens if float(alien.NoCabine)%2==0 }

### Question 7 : quel est l'ensemble des aliens dont les gardiens sont originaires de Terminus?
q7={ (alien.Nom) for alien in BaseAliens for gardien in BaseGardiens for agent in BaseAgents if alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and agent.Ville=='Terminus'}

### Question 8 : quel est l'ensemble des gardiens des aliens féminins qui mangent du bortsch?
q8={ (gardien.Nom) for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams if miam.Aliment=='Bortsch' and miam.NomAlien==alien.Nom and alien.Sexe=='F' and alien.NoCabine==gardien.NoCabine }

### Question 9 : quel est l'ensemble des cabines dont les gardiens sont originaires de Terminus ou dont les aliens sont des filles?
q9={ (cabine.NoCabine) for cabine in BaseCabines for gardien in BaseGardiens for alien in BaseAliens for agent in BaseAgents if (gardien.Nom==agent.Nom and agent.Ville=='Terminus' and gardien.NoCabine==cabine.NoCabine) or (alien.Sexe=='F' and alien.NoCabine==cabine.NoCabine) }

### Question 10 : Y a-t-il des aliments qui commencent par la même lettre que le nom du gardien qui surveille l'alien qui les mange ?
q10={ (gardien.Nom,miam.Aliment) for gardien in BaseGardiens for miam in BaseMiams for alien in BaseAliens if miam.NomAlien==alien.Nom and alien.NoCabine==gardien.NoCabine and miam.Aliment[0]==gardien.Nom[0] }

### Question 11 : Y a-t-il des aliens originaires d'Euterpe ?
q11={ (alien.Nom) for alien in BaseAliens if alien.Planete=='Euterpe' }

### Question 12 : Est-ce que tous les aliens ont un 'x' dans leur nom?
q12=


>>> q1
{'Darell', 'Hardin', 'Seldon', 'Trevize', 'Branno', 'Pelorat', 'Demerzel', 'Riose', 'Dornick'}
>>> q2
{'Hesperos', 'Kalgan', 'Terminus', 'Uco'}
>>> q3
{('4', 'Darneurane', 'Seldon'), ('1', 'Zorglub', 'Branno'), ('8', 'Arghh', 'Pelorat'), ('9', 'Joranum', 'Riose'), ('2', 'Blorx', 'Darell'), ('7', 'Zzzzzz', 'Trevize'), ('3', 'Urxiz', 'Demerzel'), ('6', 'Mulzo', 'Hardin'), ('4', 'Zbleurdite', 'Seldon')}
>>> q4
{('Zbleurdite', '1'), ('Joranum', '2'), ('Blorx', '1'), ('Urxiz', '1'), ('Zzzzzz', '2'), ('Mulzo', '2'), ('Arghh', '2'), ('Zorglub', '1'), ('Darneurane', '1')}
>>> q5
{'Zzzzzz', 'Arghh', 'Mulzo', 'Joranum'}
>>> q6
{'Trantor', 'Nexon', 'Euterpe', 'Helicon'}
>>> q7
{'Zorglub', 'Mulzo', 'Blorx', 'Joranum', 'Darneurane', 'Zbleurdite'}
>>> q8
{'Seldon', 'Riose'}
>>> q9
{'9', '7', '1', '6', '2', '4'}
>>> q10
{('Seldon', 'Schwanstucke'), ('Branno', 'Bortsch')}
>>> q11
{'Blorx', 'Joranum'}
