rules_list = [
  {
    "pattern": "(yes|yeah|yep|sure|absolutely|of course)(.*)",
    "responses": [
      "You seem quite certain. Why is that?",
      "Great! Can you explain why you feel so sure?",
      "I'm glad to hear that. Want to expand on it?"
    ]
  },
  {
    "pattern": "(no|nope|nah|not really)(.*)",
    "responses": [
      "Why not?",
      "Can you explain why you feel that way?",
      "What makes you say no?"
    ]
  },
  {
    "pattern": "(maybe|perhaps|possibly|not sure|don't know)(.*)",
    "responses": [
      "Uncertainty can be frustrating. What's making you unsure?",
      "Take your time — what do you think deep down?",
      "It's okay not to have all the answers right now."
    ]
  },
  {
    "pattern": "(.*)(always)(.*)",
    "responses": [
      "Can you think of a specific example when that happened?",
      "Do you really feel it happens all the time?",
      "Why do you think it always happens?"
    ]
  },
  {
    "pattern": "(.*)(never)(.*)",
    "responses": [
      "Never is a strong word. Are you sure about that?",
      "Why do you feel it has never happened?",
      "Has it really never happened even once?"
    ]
  },
  {
    "pattern": "(.*)(angry|mad|furious|frustrated)(.*)",
    "responses": [
      "What is making you feel so {1}?",
      "How do you usually deal with feeling {1}?",
      "It's okay to feel {1}. Let's talk about it."
    ]
  },
  {
    "pattern": "(.*)(anxious|worried|nervous)(.*)",
    "responses": [
      "What’s making you feel {1}?",
      "Is this something that often makes you {1}?",
      "Let’s talk more about what’s behind your {1} feelings."
    ]
  },
  {
    "pattern": "(.*)(lonely|alone|isolated)(.*)",
    "responses": [
      "I'm here with you. Why are you feeling {1}?",
      "Have you felt {1} for a while?",
      "What helps when you're feeling {1}?"
    ]
  },
  {
    "pattern": "(.*)(tired|exhausted|fatigued|burnt out)(.*)",
    "responses": [
      "What’s been draining your energy?",
      "Do you feel like you're getting enough rest?",
      "Maybe you need a break. Want to talk about what’s causing this?"
    ]
  },
  {
    "pattern": "(.*)(stress|stressed)(.*)",
    "responses": [
      "What’s been causing you stress lately?",
      "How do you usually cope with stress?",
      "Would talking about it help you feel better?"
    ]
  },
  {
    "pattern": "(.*)(dream|goal|aspiration|plan)(.*)",
    "responses": [
      "Tell me more about your {1}.",
      "Why is that {1} important to you?",
      "How long have you had that {1} in mind?"
    ]
  },
  {
    "pattern": "(.*)(death|die|dying|dead)(.*)",
    "responses": [
      "Death is a deep topic. What brought that to your mind?",
      "How do you feel when you think about death?",
      "Is this something personal for you?"
    ]
  },
  {
    "pattern": "(.*)(life|meaning|purpose)(.*)",
    "responses": [
      "What gives your life meaning?",
      "Let’s talk about your purpose — what drives you?",
      "Have you thought about what you want from life?"
    ]
  },
  {
    "pattern": "(hi|hello|hey|sup|yo|howdy)(.*)",
    "responses": [
      "Hey there! How are you feeling today?",
      "Hello! What would you like to talk about?",
      "Hi! I'm here to listen.",
      "Howdy! Let's chat.",
      "Yo! What's on your mind?"
    ]
  },
  {
    "pattern": "good (morning|afternoon|evening)(.*)",
    "responses": [
      "Good {0} to you too!",
      "Wishing you a great {0}.",
      "Hope you're having a lovely {0}!"
    ]
  },
  {
    "pattern": "How are you(.*)",
    "responses": [
      "I'm a program, so I'm as good as my last function call!",
      "Let's focus on you. How are you doing?",
      "I'm here and ready to chat — how are you?"
    ]
  },
  {
    "pattern": "What is your name(.*)",
    "responses": [
      "You can call me Eliza.",
      "I'm Eliza, your conversational companion.",
      "They call me Eliza — how can I help?"
    ]
  },
  {
    "pattern": "Who created you(.*)",
    "responses": [
      "I was originally created by Joseph Weizenbaum in 1966.",
      "A human programmer brought me into the world.",
      "A brilliant mind built me to listen and respond."
    ]
  },
  {
    "pattern": "I feel (.*)",
    "responses": [
      "Why do you feel {0}?",
      "How long have you felt {0}?",
      "Tell me more about feeling {0}.",
      "What triggered these feelings of {0}?"
    ]
  },
  {
    "pattern": "I am (.*)",
    "responses": [
      "Do you enjoy being {0}?",
      "Why are you {0}?",
      "Have you always been {0}?",
      "How does being {0} impact your daily life?"
    ]
  },
  {
    "pattern": "I don't know(.*)",
    "responses": [
      "Why do you think you don't know?",
      "What would it mean if you did know?",
      "Sometimes not knowing is okay. Let's explore it together."
    ]
  },
  {
    "pattern": "My name is (.*)",
    "responses": [
      "Nice to meet you, {0}.",
      "Hello {0}, how are you feeling today?",
      "Welcome, {0}. What would you like to talk about?"
    ]
  },
  {
    "pattern": "(.*)(sad|depressed|unhappy)(.*)",
    "responses": [
      "I'm sorry to hear you're feeling {1}.",
      "What do you think is making you {1}?",
      "How long have you felt {1}?",
      "Have you talked to anyone about feeling {1}?"
    ]
  },
  {
    "pattern": "(.*)(good|excited|happy|content)(.*)",
    "responses": [
      "It's great that you are feeling {1}.",
      "I'm glad to hear that!",
      "Being {1} is wonderful — what's making you feel that way?"
    ]
  },
  {
    "pattern": "(.*)(apologise|apologies|sorry)(.*)",
    "responses": [
      "Please don't apologise.",
      "Apologies are not necessary.",
      "I've told you that apologies are not required.",
      "It did not bother me. Please continue."
    ]
  },
  {
    "pattern": "Do you (.*)",
    "responses": [
      "Why does it matter whether I {0}?",
      "Would it make you feel better if I did {0}?",
      "Do you think I should {0}?"
    ]
  },
  {
    "pattern": "Can you (.*)",
    "responses": [
      "What makes you think I can {0}?",
      "Would it help if I could {0}?",
      "Do you want me to {0}?"
    ]
  },
  {
    "pattern": "Because (.*)",
    "responses": [
      "Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason explain everything?"
    ]
  },
  {
    "pattern": "I can't (.*)",
    "responses": [
      "What makes you say you can't {0}?",
      "Have you really tried to {0}?",
      "What’s stopping you from {0}?"
    ]
  },
  {
    "pattern": "I want (.*)",
    "responses": [
      "Why do you want {0}?",
      "Would getting {0} make you happy?",
      "What would it mean if you got {0}?"
    ]
  },
  {
    "pattern": "You are (.*)",
    "responses": [
      "What makes you think I am {0}?",
      "Why do you say I am {0}?",
      "Does it bother you if I am {0}?"
    ]
  },
  {
    "pattern": "I (.*) you",
    "responses": [
      "Why do you {0} me?",
      "Do you often {0} people?",
      "What makes you say that you {0} me?"
    ]
  },
  {
    "pattern": "(.*) mother(.*)",
    "responses": [
      "Tell me more about your mother.",
      "How is your relationship with your mother?",
      "What comes to mind when you think about your mother?"
    ]
  },
  {
    "pattern": "(.*) father(.*)",
    "responses": [
      "Tell me more about your father.",
      "Do you have strong feelings about your father?",
      "How did your father influence you?"
    ]
  },
  {
    "pattern": "(.*) friend(.*)",
    "responses": [
      "Tell me more about your friends.",
      "What makes someone a good friend to you?",
      "Do you feel supported by your friends?"
    ]
  },
  {
    "pattern": "(.*) love(.*)",
    "responses": [
      "Love is a complex feeling. What does it mean to you?",
      "Tell me more about love.",
      "Is love something you experience often?"
    ]
  },
  {
    "pattern": "(.*) hate(.*)",
    "responses": [
      "That's a strong word. Why do you feel that way?",
      "Hate can be difficult to carry. What fuels it?",
      "Would you like to explore where that feeling comes from?"
    ]
  },
  {
    "pattern": "(.*)",
    "responses": [
      "Can you elaborate on that?",
      "How does that make you feel?",
      "Please tell me more.",
      "Interesting... go on.",
      "And what do you think that means?",
      "Could you say that in a different way?"
    ]
  }
]

initial_prompts = ["How do you do. Please tell me your problem." , "Hi, is something bothering you today?", 
                              "Hello there! Do you need help with anything?", "How are you doing?"]
        
final_prompts = ["Goodbye. It was nice talking to you.","Goodbye.  This was really a nice talk.", "Bye. It was nice talking to you.", "Bye. See you soon!"
                            "Goodbye. I'm looking forward to our next session.", "This was a good session, wasn't it --but time is over now. Goodbye.", 
                            "Maybe we could discuss this moreover in our next session? Goodbye."]
        
quit_keywords = [ "bye", "goodbye", "done","exit", "quit", "see you", "till next time"]
