import matplotlib.pyplot as plt
import pandas as pd



tab_param = pd.ExcelFile('C:/Users/Дмитрий/PycharmProjects/pythonProject3/dota.xlsx').parse('Лист1')
tab_param['Date'] = pd.to_datetime(tab_param['Date']).dt.date
plt.subplots(figsize=(14, 5))
plt.xticks(ticks=tab_param['Date'], rotation=90, size=14, labels=tab_param['Date'])
plt.yticks(size=14)
plt.xlabel('Дата', size=14)
plt.ylabel('Количество игроков, тыс.', size=14)
plt.bar(tab_param['Date'], tab_param['Peak'], width=10)
plt.savefig('Дима лаба.png', bbox_inches='tight', dpi=300)
