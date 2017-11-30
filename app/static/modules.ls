export octavia =
  modules: {}
  aliases: {}
  require: ->
    while @aliases[it] => it = that
    @modules[it]?!

  register: (module, @modules[module]) !->

  alias: (old, @aliases[old]) !->

{map, sort-by, average} = require 'prelude-ls'

avg = ->
  return 0 unless it
  average it or 0

hide = -> it.style.visibility = 'hidden'
el = (tag) -> document.create-element tag

octavia.register 'login-form' !->
  shapes = <[square circle triangle]> # cross
  selected-shapes = []
  {parent-node: password-container}:password-field = document.query-selector '#input-password'
  password-shapes = document.query-selector '.password-shapes'
  unselected-shape = (idx) ->
    ->
      selected-shapes.splice idx, 1
      render-password!
  render-password = ->
    password-shapes.inner-HTML = ''
    password-field.value = selected-shapes * ' '
    for let password-shape, idx in selected-shapes
      el 'span'
        ..class-name = "shape shape-#password-shape"
        ..onclick = unselected-shape idx
        password-shapes.append-child ..

  hide password-field

  shape-selector = document.query-selector '.shape-selector'
  for let shape in shapes
    console.log shape
    shape-el = el 'span'
      ..class-name = "shape shape-#shape"
    shape-el.onclick = !->
      selected-shapes.push shape
      render-password!
    shape-selector.append-child shape-el

octavia.alias 'student_login' 'login-form'
octavia.alias 'student_create' 'login-form'

octavia.register 'game_scores' !->
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
  average_data = sort-by (.1), averages
  console.log JSON.stringify data
  console.log JSON.stringify average_data

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
        data: average_data
      ...
