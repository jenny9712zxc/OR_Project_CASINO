from transitions.extensions import GraphMachine

from utils import send_text_message
#"Don't be sad >///< There already does't have any answer for you to choose in this case.I know."
#"You Win!"
#"I won't give you any wrong answer,so this time i won't give you answer.There isn't any correct answer in this range."

#“taiwan“,”china”, “mongolia”, “north korea”, “south korea”, “japan”, 
# “the philippines”, “vietnam”, “laos“, “cambodia”, “burma”, “thailand”,
#  “malaysia”, “brunei”, “singapore”, “indonesia”, “east timor”, “nepal”, 
# “bhutan”, “bangladesh”, “india”, “pakistan”, “sri lanka”, “the maldives”, 
# “kazakhstan”, “kyrgyzstan”, “tajikistan”, “uzbekistan”, “turkmenistan”,
#  “afghanistan”, “iraq”, “iran”, “syria”, “jordan”, “lebanon”, “israel”, 
# “the palestinian”, “saudi arabia”, “bahrain”, “qatar”, “kuwait”, 
# “the united arab emirates”, “oman”, “yemen”, “georgia”, “armenia”,
#  “azerbaijan”, “turkey”, “cyprus”
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    #hello
    def is_going_to_hello(self, event):
        text = event.message.text
        return text.lower() == "hello"
   
    def on_enter_hello(self, event):
        print("I'm entering hello")
        reply_token = event.reply_token
        send_text_message(reply_token, "a")
        self.go_back()
       

    #the philippines
    def is_going_to_thephilippines(self, event):
        text = event.message.text
        return text.lower() == "the philippines"
   
    def on_enter_thephilippines(self, event):
        print("I'm entering thephilippines")
        reply_token = event.reply_token
        send_text_message(reply_token, "sri lanka")
        #self.go_back()
       
    #laos
    def is_going_to_laos(self, event):
        text = event.message.text
        return text.lower() == "laos"
   
    def on_enter_laos(self, event):
        print("I'm entering laos")
        reply_token = event.reply_token
        send_text_message(reply_token, "sri lanka")
        #self.go_back()
      
    #the maldives
    def is_going_to_themaldives(self, event):
        text = event.message.text
        return text.lower() == "the maldives"
   
    def on_enter_themaldives(self, event):
        print("I'm entering themaldives")
        reply_token = event.reply_token
        send_text_message(reply_token, "sri lanka")
        #self.go_back()
      
    #the united arab emirates
    def is_going_to_theunitedarabemirates(self, event):
        text = event.message.text
        return text.lower() == "the united arab emirates"
   
    def on_enter_theunitedarabemirates(self, event):
        print("I'm entering theunitedarabemirates")
        reply_token = event.reply_token
        send_text_message(reply_token, "sri lanka")
        #self.go_back()
      
    #cyprus
    def is_going_to_cyprus(self, event):
        text = event.message.text
        return text.lower() == "cyprus"
   
    def on_enter_cyprus(self, event):
        print("I'm entering cyprus")
        reply_token = event.reply_token
        send_text_message(reply_token, "sri lanka")
        #self.go_back()
      
    #singapore
    def is_going_to_singapore(self, event):
        text = event.message.text
        return text.lower() == "singapore"
   
    def on_enter_singapore(self, event):
        print("I'm entering singapore")
        reply_token = event.reply_token
        send_text_message(reply_token, "east timor")
        #self.go_back()
           
    #iraq
    def is_going_to_iraq(self, event):
        text = event.message.text
        return text.lower() == "iraq"
   
    def on_enter_iraq(self, event):
        print("I'm entering iraq")
        reply_token = event.reply_token
        send_text_message(reply_token, "qatar")
        #self.go_back()
       
    #nepal
    def is_going_to_nepal(self, event):
        text = event.message.text
        return text.lower() == "nepal"
   
    def on_enter_nepal(self, event):
        print("I'm entering nepal")
        reply_token = event.reply_token
        send_text_message(reply_token, "lebanon")
        #self.go_back()

    def is_going_to_state17(self, event):
        text = event.message.text
        return text.lower() == "north korea"
   
    def on_enter_state17(self, event):
        text = event.message.text
        print("I'm entering state17")
        if(text.lower() == "north korea"):
            reply_token = event.reply_token
            send_text_message(reply_token, "azerbaijan")
            #self.go_back()
        #self.go_back()
       
    def is_going_to_state18(self, event):
        return True
   
    def on_enter_state18(self, event):
        print("I'm entering state18")
        reply_token = event.reply_token
        send_text_message(reply_token, "Don't be sad >///< There already does't have any answer for you to choose in this case.I know.")
        self.go_back()
    #another kind end point
       
    #israel
    def is_going_to_israel(self, event):
        text = event.message.text
        return text.lower() == "israel"
   
    def on_enter_israel(self, event):
        print("I'm entering israel")
        reply_token = event.reply_token
        send_text_message(reply_token, "lebanon")
        #self.go_back()
   
    #lebanon
    def is_going_to_lebanon(self, event):
        text = event.message.text
        return text.lower() == "lebanon"
   
    def on_enter_lebanon(self, event):
        print("I'm entering lebanon")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()

    def is_going_to_state14(self, event):
        text = event.message.text
        return text.lower() == "afghanistan"
    
    def on_enter_state14(self, event):
        text = event.message.text
        print("I'm entering state14")
        if(text.lower() == "afghanistan"):
            reply_token = event.reply_token
            send_text_message(reply_token, "nepal")
            #self.go_back()
        #self.go_back()
  
    def is_going_to_state15(self, event):
        text = event.message.text
        return text.lower() == "azerbaijan"
    
    def on_enter_state15(self, event):
        text = event.message.text
        print("I'm entering state15")
        if(text.lower() == "azerbaijan"):
            reply_token = event.reply_token
            send_text_message(reply_token, "nepal")
            #self.go_back()
        #self.go_back()        
    def is_going_to_state16(self, event):
        text = event.message.text
        return text.lower() == "laos"
    
    def on_enter_state16(self, event):
        text = event.message.text
        print("I'm entering state16")
        if(text.lower() == "laos"):
            reply_token = event.reply_token
            send_text_message(reply_token, "You Win!")
            #self.go_back()
        self.go_back()        
    #end point

    #kuwait
    def is_going_to_kuwait(self, event):
        text = event.message.text
        return text.lower() == "kuwait"
   
    def on_enter_kuwait(self, event):
        print("I'm entering kuwait")
        reply_token = event.reply_token
        send_text_message(reply_token, "turkey")
        #self.go_back()

    def is_going_to_state13(self, event):
        text = event.message.text
        return text.lower() == "yemen"
    
    def on_enter_state13(self, event):
        text = event.message.text
        print("I'm entering state13")
        if(text.lower() == "yemen"):
            reply_token = event.reply_token
            send_text_message(reply_token, "nepal")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be yemen or the other correct answer!")
            self.go_back()
        #self.go_back()
    
    #taiwan    
    def is_going_to_taiwan(self, event):
        text = event.message.text
        return text.lower() == "taiwan"
    
    def on_enter_taiwan(self, event):
        print("I'm entering taiwan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
    
    #japan
    def is_going_to_japan(self, event):
        text = event.message.text
        return text.lower() == "japan"
    
    def on_enter_japan(self, event):
        print("I'm entering japan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
    
    #bhutan
    def is_going_to_bhutan(self, event):
        text = event.message.text
        return text.lower() == "bhutan"
    
    def on_enter_bhutan(self, event):
        print("I'm entering bhutan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
    
    #pakistan
    def is_going_to_pakistan(self, event):
        text = event.message.text
        return text.lower() == "pakistan"
    
    def on_enter_pakistan(self, event):
        print("I'm entering pakistan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
    
    #kazakhstan
    def is_going_to_kazakhstan(self, event):
        text = event.message.text
        return text.lower() == "kazakhstan"
    
    def on_enter_kazakhstan(self, event):
        print("I'm entering kazakhstan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
    
    #kyrgyzstan
    def is_going_to_kyrgyzstan(self, event):
        text = event.message.text
        return text.lower() == "kyrgyzstan"
    
    def on_enter_kyrgyzstan(self, event):
        print("I'm entering kyrgyzstan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
    
    #tajikistan
    def is_going_to_tajikistan(self, event):
        text = event.message.text
        return text.lower() == "tajikistan"
    
    def on_enter_tajikistan(self, event):
        print("I'm entering tajikistan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
 
    #uzbekistan
    def is_going_to_uzbekistan(self, event):
        text = event.message.text
        return text.lower() == "uzbekistan"
    
    def on_enter_uzbekistan(self, event):
        print("I'm entering uzbekistan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
 
    #turkmenistan
    def is_going_to_turkmenistan(self, event):
        text = event.message.text
        return text.lower() == "turkmenistan"
    
    def on_enter_turkmenistan(self, event):
        print("I'm entering turkmenistan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
 
    #iran
    def is_going_to_iran(self, event):
        text = event.message.text
        return text.lower() == "iran"
    
    def on_enter_iran(self, event):
        print("I'm entering iran")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
 
    #jordan
    def is_going_to_jordan(self, event):
        text = event.message.text
        return text.lower() == "jordan"
    
    def on_enter_jordan(self, event):
        print("I'm entering jordan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()

    #the palestinian
    def is_going_to_thepalestinian(self, event):
        text = event.message.text
        return text.lower() == "the palestinian"
    
    def on_enter_thepalestinian(self, event):
        print("I'm entering thepalestinian")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()

    #bahrain
    def is_going_to_bahrain(self, event):
        text = event.message.text
        return text.lower() == "bahrain"
    
    def on_enter_bahrain(self, event):
        print("I'm entering bahrain")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()

    #oman
    def is_going_to_oman(self, event):
        text = event.message.text
        return text.lower() == "oman"
    
    def on_enter_oman(self, event):
        print("I'm entering oman")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()

    #yemen
    def is_going_to_yemen(self, event):
        text = event.message.text
        return text.lower() == "yemen"
    
    def on_enter_yemen(self, event):
        print("I'm entering yemen")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
    
    #(9 ,11 12)(10 ,11 12)
    #vietnam
    def is_going_to_vietnam(self, event):
        text = event.message.text
        return text.lower() == "vietnam"
   
    def on_enter_vietnam(self, event):
        print("I'm entering vietnam")
        reply_token = event.reply_token
        send_text_message(reply_token, "malaysia")
        #self.go_back()
       
    #afghanistan
    def is_going_to_afghanistan(self, event):
        text = event.message.text
        return text.lower() == "afghanistan"
   
    def on_enter_afghanistan(self, event):
        print("I'm entering afghanistan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()
    
    def is_going_to_state9(self, event):
        text = event.message.text
        return text.lower() == "azerbaijan"

    def on_enter_state9(self, event):
        text = event.message.text
        print("I'm entering state9")
        if(text.lower() == "azerbaijan"):
            reply_token = event.reply_token
            send_text_message(reply_token, "nepal")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be azerbaijan or the other correct answer!")
            self.go_back()
        #self.go_back()

    #azerbaijan 
    def is_going_to_azerbaijan(self, event):
        text = event.message.text
        return text.lower() == "azerbaijan"
   
    def on_enter_azerbaijan(self, event):
        print("I'm entering azerbaijan")
        reply_token = event.reply_token
        send_text_message(reply_token, "north korea")
        #self.go_back()

    def is_going_to_state10(self, event):
        text = event.message.text
        return text.lower() == "afghanistan"

    def on_enter_state10(self, event):
        text = event.message.text
        print("I'm entering state10")
        if(text.lower() == "afghanistan"):
            reply_token = event.reply_token
            send_text_message(reply_token, "nepal")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be afghanistan or the other correct answer!")
            self.go_back()
        #self.go_back()

    def is_going_to_state11(self, event):
        text = event.message.text
        return text.lower() == "laos"

    def on_enter_state11(self, event):
        text = event.message.text        
        print("I'm entering state11")
        if(text.lower() == "laos"):
            reply_token = event.reply_token
            send_text_message(reply_token, "You Win!")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be wrong!")
        self.go_back()
    #end point

    def is_going_to_state12(self, event):
        text = event.message.text
        return text.lower() == "lebanon"

    def on_enter_state12(self, event):
        text = event.message.text        
        print("I'm entering state12")
        if(text.lower() == "lebanon"):
            reply_token = event.reply_token
            send_text_message(reply_token, "You Win!")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be wrong!")
        self.go_back()
    #end point

    #north korea
    def is_going_to_northkorea(self, event):
        text = event.message.text
        return text.lower() == "north korea"
   
    def on_enter_northkorea(self, event):
        print("I'm entering northkorea")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "nepal"
    
    def on_enter_state7(self, event):
        text = event.message.text
        print("I'm entering state7")
        if(text.lower() == "nepal"):
            reply_token = event.reply_token
            send_text_message(reply_token, "laos")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be laos or the other correct answer!")
            self.go_back()
        #self.go_back()

    def is_going_to_state8(self, event):
        text = event.message.text
        return((text.lower() == "singapore") or (text.lower() == "sri lanka")or (text.lower() == "syria")or (text.lower() == "saudi arabia")or (text.lower() == "south korea"))
    
    def on_enter_state8(self, event):
        text = event.message.text        
        print("I'm entering state8")
        if((text.lower() == "singapore") or (text.lower() == "sri lanka")or (text.lower() == "syria")or (text.lower() == "saudi arabia")or (text.lower() == "south korea")):
            reply_token = event.reply_token
            send_text_message(reply_token, "You Win!")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be singapore or sri lanka or south korea or syria or saudi arabia or the other correct answer!")
        self.go_back()
    #end point

    #brunei
    def is_going_to_brunei(self, event):
        text = event.message.text
        return text.lower() == "brunei"
   
    def on_enter_brunei(self, event):
        print("I'm entering brunei")
        reply_token = event.reply_token
        send_text_message(reply_token, "iran")
        #self.go_back()
   
    #turkey
    def is_going_to_turkey(self, event):
        text = event.message.text
        return text.lower() == "turkey"
   
    def on_enter_turkey(self, event):
        print("I'm entering turkey")
        reply_token = event.reply_token
        send_text_message(reply_token, "yemen")
        #self.go_back()

    #china
    def is_going_to_china(self, event):
        text = event.message.text
        return text.lower() == "china"
   
    def on_enter_china(self, event):
        print("I'm entering china")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()

    #mongolia
    def is_going_to_mongolia(self, event):
        text = event.message.text
        return text.lower() == "mongolia"

    def on_enter_mongolia(self, event):
        print("I'm entering mongolia")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()

    #south korea
    def is_going_to_southkorea(self, event):
        text = event.message.text
        return text.lower() == "south korea"
  
    def on_enter_southkorea(self, event):
        print("I'm entering southkorea")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()

    #cambodia
    def is_going_to_cambodia(self, event):
        text = event.message.text
        return text.lower() == "cambodia"
   
    def on_enter_cambodia(self, event):
        print("I'm entering cambodia")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #burma
    def is_going_to_burma(self, event):
        text = event.message.text
        return text.lower() == "burma"
   
    def on_enter_burma(self, event):
        print("I'm entering burma")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #malaysia
    def is_going_to_malaysia(self, event):
        text = event.message.text
        return text.lower() == "malaysia"
   
    def on_enter_malaysia(self, event):
        print("I'm entering malaysia")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #indonesia
    def is_going_to_indonesia(self, event):
        text = event.message.text
        return text.lower() == "indonesia"
   
    def on_enter_indonesia(self, event):
        print("I'm entering indonesia")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
    #india
    def is_going_to_india(self, event):
        text = event.message.text
        return text.lower() == "india"
   
    def on_enter_india(self, event):
        print("I'm entering india")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #sri lanka
    def is_going_to_srilanka(self, event):
        text = event.message.text
        return text.lower() == "sri lanka"
   
    def on_enter_srilanka(self, event):
        print("I'm entering srilanka")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #syria
    def is_going_to_syria(self, event):
        text = event.message.text
        return text.lower() == "syria"
   
    def on_enter_syria(self, event):
        print("I'm entering syria")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #saudi arabia
    def is_going_to_saudiarabia(self, event):
        text = event.message.text
        return text.lower() == "saudi arabia"
   
    def on_enter_saudiarabia(self, event):
        print("I'm entering saudiarabia")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #georgia
    def is_going_to_georgia(self, event):
        text = event.message.text
        return text.lower() == "georgia"
   
    def on_enter_georgia(self, event):
        print("I'm entering georgia")
        reply_token = event.reply_token
        send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #armenia
    #def is_going_to_armenia(self, event):
    #   text = event.message.text
    #   return text.lower() == "armenia"
   
    #def on_enter_armenia(self, event):
    #    print("I'm entering armenia")
    #    reply_token = event.reply_token
    #    send_text_message(reply_token, "afghanistan")
        #self.go_back()
  
    #Xa case

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "north korea"
    
    def on_enter_state3(self, event):
        text = event.message.text
        print("I'm entering state3")
        if(text.lower() == "north korea"):
            reply_token = event.reply_token
            send_text_message(reply_token, "azerbaijan")
    
    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "nepal"
    
    def on_enter_state6(self, event):
        text = event.message.text        
        print("I'm entering state6")
        if(text.lower() == "nepal"):
            reply_token = event.reply_token
            send_text_message(reply_token, "You Win!")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be "+ text.lower() +" or the other correct answer!")
        self.go_back()
    #end point

    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "nepal"
    
    def on_enter_state4(self, event):
        text = event.message.text
        print("I'm entering state4")
        if(text.lower() == "nepal"):
            reply_token = event.reply_token
            send_text_message(reply_token, "lebanon")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be north korea or the other correct answer!")
            self.go_back()
        #self.go_back()

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "north korea"
    
    def on_enter_state5(self, event):
        text = event.message.text        
        print("I'm entering state5")
        if(text.lower() == "north korea"):
            reply_token = event.reply_token
            send_text_message(reply_token, "You win!")
            #self.go_back()
        else:
            reply_token = event.reply_token
            send_text_message(reply_token, "your answer might be "+ text.lower() +" or the other correct answer!")
        self.go_back()
    #end point   

    #thailand
    def is_going_to_thailand(self, event):
        text = event.message.text
        return text.lower() == "thailand"
   
    def on_enter_thailand(self, event):
        print("I'm entering thailand")
        reply_token = event.reply_token
        send_text_message(reply_token, "I won't give you any wrong answer,so this time i won't give you answer.There isn't any correct answer in this range.")
        self.go_back()
    #another end point 2
 
    #bangladesh
    def is_going_to_bangladesh(self, event):
        text = event.message.text
        return text.lower() == "bangladesh"
   
    def on_enter_bangladesh(self, event):
        print("I'm entering bangladesh")
        reply_token = event.reply_token
        send_text_message(reply_token, "I won't give you any wrong answer,so this time i won't give you answer.There isn't any correct answer in this range.")
        self.go_back()
    #another end point 2             
    
    #east timor
    def is_going_to_easttimor(self, event):
        text = event.message.text
        return text.lower() == "east timor"
   
    def on_enter_easttimor(self, event):
        print("I'm entering easttimor")
        reply_token = event.reply_token
        send_text_message(reply_token, "I won't give you any wrong answer,so this time i won't give you answer.There isn't any correct answer in this range.")
        self.go_back()
    #another end point 2
    
    #qatar
    def is_going_to_qatar(self, event):
        text = event.message.text
        return text.lower() == "qatar"
   
    def on_enter_qatar(self, event):
        print("I'm entering qatar")
        reply_token = event.reply_token
        send_text_message(reply_token, "I won't give you any wrong answer,so this time i won't give you answer.There isn't any correct answer in this range.")
        self.go_back()
    #another end point 2
 