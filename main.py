from analysis import team_analysis
from flask import Flask, request

TeamAnalysis = team_analysis.TeamAnalysis('https://pokepast.es/76c817bcd0f4ff7e', debug=True)
TeamAnalysis.team_format()
TeamAnalysis.defense_analysis()