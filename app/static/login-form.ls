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
      L 'span'
        ..class-name = "shape shape-#password-shape"
        ..onclick = unselected-shape idx
        password-shapes.append-child ..

  hide password-field

  shape-selector = document.query-selector '.shape-selector'
  for let shape in shapes
    console.log shape
    shape-el = L 'span'
      ..class-name = "shape shape-#shape"
    shape-el.onclick = !->
      selected-shapes.push shape
      render-password!
    shape-selector.append-child shape-el

octavia.alias 'student_login' 'login-form'
octavia.alias 'student_create' 'login-form'
