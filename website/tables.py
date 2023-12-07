from flask_table import Table, Col
from sqlalchemy import text
from .queries import query_driver_standings, query_constructor_standings
from . import db

class DriverStandings(Table):
    classes = ['w-full', 'text-center']
    rank = Col('Rank', column_html_attrs={'class': 'py-2'})
    driver = Col('Driver', column_html_attrs={'class': 'text-left py-2'})
    points = Col('Points', column_html_attrs={'class': 'py-2'})
    wins = Col('Wins', column_html_attrs={'class': 'py-2'})
    podiums = Col('Podiums', column_html_attrs={'class': 'py-2'})

    def get_tr_attrs(self, item):
        return {'class': 'driverStandingRow border-t hover:bg-gray-100'}

class ConstructorStandings(Table):
    classes = ['w-full', 'text-center']
    rank = Col('Rank', column_html_attrs={'class': 'py-2'})
    constructor = Col('Constructor', column_html_attrs={'class': 'text-left py-2'})
    points = Col('Points', column_html_attrs={'class': 'py-2'})
    wins = Col('Wins', column_html_attrs={'class': 'py-2'})
    podiums = Col('Podiums', column_html_attrs={'class': 'py-2'})

    def get_tr_attrs(self, item):
        return {'class': 'constructorStandingRow border-t hover:bg-gray-100'}

def getDriversTable():
    standings = db.session.execute(text(query_driver_standings))
    driver_standings = []
    for standing in standings:
        driver_standings.append(standing)
    return DriverStandings(driver_standings)

def getConstructorsTable():
    standings = db.session.execute(text(query_constructor_standings))
    constructor_standings = []
    for standing in standings:
        constructor_standings.append(standing)
    return ConstructorStandings(constructor_standings)