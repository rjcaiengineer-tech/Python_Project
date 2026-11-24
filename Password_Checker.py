password = input (" Entrez le mot de passe")


def password_checker():
          Score = 0
          if Lo_password():
               Score = Score+1
          if Up_password ():
               Score = Score+1
         if len(password):
               Score = Score+1 
         if carac_speciaux():
                Score = Score +1


print( "Score :" = Score, "/ 5" )


           

def len_password():

            for i in password():
                 If  len(password) >= 8: 
                       return true
                 
              return false   
          

           
                 

def Up_password():
         For i in password:
                 if i.isuppercase:
                     return true
                 
          return false


                
def Lo_password():
           For i in password:
                  If i.islower:
                     return true
                
             return false

def  caract_speciaux():

             speciaux == " #$%@&*!^+×÷=/_<>[](/'/"/:/;,? "
             For i in speciaux:
                    if i in speciaux:
                        return true

             return false


password_checker()
