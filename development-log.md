# Status updates

## Project start
### 27June
- The idea behind the app is wanting a data series that will be able to be presented using the python package matplotlib. A quick emotion tracking app that is able to be run throughout the day as your mood changes will provide good data pieces that will be of benefit to the user. It will also allow for future iterations to explore timed notifications, data set segmentation along dates and time, and scraping for other quotes to expand the emotion dictionary. Thinking about the flow of the application, I am trying to make it both fit within the scope of my coding ability but also contain the necessary technical components necessary. My thought here is that it is better to start simple and add features than the other way around.

## Pre-testing
### 29June
- The code for the app has been written and is functional. The addition of the argparse allows a user to skip the first menu and streamline the first half of the app. Future features will look at expanding the potential arguments that can be parsed to extend into the second menu. At this stage, I have been committing to git and running the code through pylint to clean up the syntax. The remaining part is creating tests for the various functions. Additionally, I have moved the integration of matplotlib to a future feature to better visualise the counter data.

## Testing
#### 4 July
- Writing the tests today, added integrating emojis into future feature updates on Trello to improve UX. The tests are to check the output of specific functions in the application that are not dependant on user input. A nested loop was identified and fixed inside the funciton add_quote by breaking the loop to return to the second menu. From a UX POV, I moved a print statement to inside the second_menu loop, giving input prompts to remind the user of the available inputs.

- Scripts have been changed to executables and a shell script written that will automatically compile the python script into a binary distribution. Help file has been written to give steps for the available ways of interacting with the script and/or executable. A shell scrpipt has also been written to automate the running of the python script test_HDYF.py. Instructions are under the heading, testing.