#!/usr/bin/env python
# coding: utf-8

# # Simple chatbot assistance system using python

# In[3]:


import nltk
from nltk.chat.util import Chat, reflections


# In[4]:


print(Chat)


# In[5]:


reflections


# In[13]:


set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["Your can call me a charbot?",]
    ],
    [
        r"how are you?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you",
        ["i am looking for online guides and courses to learn data science, can you suggest?","i am looking for data science training",]
    ],
    [
        r"i'm(.*) doing good",
        ["That's a great to hear", "How can i help you?:)",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Coding Ninjas is a great option to learn data science. You can check their website",]
    ],
    [
        r"thanks for the suggestion. do they have great authors and instructurs?",
        ["Yes, they have the world class best authors, that is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["I am happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    ]


# In[14]:


def chatbot():
    print("Hi I am a rule-based chatbot! What can I help you with?")

chatbot()    


# In[15]:


chat = Chat(set_pairs, reflections)
print(chat)


# In[22]:


chat.converse()
if ___name___== "___main___":
    chatbot()


# # conclusion:

# We can sucessfully made a chatbot it is one of the simple ways to transport data from a computer without having to think for proper keywords to look up in a search or browse several web pages to collect information; users can easily type their query in natural language and retrieve information.
# Chatbots allow businesses to connect with customers in a personal way without the expense of human representatives. For example, many of the questions or issues customers have are common and easily answered. That's why companies create FAQs and troubleshooting guides.
# 

# In[ ]:




