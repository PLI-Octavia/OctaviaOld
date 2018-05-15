<-! octavia.register 'game_scores'

users = {[..pk, ..fields] for js-data-users}
console.log users
scores = {}
averages = []
for {fields: {student: student-id, value, date}} in js-data-scores
  student = users[student-id]
  scores[][student.username]push [new Date date .value-of!; value]
for username, values of scores
  averages.push [username, avg map (.1), values]
data = [{name: username, data: sort-by (.0), values} for username, values of scores]
average-data = sort-by (.1), averages

Highcharts.chart 'stats_base' do
  title:
    text: 'Statistiques'
  xAxis:
    type: 'datetime'
  yAxis:
    title:
      text: 'Score'
  series: data
Highcharts.chart 'stats_avg' do
  chart:
    type: 'column'
  title:
    text: 'Moyennes'
  xAxis:
    type: 'category'
  series:
    * name: 'Moyennes'
      data: average-data
    ...

