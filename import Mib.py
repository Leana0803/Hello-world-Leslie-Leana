triples = { (alien.No_Cabine, alien.Nom, gardien.Nom)
              for alien in baseAlien for gardien in baseGardien
              if gardien.No_Cabine == alien.No_Cabine}               
