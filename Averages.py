import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('League of Legends Post Game Analyzer')

st.header('About')
st.info('Welcome to the tool used to analyze your post game data from finished League of Legends games. There will be a total of 9 major categories that will be rated, which will be scored on a 0 out of 10 ten basis. After entering the information the questions ask for press the contiune button for your in depth analysis.')

def Start():
    # st.sidebar.subheader("login")
    # username = st.sidebar.text_input("Username")
    # button_was_clicked = st.sidebar.button("SUBMIT")

    st.header('Data Entry')
    name = st.text_input('Enter your Summoner Name: ')
    time = st.number_input('Enter the Time of the game (if game was 42:43 enter 424, this is on a 10 cs per minute basis): ')
    timemin = st.number_input('Enter the Time of the game just minutes: ')
    cs = st.number_input('Enter the CS: ')
    totalTeamDamag = st.number_input('Enter the teams total damage: ')
    personalDamag = st.number_input('Enter your total damage: ')
    vision = st.number_input('Enter the vision score: ')
    controlWard = st.number_input('Enter the number of control wards purchased: ')
    totalTeamGold = st.number_input('Enter the total gold earned by your team: ')
    personalGold = st.number_input('Enter your personal total gold: ')
    dragon = st.number_input('Enter the number of dragons your team had: ')
    baron = st.number_input('Enter how many baron buffs your team earned: ')
    rift = st.number_input('Enter how many rift heralds your team earned: ')
    tower = st.number_input('Enter the number of towers destroyed: ')
    inhibs = st.number_input('Enter the number of inhibs destroyed:')
    totalTeamKills = st.number_input('Enter team kill total: ')
    personalKills = st.number_input('Enter the number of kills you had: ')
    totalTeamDeaths = st.number_input('Enter team deaths: ')
    personalDeaths = st.number_input('Enter your death total: ')
    personalAssists = st.number_input('Enter your assist number: ')
    champMastery = st.number_input('Enter your number of mastery points with your champion: ')
    champLevel = st.number_input('Enter your mastery level: ')
    wol = st.text_input('Enter if your team won or lost the game (type win or loss): ')

    if st.button('Confirm'):
        st.header('Indvidual Ratings')
        st.markdown('This is your report for Summoner: ' + name)

        st.markdown('**Creep Score**')
        csrate = cs / time
        if csrate <= 0.1:
            st.latex("0 / 10")
            csscore = 0
        elif csrate > 0.1 and csrate < 0.2:
            st.latex("1 / 10")
            csscore = 0.1
        elif csrate >= 0.2 and csrate < 0.3:
            st.latex("2 / 10")
            csscore = 0.2
        elif csrate >= 0.3 and csrate < 0.4:
            st.latex("3 / 10")
            csscore = 0.3
        elif csrate >= 0.4 and csrate < 0.5:
            st.latex("4 / 10")
            csscore = 0.4
        elif csrate >= 0.5 and csrate < 0.6:
            st.latex("5 / 10")
            csscore = 0.5
        elif csrate >= 0.6 and csrate < 0.7:
            st.latex("6 / 10")
            csscore = 0.6
        elif csrate >= 0.7 and csrate < 0.8:
            st.latex("7 / 10")
            csscore = 0.7
        elif csrate >= 0.8 and csrate < 0.9:
            st.latex("8 / 10")
            csscore = 0.8
        elif csrate >= 0.9 and csrate < 1.0:
            st.latex("9 / 10")
            csscore = 0.9
        elif csrate >= 1.0:
            st.latex("10 / 10")
            csscore = 1.0

        csbar = st.progress(0)
        csbar.progress(csscore)

        st.markdown('**Damage**')
        fighting = personalDamag / totalTeamDamag
        if fighting <= 0.1:
            st.latex("0 / 10")
            scorefighting = 0
        elif fighting > 0.1 and fighting <= 0.125:
            st.latex("1 / 10")
            scorefighting = 0.1
        elif fighting > 0.125 and fighting <= 0.15:
            st.latex("2 / 10")
            scorefighting = 0.2
        elif fighting > 0.15 and fighting <= 0.175:
            st.latex("3 / 10")
            scorefighting = 0.3
        elif fighting > 0.175 and fighting <= 0.2:
            st.latex("4 / 10")
            scorefighting = 0.4
        elif fighting > 0.2 and fighting <= 0.21:
            st.latex("5 / 10")
            scorefighting = 0.5
        elif fighting > 0.21 and fighting <= 0.22:
            st.latex("6 / 10")
            scorefighting = 0.6
        elif fighting > 0.22 and fighting <= 0.23:
            st.latex("7 / 10")
            scorefighting = 0.7
        elif fighting > 0.23 and fighting <= 0.24:
            st.latex("8 / 10")
            scorefighting = 0.8
        elif fighting > 0.24 and fighting <= 0.25:
            st.latex("9 / 10")
            scorefighting = 0.9
        elif fighting > 0.25:
            st.latex("10 / 10")
            scorefighting = 1.0

        damagebar = st.progress(0)
        damagebar.progress(scorefighting)

        st.markdown('**Vision Score**')
        sight = vision / timemin
        if sight <= 0.3:
            st.latex("0 / 10")
            visionscore = 0.1
        elif sight <= 0.4:
            st.latex("1 / 10")
            visionscore = 0.2
        elif sight <= 0.5:
            st.latex("2 / 10")
            visionscore = 0.2
        elif sight <= 0.6:
            st.latex("3 / 10")
            visionscore = 0.3
        elif sight <= 0.7:
            st.latex("4 / 10")
            visionscore = 0.4
        elif sight <= 0.8:
            st.latex("5 / 10")
            visionscore = 0.5
        elif sight <= 0.9:
            st.latex("6 / 10")
            visionscore = 0.6
        elif sight <= 1.05:
            st.latex("7 / 10")
            visionscore = 0.7
        elif sight <= 1.2:
            st.latex("8 / 10")
            visionscore = 0.8
        elif sight <= 1.35:
            st.latex("9 / 10")
            visionscore = 0.9
        elif sight > 1.45:
            st.latex("10 / 10")
            visionscore = 1.0

        visionbar = st.progress(0)
        visionbar.progress(visionscore)

        st.markdown('**Income**')
        income = personalGold / totalTeamGold
        if income <= 0.1:
            st.latex("0 / 10")
            incomescore = 0
        elif income > 0.1 and income <= 0.125:
            st.latex("1 / 10")
            incomescore = 0.1
        elif income > 0.125 and income <= 0.15:
            st.latex("2 / 10")
            incomescore = 0.2
        elif income > 0.15 and income <= 0.175:
            st.latex("3 / 10")
            incomescore = 0.3
        elif income > 0.175 and income <= 0.2:
            st.latex("4 / 10")
            incomescore = 0.4
        elif income > 0.2 and income <= 0.21:
            st.latex("5 / 10")
            incomescore = 0.5
        elif income > 0.21 and income <= 0.22:
            st.latex("6 / 10")
            incomescore = 0.6
        elif income > 0.22 and income <= 0.23:
            st.latex("7 / 10")
            incomescore = 0.7
        elif income > 0.23 and income <= 0.24:
            st.latex("8 / 10")
            incomescore = 0.8
        elif income > 0.24 and income <= 0.25:
            st.latex("9 / 10")
            incomescore = 0.9
        elif income > 0.25:
            st.latex("10 / 10")
            incomescore = 1.0

        incomebar = st.progress(0)
        incomebar.progress(incomescore)

        st.markdown('**Objectives**')
        if timemin <= 60 and dragon == 0 and baron == 0 and rift == 0:
            st.latex("0 / 10")
            objscore = 0
        elif timemin < 10 and dragon == 1 and rift == 1:
            st.latex("10 / 10")
            objscore = 1.0
        elif timemin < 10 and dragon == 0 and rift == 1:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 10 and dragon == 1 and rift == 0:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 15 and dragon == 2 and rift == 1:
            st.latex("10 / 10")
            objscore = 1.0
        elif timemin < 15 and dragon == 1 and rift == 1:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 15 and dragon == 0 and rift == 1:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 15 and dragon == 2 and rift == 0:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 15 and dragon == 1 and rift == 0:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 20 and dragon == 3 and rift == 2:
            st.latex("10 / 10")
            objscore = 1.0
        elif timemin < 20 and dragon == 2 and rift == 2:
            st.latex("8 / 10")
            objscore = 0.8
        elif timemin < 20 and dragon == 1 and rift == 2:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 20 and dragon == 0 and rift == 2:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 20 and dragon == 3 and rift == 1:
            st.latex("8 / 10")
            objscore = 0.8
        elif timemin < 20 and dragon == 2 and rift == 1:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 20 and dragon == 1 and rift == 1:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 20 and dragon == 0 and rift == 1:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 20 and dragon == 3 and rift == 0:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 20 and dragon == 2 and rift == 0:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 20 and dragon == 1 and rift == 0:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 25 and dragon == 4 and rift == 2 and baron == 1:
            st.latex("10 / 10")
            objscore = 1.0
        elif timemin < 25 and dragon == 3 and rift == 2 and baron == 1:
            st.latex("8 / 10")
            objscore = 0.8
        elif timemin < 25 and dragon == 2 and rift == 2 and baron == 1:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 25 and dragon == 1 and rift == 2 and baron == 1:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 25 and dragon == 0 and rift == 2 and baron == 1:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 25 and dragon == 4 and rift == 1 and baron == 1:
            st.latex("8 / 10")
            objscore = 0.8
        elif timemin < 25 and dragon == 3 and rift == 1 and baron == 1:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 25 and dragon == 2 and rift == 1 and baron == 1:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 25 and dragon == 1 and rift == 1 and baron == 1:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 25 and dragon == 0 and rift == 1 and baron == 1:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 25 and dragon == 4 and rift == 0 and baron == 1:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 25 and dragon == 3 and rift == 0 and baron == 1:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 25 and dragon == 2 and rift == 0 and baron == 1:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 25 and dragon == 1 and rift == 0 and baron == 1:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 25 and dragon == 0 and rift == 0 and baron == 1:
            st.latex("1 / 10")
            objscore = 0.1
        elif timemin < 25 and dragon == 4 and rift == 2 and baron == 0:
            st.latex("8 / 10")
            objscore = 0.8
        elif timemin < 25 and dragon == 3 and rift == 2 and baron == 0:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 25 and dragon == 2 and rift == 2 and baron == 0:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 25 and dragon == 1 and rift == 2 and baron == 0:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 25 and dragon == 0 and rift == 2 and baron == 0:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 25 and dragon == 4 and rift == 1 and baron == 0:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 25 and dragon == 3 and rift == 1 and baron == 0:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 25 and dragon == 2 and rift == 1 and baron == 0:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 25 and dragon == 1 and rift == 1 and baron == 0:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 25 and dragon == 0 and rift == 1 and baron == 0:
            st.latex("1 / 10")
            objscore = 0.1
        elif timemin < 25 and dragon == 4 and rift == 0 and baron == 0:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 25 and dragon == 3 and rift == 0 and baron == 0:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 25 and dragon == 2 and rift == 0 and baron == 0:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 25 and dragon == 1 and rift == 0 and baron == 0:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 25 and dragon == 0 and rift == 0 and baron == 0:
            st.latex("0 / 10")
            objscore = 0.0
        elif timemin < 35 and dragon == 5 and rift == 2 and baron == 1:
            st.latex("10 / 10")
            objscore = 1.0
        elif timemin < 35 and dragon == 4 and rift == 2 and baron == 1:
            st.latex("9 / 10")
            objscore = 0.9
        elif timemin < 35 and dragon == 3 and rift == 2 and baron == 1:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 35 and dragon == 2 and rift == 2 and baron == 1:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 35 and dragon == 1 and rift == 2 and baron == 1:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 35 and dragon == 0 and rift == 2 and baron == 1:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 35 and dragon == 5 and rift == 1 and baron == 1:
            st.latex("9 / 10")
            objscore = 0.9
        elif timemin < 35 and dragon == 4 and rift == 1 and baron == 1:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 35 and dragon == 3 and rift == 1 and baron == 1:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 35 and dragon == 2 and rift == 1 and baron == 1:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 35 and dragon == 1 and rift == 1 and baron == 1:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 35 and dragon == 0 and rift == 1 and baron == 1:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 35 and dragon == 5 and rift == 0 and baron == 1:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 35 and dragon == 4 and rift == 0 and baron == 1:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 35 and dragon == 3 and rift == 0 and baron == 1:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 35 and dragon == 2 and rift == 0 and baron == 1:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 35 and dragon == 1 and rift == 0 and baron == 1:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 35 and dragon == 0 and rift == 0 and baron == 1:
            st.latex("1 / 10")
            objscore = 0.1
        elif timemin < 35 and dragon == 5 and rift == 2 and baron == 0:
            st.latex("9 / 10")
            objscore = 0.9
        elif timemin < 35 and dragon == 4 and rift == 2 and baron == 0:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 35 and dragon == 3 and rift == 2 and baron == 0:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 35 and dragon == 2 and rift == 2 and baron == 0:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 35 and dragon == 1 and rift == 2 and baron == 0:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 35 and dragon == 0 and rift == 2 and baron == 0:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 35 and dragon == 5 and rift == 1 and baron == 0:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 35 and dragon == 4 and rift == 1 and baron == 0:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 35 and dragon == 3 and rift == 1 and baron == 0:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 35 and dragon == 2 and rift == 1 and baron == 0:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 35 and dragon == 1 and rift == 1 and baron == 0:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 35 and dragon == 0 and rift == 1 and baron == 0:
            st.latex("1 / 10")
            objscore = 0.1
        elif timemin < 35 and dragon == 5 and rift == 0 and baron == 0:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 35 and dragon == 4 and rift == 0 and baron == 0:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 35 and dragon == 3 and rift == 0 and baron == 0:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 35 and dragon == 2 and rift == 0 and baron == 0:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 35 and dragon == 1 and rift == 0 and baron == 0:
            st.latex("1 / 10")
            objscore = 0.1
        elif timemin < 35 and dragon == 0 and rift == 0 and baron == 0:
            st.latex("0 / 10")
            objscore = 0
        elif timemin < 50 and dragon == 7 and baron == 3:
            st.latex("10 / 10")
            objscore = 1.0
        elif timemin < 50 and dragon == 6 and baron == 3:
            st.latex("9 / 10")
            objscore = 0.9
        elif timemin < 50 and dragon == 5 and baron == 3:
            st.latex("8 / 10")
            objscore = 0.8
        elif timemin < 50 and dragon == 4 and baron == 3:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 50 and dragon == 3 and baron == 3:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 50 and dragon == 2 and baron == 3:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 50 and dragon == 1 and baron == 3:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 50 and dragon == 0 and baron == 3:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 50 and dragon == 7 and baron == 2:
            st.latex("9 / 10")
            objscore = 0.9
        elif timemin < 50 and dragon == 6 and baron == 2:
            st.latex("8 / 10")
            objscore = 0.8
        elif timemin < 50 and dragon == 5 and baron == 2:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 50 and dragon == 4 and baron == 2:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 50 and dragon == 3 and baron == 2:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 50 and dragon == 2 and baron == 2:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 50 and dragon == 1 and baron == 2:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 50 and dragon == 0 and baron == 2:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 50 and dragon == 7 and baron == 1:
            st.latex("8 / 10")
            objscore = 0.8
        elif timemin < 50 and dragon == 6 and baron == 1:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 50 and dragon == 5 and baron == 1:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 50 and dragon == 4 and baron == 1:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 50 and dragon == 3 and baron == 1:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 50 and dragon == 2 and baron == 1:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 50 and dragon == 1 and baron == 1:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 50 and dragon == 0 and baron == 1:
            st.latex("1 / 10")
            objscore = 0.1
        elif timemin < 50 and dragon == 7 and baron == 0:
            st.latex("7 / 10")
            objscore = 0.7
        elif timemin < 50 and dragon == 6 and baron == 0:
            st.latex("6 / 10")
            objscore = 0.6
        elif timemin < 50 and dragon == 5 and baron == 0:
            st.latex("5 / 10")
            objscore = 0.5
        elif timemin < 50 and dragon == 4 and baron == 0:
            st.latex("4 / 10")
            objscore = 0.4
        elif timemin < 50 and dragon == 3 and baron == 0:
            st.latex("3 / 10")
            objscore = 0.3
        elif timemin < 50 and dragon == 2 and baron == 0:
            st.latex("2 / 10")
            objscore = 0.2
        elif timemin < 50 and dragon == 1 and baron == 0:
            st.latex("1 / 10")
            objscore = 0.1
        elif timemin < 50 and dragon == 0 and baron == 0:
            st.latex("0 / 10")
            objscore = 0

        objbar = st.progress(0)
        objbar.progress(objscore)

        st.markdown('**Map Pressure**')
        if tower == 0 and inhibs == 0:
            st.latex("0 / 10")
            mapscore = 0
        elif tower == 1 and inhibs <= 0:
            st.latex("0 / 10")
            mapscore = 0
        elif tower == 2 and inhibs <= 0:
            st.latex("1 / 10")
            mapscore = 0.1
        elif tower == 3 and inhibs <= 0:
            st.latex("2 / 10")
            mapscore = 0.2
        elif tower == 4 and inhibs <= 0:
            st.latex("3 / 10")
            mapscore = 0.3
        elif tower == 5 and inhibs <= 0:
            st.latex("4 / 10")
            mapscore = 0.4
        elif tower == 6 and inhibs <= 0:
            st.latex("5 / 10")
            mapscore = 0.5
        elif tower == 7 and inhibs <= 0:
            st.latex("6 / 10")
            mapscore = 0.6
        elif tower == 8 and inhibs <= 0:
            st.latex("6 / 10")
            mapscore = 0.6
        elif tower == 9 and inhibs <= 0:
            st.latex("7 / 10")
            mapscore = 0.7
        elif tower == 3 and inhibs >= 1:
            st.latex("3 / 10")
            mapscore = 0.3
        elif tower == 4 and inhibs >= 1:
            st.latex("4 / 10")
            mapscore = 0.4
        elif tower == 5 and inhibs >= 1:
            st.latex("5 / 10")
            mapscore = 0.5
        elif tower == 6 and inhibs >= 1:
            st.latex("6 / 10")
            mapscore = 0.6
        elif tower == 7 and inhibs >= 1:
            st.latex("6 / 10")
            mapscore = 0.6
        elif tower == 8 and inhibs >= 1:
            st.latex("7 / 10")
            mapscore = 0.7
        elif tower == 9 and inhibs >= 1:
            st.latex("8 / 10")
            mapscore = 0.8
        elif tower == 10 and inhibs >= 1:
            st.latex("10 / 10")
            mapscore = 1.0
        elif tower == 11 and inhibs >= 1:
            st.latex("10 / 10")
            mapscore = 1.0

        mapbar = st.progress(0)
        mapbar.progress(mapscore)

        st.markdown('**Survival and Fighting**')
        slayer = personalKills / totalTeamKills
        dying = personalDeaths / totalTeamDeaths
        helper = (personalKills + personalAssists) / totalTeamKills
        if slayer <= 0.1:
            slayscore = 0
        elif slayer > 0.1 and slayer <= 0.125:
            slayscore = 0.1
        elif slayer > 0.125 and slayer <= 0.15:
            slayscore = 0.2
        elif slayer > 0.15 and slayer <= 0.175:
            slayscore = 0.3
        elif slayer > 0.175 and slayer <= 0.2:
            slayscore = 0.4
        elif slayer > 0.2 and slayer <= 0.21:
            slayscore = 0.5
        elif slayer > 0.21 and slayer <= 0.22:
            slayscore = 0.6
        elif slayer > 0.22 and slayer <= 0.23:
            slayscore = 0.7
        elif slayer > 0.23 and slayer <= 0.24:
            slayscore = 0.8
        elif slayer > 0.24 and slayer <= 0.25:
            slayscore = 0.9
        elif slayer > 0.25:
            slayscore = 1.0

        if dying <= 0.1:
            dyingscore = 1.0
        elif dying > 0.1 and dying <= 0.12:
            dyingscore = 0.9
        elif dying > 0.12 and dying <= 0.13:
            dyingscore = 0.8
        elif dying > 0.13 and dying <= 0.14:
            dyingscore = 0.7
        elif dying > 0.14 and dying <= 0.15:
            dyingscore = 0.6
        elif dying > 0.15 and dying <= 0.16:
            dyingscore = 0.5
        elif dying > 0.16 and dying <= 0.17:
            dyingscore = 0.4
        elif dying > 0.17 and dying <= 0.18:
            dyingscore = 0.3
        elif dying > 0.18 and dying <= 0.19:
            dyingscore = 0.2
        elif dying > 0.19 and dying <= 0.20:
            dyingscore = 0.1
        elif dying > 0.20:
            dyingscore = 0

        if helper > 0 and helper <= 0.5:
            helperscore = 0
        elif helper > 0.5 and helper <= 0.1:
            helperscore = 0.1
        elif helper > 0.1 and helper <= 0.15:
            helperscore = 0.2
        elif helper > 0.15 and helper <= 0.2:
            helperscore = 0.3
        elif helper > 0.2 and helper <= 0.25:
            helperscore = 0.4
        elif helper > 0.25 and helper <= 0.3:
            helperscore = 0.5
        elif helper > 0.3 and helper <= 0.35:
            helperscore = 0.6
        elif helper > 0.35 and helper <= 0.4:
            helperscore = 0.7
        elif helper > 0.4 and helper <= 0.45:
            helperscore = 0.8
        elif helper > 0.45 and helper <= 0.5:
            helperscore = 0.9
        elif helper > 0.5:
            helperscore = 1.0

        brawlscore = (slayscore + dyingscore + helperscore) / 3
        if brawlscore >= 0 and brawlscore < 0.1:
            st.latex("0 / 10")
        elif brawlscore >= 0.1 and brawlscore < 0.2:
            st.latex("1 / 10")
        elif brawlscore >= 0.2 and brawlscore < 0.3:
            st.latex("2 / 10")
        elif brawlscore >= 0.3 and brawlscore < 0.4:
            st.latex("3 / 10")
        elif brawlscore >= 0.4 and brawlscore < 0.5:
            st.latex("4 / 10")
        elif brawlscore >= 0.5 and brawlscore < 0.6:
            st.latex("5 / 10")
        elif brawlscore >= 0.6 and brawlscore < 0.7:
            st.latex("6 / 10")
        elif brawlscore >= 0.7 and brawlscore < 0.8:
            st.latex("7 / 10")
        elif brawlscore >= 0.8 and brawlscore < 0.9:
            st.latex("8 / 10")
        elif brawlscore >= 0.9 and brawlscore < 1.0:
            st.latex("9 / 10")
        elif brawlscore >= 1.0:
            st.latex("10 / 10")

        brawlbar = st.progress(0)
        brawlbar.progress(brawlscore)

        st.markdown('**Champion Mastery**')
        if champMastery <= 1800 and champLevel == 1:
            st.latex("1 / 10")
            champscore = 0.1
        elif champMastery > 1800 and champMastery <= 6000 and champLevel == 2:
            st.latex("2 / 10")
            champscore = 0.2
        elif champMastery > 6000 and champMastery <= 12600 and champLevel == 3:
            st.latex("4 / 10")
            champscore = 0.4
        elif champMastery > 12600 and champMastery <= 21600 and champLevel == 4:
            st.latex("5 / 10")
            champscore = 0.5
        elif champMastery > 21600 and champLevel == 5:
            st.latex("6 / 10")
            champscore = 0.6
        elif champMastery > 21600 and champMastery <= 32000 and champLevel == 6:
            st.latex("7 / 10")
            champscore = 0.7
        elif champMastery > 32000 and champLevel == 6:
            st.latex("8 / 10")
            champscore = 0.8
        elif champMastery > 21600 and champMastery <= 40000 and champlevel == 7:
            st.latex("9 / 10")
            champscore = 0.9
        elif champMastery > 40000 and champLevel == 7:
            st.latex("10 / 10")
            champscore = 1.0

        champbar = st.progress(0)
        champbar.progress(champscore)

        st.markdown('**W/L**')
        if wol == 'win':
            st.latex("10 / 10")
            wolscore = 1.0
        elif wol == 'loss':
            st.latex("6 / 10")
            wolscore = 0.6

        wolbar = st.progress(0)
        wolbar.progress(wolscore)

        st.header('**Overall Skill**')
        ovr = (csrate + scorefighting + visionscore + incomescore + objscore + mapscore + slayscore + dyingscore + helperscore + champscore + wolscore) / 11
        if ovr > 0 and ovr < 0.10:
            st.latex("0 / 10")
        elif ovr >= 0.10 and ovr < 0.20:
            st.latex("1 / 10")
        elif ovr >= 0.20 and ovr < 0.30:
            st.latex("2 / 10")
        elif ovr >= 0.30 and ovr < 0.40:
            st.latex("3 / 10")
        elif ovr >= 0.40 and ovr < 0.50:
            st.latex("4 / 10")
        elif ovr >= 0.50 and ovr < 0.60:
            st.latex("5 / 10")
        elif ovr >= 0.60 and ovr < 0.70:
            st.latex("6 / 10")
        elif ovr >= 0.70 and ovr < 0.80:
            st.latex("7 / 10")
        elif ovr >= 0.80 and ovr < 0.90:
            st.latex("8 / 10")
        elif ovr >= 0.90 and ovr < 1.00:
            st.latex("9 / 10")
        elif ovr >= 1.00:
            st.latex("10 / 10")

        st.header('**Improvement Opportunities**')
        if csrate <= scorefighting and csrate <= visionscore and csrate <= incomescore and csrate <= objscore and csrate <= mapscore and csrate <= brawlscore and csrate <= champscore:
            st.info('Your cs ability is your lowest category in order to improve it is recommended to go into the practice tool for the first 10 minutes and practice cs and get used to your auto attacks. Also try to save your auto attacks for when the minons health is low enough you know you will kill it instantly. Lastly it is recommended that you play the champion more and get used to it since every champion is not the same.')
        elif scorefighting <= csrate and scorefighting <= visionscore and scorefighting <= incomescore and scorefighting <= objscore and scorefighting <= mapscore and scorefighting <= brawlscore and scorefighting <= champscore:
            st.info('Your damage percentage is your lowest category in order to improve in this category it is recommended to try to trade in lane whenever you can have a winning trade. To do this you should check if your opposition has used import spell cooldowns that take a while or recharge. These will change the way a fight goes and dratically help your team win.')
        elif visionscore <= csrate and visionscore <= scorefighting and visionscore <= incomescore and visionscore <= objscore and visionscore <= mapscore and visionscore <= brawlscore and visionscore <= champscore:
            st.info('Your vision score is your lowest category in order to improve on this try placing more wards deeper into the enemy jungle where you can find the jungler and see what he is doing and where he is going. Also another way to improve your vision is to buy more control wards which will give you permanent vision until they are destroyed. The final way to improve is to put wards in spots people will not think to get rid of them and you can get the full value for them.')
        elif incomescore <= csrate and incomescore <= scorefighting and incomescore <= visionscore and incomescore <= objscore and incomescore <= mapscore and incomescore <= brawlscore and incomescore <= champscore:
            st.info('Your income and income percentage is your lowest category in order to improve on this you can do a few things. One important thing is the most money you get will be from csing so it is important to make sure you can collect as much of those as you can. The next thing to focus on is getting kills and assists. In League kills = 300 gold so it is important to get as many as you can during the game so you can get stronger. Then finally get as many objectives, towers and jungle camps to increase the ammount of gold you have. Remember the more gold you have the more items you can buy which make you do more damage.')
        elif objscore <= csrate and objscore <= scorefighting and objscore <= visionscore and objscore <= incomescore and objscore <= mapscore and objscore <= brawlscore and objscore <= champscore:
            st.info('Your objectives seem to be the lowest category in order to improve on this one thing that is recommended is having an open communication with your jungler or your laners. Having a good communication will allow you to be able to take more objectives and get advantages for your team. Make sure you are keeping track of cooldowns for dragons and objectives so you can set yourself in a way you wont be missing expierence for doing an objective.')
        elif mapscore <= csrate and mapscore <= scorefighting and mapscore <= visionscore and mapscore <= incomescore and mapscore <= objscore and mapscore <= brawlscore and mapscore <= champscore:
            st.info('Your map pressure is your lowest category, this is a pretty straightforward category which focus on how many towers and inhibs you have taken. In order to increase this ammount try to get as many towers as possible because towers destroyed means more team gold. Another import part to improve on this category is making sure that if you get your tower destroyed move to another lane to help them get the tower and play as a team.')
        elif brawlscore <= csrate and brawlscore <= scorefighting and brawlscore <= visionscore and brawlscore <= incomescore and brawlscore <= objscore and brawlscore <= mapscore and brawlscore <= champscore:
            st.info('Your ability to survive, kill, and help your team get kills is your lowest category. In order to improve in this category you can do a few things which are get more kills for yourself, die less often, and help make plays happen more often. The more kills you get the less time your enemy spends alive csing and getting xp. Dying less will make sure you dont give away free 300 gold and help them get a lead. Then finally the more kills you help in setting up the more gold your team has over them which can make you have item advantages.')
        elif champscore <= csrate and champscore <= scorefighting and champscore <= visionscore and champscore <= incomescore and champscore <= objscore and champscore <= mapscore and champscore <= brawlscore:
            st.info('Your champion mastery is your lowest category in order to improve on this it is recommended that you play your champion more. The more you play your champion the more you learn how to use them properly then the more your comfortability goes up and you know your power spikes and when you can do damage. A good way to improve is to limit test and put yourself in situations where you have to perform perfectly in order to win. But the overall way to improve is to just get more familiar with your champion and how they work. As they say practice makes perfect.')

        # arr = np.random.normal(10, 10, size=8)
        # plt.hist(arr, bins=5)
        # plt.xlabel('Categories (in order)')
        # plt.ylabel('Rating')
        # plt.grid(True)
        # st.pyplot()


if __name__ == "__main__":
    Start()
