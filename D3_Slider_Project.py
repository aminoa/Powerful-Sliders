from IPython.display import display
import ipywidgets as widgets
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np
from d3graph import d3graph

#This is where we get the original tweet that will start off the entire conversation

original_tweet = input("Hello and welcome to Tweets R' Us, Where we help you craft your perfect responses on Twitter. To start, can you please enter in the Tweet that you want to repond to?\n")
#These are the matricies that will hold all of the data

adj_matrix = pd.DataFrame({
    '0': [0],
}, index=['0'])



tweet = [
    {'tweet': original_tweet, 'connection': 0, 'sentiment': 0, 'og': 'Starting Tweet'},
    
]
df_tweet = pd.DataFrame(tweet)




print("Here is the slider that you can use to choose the sentiment score that you want to include for the response:\n -1 means very negative\n 0 means neutral \n 1 means very positive \n")


# This is the slider that will update the value of the sentiment
def update_graph(val):
    # Retrieve the current value of the slider
    slider_value = slider.val
    
    # Update the global variable graph_value
    global graph_value
    graph_value = slider_value
    
    
    
    # Display a confirmation button
    confirm_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
    confirm_button = Button(confirm_ax, 'Confirm', color='green', hovercolor='lightgreen')
    
    # Define the function to handle the confirmation button click
    def confirm_clicked(event):
        global confirmed
        confirmed = True
    
    # Add an event listener to the confirmation button
    confirm_button.on_clicked(confirm_clicked)
    
    # Wait for the user to confirm their selection
    global confirmed
    confirmed = False
    while not confirmed:
        plt.pause(0.05)



Done = False
past_connection = 0
while Done == False:

    slider_ax = plt.axes([0.1, 0.1, 0.8, 0.03])
    slider = Slider(slider_ax, label="Mood:", valmin=-1, valmax=1, valinit=0, valstep=0.1)

    # Add the event listener to the slider
    slider.on_changed(update_graph)

    # Display the slider and the graph
    plt.show()


    #HERE IS WHERE WE WOULD SEND THE TWEET AND THE SENTIMENT SCORE TO ANEESHES FUN FUN FUN TIME

    new_tweet = "in in in in in in in in in"
    sentiment_score = graph_value

    
    new_tweet_data =  [
    {'tweet': new_tweet, 'connection': past_connection, 'sentiment': sentiment_score, 'og': 'Response'}   
]
    df_tweet = df_tweet.append(new_tweet_data)
    print(df_tweet)
    row = df_tweet.iloc[-1]
    
    
    papa_node = row.connection


    adj_matrix.loc[str(len(df_tweet) - 1)] = 0
    adj_matrix[str(len(df_tweet) - 1)] = 0
    adj_matrix.loc[str(past_connection), str(len(df_tweet) - 1)] = 1

    
    

    d3 = d3graph()

    label = df_tweet['og'].values
   
    tweets = df_tweet['tweet'].values

    
    sent_scores = df_tweet['sentiment'].values
    

    d3.graph(adj_matrix)
    d3.set_edge_properties(edge_distance=1000)
    d3.set_edge_properties(directed=True)

    d3.set_node_properties(color=sent_scores)
    d3.set_node_properties(label=label, color=sent_scores, cmap='coolwarm', tooltip=tweets)
    #d3.set_node_properties(tooltips = label)
    

    
    d3.show()

    stop_the_tweets = input("Are you happy with your Responses?\n Reply Yes if you are done or No if you want to continue creating responses: ")
    if stop_the_tweets == 'Yes':
        Done = True
    else:
        reply = input("Do you want to create a potential reply to this tweet, or try a different reply to the original tweet? \n Type Original if you want to find a reply to the original tweet \n Type New if you want to respond to the tweet that has been generated: ")
        
        if reply == 'Original':
            find_tweet = df_tweet.iloc[0]

            original_tweet = find_tweet.tweet
            past_connection = 0


        else:
            find_tweet = df_tweet.iloc[-1]
            original_tweet = find_tweet.tweet
            past_connection = len(df_tweet) - 1
        

    



