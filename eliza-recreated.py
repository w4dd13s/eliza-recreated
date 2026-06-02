import re 
import random
import rules

class Eliza():
    def __init__(self):            
        self.rules_list = rules.rules_list
        self.initial_prompts = rules.initial_prompts
        self.final_prompts = rules.final_prompts
        self.quit_keywords = set(k.lower() for k in rules.quit_keywords)        
        self.show_intro()

        print("Eliza:", random.choice(self.initial_prompts))
    
    def show_intro(self):
        intro_text = """
        Welcome to                                                                    
                        EEEEEE  LL      IIII  ZZZZZZZ   AAAAA                       
                        EE      LL       II       ZZ   AA   AA                      
                        EEEEE   LL       II     ZZZ    AAAAAAA                      
                        EE      LL       II    ZZ      AA   AA                      
                        EEEEEE  LLLLLL  IIII  ZZZZZZZ  AA   AA                      

            ELIZA is one of the first natural language processing programs developed in the mid-60s. 
            This version is a Python remake — simple, lightweight, and beginner-friendly.  
            It mimics a therapist using pattern matching and substitution. 
            The goal is to show how simple rules and clever regex can simulate conversation.  
            A great entry point for understanding how early chatbots worked — and how far we've come.  
            
        """
        print(intro_text)
    
    def respond(self,user_input):
        for rule in self.quit_keywords:
            if rule == user_input:
                return random.choice(self.final_prompts)
            
        for rule in self.rules_list:
            match = re.match(rule["pattern"], user_input,re.IGNORECASE)
            if match:
                return random.choice(rule["responses"]).format(*match.groups())
    
    def chat(self):
        while(True):
            user_input = input("You: ")
            print("Eliza: " + self.respond(user_input))
            if user_input in self.quit_keywords:
                break

if __name__ == "__main__":
    eliza = Eliza()
    eliza.chat()
