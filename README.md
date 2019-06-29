# Software development plan

##purpose

The purpose of the How Do You Feel application is to track your mood during the day.

##Scope

####high level

As a <ROLE> I want to <DO> so that <BENEFIT>

As a human, I want to better identify my emotions so I can be more aware of my emotions. 

####Problem

How do you track your emotions as they shift during the day and reflect accurately on how you have felt over time.

####Audience

The audience is anyone interested in better identifying and tracking their emotions.

####How it will be used

When the application starts, a user is asked how they feel. When they identify their emotion from a list, they are presented with a quote that is randomly selected from a list of quotes relevant to that emotion. The emotion is written to an external file in order to be counted.

After reading the quote, the user goes to a secondary menu where they can either track their mood or add a quote. If they track their mood, a cumlative count of the mood inputs is displayed. 

If they add a quote, they select which list they want to append, then are prompted to input a quote that is appended to the relevant list.

#Features

Printing a random quote that reflects the user's mood.

Track your mood with a cumulative counter.

Add a quote to the emotion dictionary - stored as a .json file.

#User Interaction
##Outline
test
The user starts the application, either passing an argument that is their current mood or not. If a valid argument is passed, a relevant quote is printed on the screen. If no argument is passed, a menu is displayed asking for input and displaying the available moods. Once a valid mood has been inputted, a quote is printed on the screen that is randomly selected from the emotion dictionary.

The user then sees a second menu, where they can either track their mood and see what they have selected previously, or add a quote, in which they identify the mood and input the quote to be written to the dictionary.

After that, the user exits the app.

#Control flow diagram

#Implementation plan
Insert from Trello

#Status updates

27/6

- The idea behind the app is wanting a data series that will be able to be presented using hte python package matplotlib. A quick emotion tracking app that is able to be run throughout the day as your mood changes will provide good data pieces that will be of benefit to the user. It will also allow for future iterations to explore timed notifications, data set segmentation along dates and time, and scraping for other quotes to expand the emotion dictionary. Thinking about the flow of the application, I am trying to make it both fit within the scope of my coding ability but also contain the necessary technical components necessary. My thought here is that it is better to start simple and add features than the other way around.

#Help
##How to install
##Dependencies

json

random

matplotlib

##System requirements

#Testing procedure




