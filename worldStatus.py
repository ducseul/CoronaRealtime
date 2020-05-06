'''
{'total_cases': 3741269, 'total_recovered': 1247374, 'total_unresolved': 2039891, 'total_deaths': 258509, 'total_new_cases_today': 16752, 'total_new_deaths_today': 482, 'total_active_cases': 2235386, 'total_serious_cases': 49245, 'total_affected_countries': 212, 'source': {'url': 'https://thevirustracker.com/'}}
'''
from datetime import datetime

class WorldStatus:
    def __init__(self, total_cases, total_recovered, total_deaths, total_new_cases_today, total_new_deaths_today, total_affected_countries):
        self.total_cases = total_cases
        self.total_recovered = total_recovered
        self.total_deaths = total_deaths
        self.total_new_cases_today = total_new_cases_today
        self.total_new_deaths_today = total_new_deaths_today
        self.total_affected_countries = total_affected_countries
        self.updatedTime = datetime.now().strftime("%b %d %Y %H:%M:%S")
    
    def formating_Number(self, args):
        return "{:,}".format(int(args))

    def toString(self):
        return "\n=========\nTime Updated: {}\n Total Case: {}\n Total Recovered: {}\n Total Deaths: {}\n=========\nTotal New Cases: {}\nTotal New Deaths Today: {}\nTotal Country Affected: {}".format(
            self.updatedTime, self.formating_Number(self.total_cases), self.formating_Number(self.total_recovered), self.formating_Number(self.total_deaths), self.formating_Number(self.total_new_cases_today), self.formating_Number(self.total_new_deaths_today), self.formating_Number(self.total_affected_countries))