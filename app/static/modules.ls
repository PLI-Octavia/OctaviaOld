export octavia =
  modules: {}
  aliases: {}
  require: ->
    while @aliases[it] => it = that
    @modules[it]?!

  register: (module, @modules[module]) !->

  alias: (old, @aliases[old]) !->

{map} = require 'prelude-ls'

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
  for {fields: {student: student-id, value, date}} in js-data-scores
    student = users[student-id]
    scores[][student.username]push [new Date date .value-of!; value]
  data = [{name: username, data: values} for username, values of scores]
  console.log JSON.stringify data

  Highcharts.chart 'stats' do
    title:
      text: 'Statistiques'
    xAxis:
      type: 'datetime'
    yAxis:
      title:
        text: 'Score'
    series: data
