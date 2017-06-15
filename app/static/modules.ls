export octavia =
  modules: []
  require: !->
    [ctrl, action] = it / '_'
    @modules[ctrl]?[action]?!

  register: ([ctrl, action], fn) !->
    @modules{}[ctrl][action] = fn

{map} = require 'prelude-ls'

hide = -> it.style.visibility = 'hidden'
el = (tag) -> document.create-element tag

octavia.register <[student login]> !->
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
