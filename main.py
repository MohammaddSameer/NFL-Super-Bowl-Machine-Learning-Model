import pandas as pd
import numpy as np


csv_folder = "NFLData/"

# Offense Stats
NFL2024OFF = pd.read_csv('NFLData/NFL2024OFF.csv')
NFL2024OFF['Year'] = '2024'

NFL2023OFF = pd.read_csv('NFLData/NFL2023OFF.csv')
NFL2023OFF['Year'] = '2023'

NFL2022OFF = pd.read_csv('NFLData/NFL2022OFF.csv')
NFL2022OFF['Year'] = '2022'

NFL2021OFF = pd.read_csv('NFLData/NFL2021OFF.csv')
NFL2021OFF['Year'] = '2021'

NFL2020OFF = pd.read_csv('NFLData/NFL2020OFF.csv')
NFL2020OFF['Year'] = '2020'

NFL2019OFF = pd.read_csv('NFLData/NFL2019OFF.csv')
NFL2019OFF['Year'] = '2019'

NFL2018OFF = pd.read_csv('NFLData/NFL2018OFF.csv')
NFL2018OFF['Year'] = '2018'

NFL2017OFF = pd.read_csv('NFLData/NFL2017OFF.csv')
NFL2017OFF['Year'] = '2017'

NFL2016OFF = pd.read_csv('NFLData/NFL2016OFF.csv')
NFL2016OFF['Year'] = '2016'

NFL2015OFF = pd.read_csv('NFLData/NFL2015OFF.csv')
NFL2015OFF['Year'] = '2015'

NFL2014OFF = pd.read_csv('NFLData/NFL2014OFF.csv')
NFL2014OFF['Year'] = '2014'

NFL2013OFF = pd.read_csv('NFLData/NFL2013OFF.csv')
NFL2013OFF['Year'] = '2013'

NFL2012OFF = pd.read_csv('NFLData/NFL2012OFF.csv')
NFL2012OFF['Year'] = '2012'

NFL2011OFF = pd.read_csv('NFLData/NFL2011OFF.csv')
NFL2011OFF['Year'] = '2011'

NFL2010OFF = pd.read_csv('NFLData/NFL2010OFF.csv')
NFL2010OFF['Year'] = '2010'

NFL2009OFF = pd.read_csv('NFLData/NFL2009OFF.csv')
NFL2009OFF['Year'] = '2009'

NFL2008OFF = pd.read_csv('NFLData/NFL2008OFF.csv')
NFL2008OFF['Year'] = '2008'

NFL2007OFF = pd.read_csv('NFLData/NFL2007OFF.csv')
NFL2007OFF['Year'] = '2007'

NFL2006OFF = pd.read_csv('NFLData/NFL2006OFF.csv')
NFL2006OFF['Year'] = '2006'

NFL2005OFF = pd.read_csv('NFLData/NFL2005OFF.csv')
NFL2005OFF['Year'] = '2005'

NFL2004OFF = pd.read_csv('NFLData/NFL2004OFF.csv')
NFL2004OFF['Year'] = '2004'

NFL2003OFF = pd.read_csv('NFLData/NFL2003OFF.csv')
NFL2003OFF['Year'] = '2003'

NFL2002OFF = pd.read_csv('NFLData/NFL2002OFF.csv')
NFL2002OFF['Year'] = '2002'

NFL2001OFF = pd.read_csv('NFLData/NFL2001OFF.csv')
NFL2001OFF['Year'] = '2001'

NFL2000OFF = pd.read_csv('NFLData/NFL2000OFF.csv')
NFL2000OFF['Year'] = '2000'



data_frames_off = [NFL2024OFF[1:33], NFL2023OFF[1:33],NFL2020OFF[1:33],NFL2019OFF[1:33], NFL2018OFF[1:33], NFL2017OFF[1:33], NFL2016OFF[1:33], NFL2015OFF[1:33], NFL2014OFF[1:33], NFL2013OFF[1:33], NFL2012OFF[1:33],
              NFL2011OFF[1:33], NFL2010OFF[1:33], NFL2009OFF[1:33], NFL2008OFF[1:33], NFL2007OFF[1:33], NFL2006OFF[1:33], NFL2005OFF[1:33],
              NFL2004OFF[1:33], NFL2003OFF[1:33], NFL2002OFF[1:33], NFL2001OFF[1:32], NFL2000OFF[1:32]]
O_total = pd.concat(data_frames_off)

O_total.columns = ['O_Rank', 'Team', 'O_Games_Played', 'O_Points_For', 'O_Total_Yards',
       'O_Plays', 'O_Y/Play', 'O_TO', 'O_Fumbles_Lost',
       'O_1st_D', 'O_P_Completions', 'O_P_Attempts', 'O_P_Yards', 'O_P_TD',
       'O_P_Int', 'O_P_Y/PA', 'O_P_Passing_1st_D', 'O_R_Att', 'O_R_Yards',
       'O_R_TD', 'O_R_Y/A', 'O_R_1st_D', 'O_Pe', 'O_Pe_Yards',
       'O_Pe_1st_D', 'O_Scoring_Drives', 'O_TO_%', 'O_Expected_Points', 'Year']

O_total['Year'] = O_total['Year'].astype('int')



# Defense Stats
NFL2024DEF = pd.read_csv('NFLData/NFL2024DEF.csv')
NFL2024DEF['Year'] = '2024'

NFL2023DEF = pd.read_csv('NFLData/NFL2023DEF.csv')
NFL2023DEF['Year'] = '2023'

NFL2022DEF = pd.read_csv('NFLData/NFL2022DEF.csv')
NFL2022DEF['Year'] = '2022'

NFL2021DEF = pd.read_csv('NFLData/NFL2021DEF.csv')
NFL2021DEF['Year'] = '2021'

NFL2020DEF = pd.read_csv('NFLData/NFL2020DEF.csv')
NFL2020DEF['Year'] = '2020'

NFL2019DEF = pd.read_csv('NFLData/NFL2019DEF.csv')
NFL2019DEF['Year'] = '2019'

NFL2018DEF = pd.read_csv('NFLData/NFL2018DEF.csv')
NFL2018DEF['Year'] = '2018'

NFL2017DEF = pd.read_csv('NFLData/NFL2017DEF.csv')
NFL2017DEF['Year'] = '2017'

NFL2016DEF = pd.read_csv('NFLData/NFL2016DEF.csv')
NFL2016DEF['Year'] = '2016'

NFL2015DEF = pd.read_csv('NFLData/NFL2015DEF.csv')
NFL2015DEF['Year'] = '2015'

NFL2014DEF = pd.read_csv('NFLData/NFL2014DEF.csv')
NFL2014DEF['Year'] = '2014'

NFL2013DEF = pd.read_csv('NFLData/NFL2013DEF.csv')
NFL2013DEF['Year'] = '2013'

NFL2012DEF = pd.read_csv('NFLData/NFL2012DEF.csv')
NFL2012DEF['Year'] = '2012'

NFL2011DEF = pd.read_csv('NFLData/NFL2011DEF.csv')
NFL2011DEF['Year'] = '2011'

NFL2010DEF = pd.read_csv('NFLData/NFL2010DEF.csv')
NFL2010DEF['Year'] = '2010'

NFL2009DEF = pd.read_csv('NFLData/NFL2009DEF.csv')
NFL2009DEF['Year'] = '2009'

NFL2008DEF = pd.read_csv('NFLData/NFL2008DEF.csv')
NFL2008DEF['Year'] = '2008'

NFL2007DEF = pd.read_csv('NFLData/NFL2007DEF.csv')
NFL2007DEF['Year'] = '2007'

NFL2006DEF = pd.read_csv('NFLData/NFL2006DEF.csv')
NFL2006DEF['Year'] = '2006'

NFL2005DEF = pd.read_csv('NFLData/NFL2005DEF.csv')
NFL2005DEF['Year'] = '2005'

NFL2004DEF = pd.read_csv('NFLData/NFL2004DEF.csv')
NFL2004DEF['Year'] = '2004'

NFL2003DEF = pd.read_csv('NFLData/NFL2003DEF.csv')
NFL2003DEF['Year'] = '2003'

NFL2002DEF = pd.read_csv('NFLData/NFL2002DEF.csv')
NFL2002DEF['Year'] = '2002'

NFL2001DEF = pd.read_csv('NFLData/NFL2001DEF.csv')
NFL2001DEF['Year'] = '2001'

NFL2000DEF = pd.read_csv('NFLData/NFL2000DEF.csv')
NFL2000DEF['Year'] = '2000'


data_frames_def = [NFL2024DEF[1:33], NFL2023DEF[1:33],NFL2020DEF[1:33],NFL2019DEF[1:33], NFL2018DEF[1:33], NFL2017DEF[1:33], NFL2016DEF[1:33], NFL2015DEF[1:33], NFL2014DEF[1:33], NFL2013DEF[1:33], NFL2012DEF[1:33],
              NFL2011DEF[1:33], NFL2010DEF[1:33], NFL2009DEF[1:33], NFL2008DEF[1:33], NFL2007DEF[1:33], NFL2006DEF[1:33], NFL2005DEF[1:33],
              NFL2004DEF[1:33], NFL2003DEF[1:33], NFL2002DEF[1:33], NFL2001DEF[1:32], NFL2000DEF[1:32]]

D_total = pd.concat(data_frames_def)


D_total.columns = ['D_Rank', 'Team', 'D_Games_Played', 'D_Points_Allowed', 'D_Total_Yards',
       'D_Plays', 'D_Y/Play', 'D_TD', 'D_Fumbles_Lost',
       'D_1st_D', 'D_P_Completions', 'D_P_Attempts', 'D_P_Yards', 'D_P_TD',
       'D_P_Int', 'D_P_Y/PA', 'D_P_Passing_1st_D', 'D_R_Att', 'D_R_Yards',
       'D_R_TD', 'D_R_Y/A', 'D_R_1st_D', 'D_Pe', 'D_Pe_Yards',
       'D_Pe_1st_D', 'D_Scoring_Drives', 'D_TD_%', 'D_Expected_Points', 'Year']

D_total['Year'] = O_total['Year'].astype('int')

print(D_total)