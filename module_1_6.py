countries_gold_medals = {'USA' : 7  , 'Russia' : 12 , 'Brazil' : 9}
print('Countries thet have won the most gold medals: ', countries_gold_medals)
print('Most of almonds: ', (countries_gold_medals['Russia']))
print('Swiming midals: ', (countries_gold_medals.get('China')))
countries_gold_medals.update({'Germany' : 5 , 'Georgia': 4})
print('Full list of gold medals winners:', countries_gold_medals)
doping = countries_gold_medals.pop('USA')
print('Number of medals taken away for doping:' , doping)
print('New list of gold medals winners:', countries_gold_medals)


list_ = {43, 'car', 163.452, 12, 43, 589, 'car'}
print(list_)
list_.add('phone')
list_.add(13)
list_.discard(163.452)
print(list_)