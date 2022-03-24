
from collections import namedtuple

def fin_copmanies(count):
    companies = [0] * count
    mid_profit = [0] * count
    company_less_mid_profit = []
    company_more_mid_profit = []
    # Create data for every company
    for i in range(count):
        company = namedtuple(input('Enter name of company: '),
                                  ['q1', 'q2', 'q3', 'q4'])
        companies[i] = company(int(input('Enter profit for 1st quarter: ')),
                               int(input('Enter profit for 2nd quarter: ')),
                               int(input('Enter profit for 3rd quarter: ')),
                               int(input('Enter profit for 4th quarter: ')))
    # Calculate middle profit for every company and all middle profit
    for company in range(len(companies)):
        mid_profit[company] = sum(companies[company])/4
    mid_profit_all = sum(mid_profit)/len(companies)
    # identify what company has less profit or more profit then middle value
    for profit in mid_profit:
        if profit > mid_profit_all:
            company_more_mid_profit.append(mid_profit.index(profit))
        else:
            company_less_mid_profit.append(mid_profit.index(profit))
    print()
    print('The middle of profit all companies', mid_profit_all)
    print('Companies, who have profit less then middle:', end=' ')
    for company in company_less_mid_profit:
        if company == company_less_mid_profit[-1]:
            print(type(companies[company]).__name__)
        else:
            print(type(companies[company]).__name__, end=', ')

    print('Companies, who have profit more then middle:', end=' ')
    for company in company_more_mid_profit:
        if company == company_more_mid_profit[-1]:
            print(type(companies[company]).__name__)
        else:
            print(type(companies[company]).__name__, end=', ')


if __name__ == '__main__':
    fin_copmanies(int(input('Enter number of companies: ')))


