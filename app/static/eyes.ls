$eye = $ '.eye'
if $eye.length
  const PREFIXES = [\-webkit- \-moz- \-ms- '']
  <-! $ document.body .mousemove
  {left, top} = $eye.offset!
  x = left + $eye.width! / 2
  y = top + $eye.height! / 2
  rad = Math.atan2 it.pageX - x, it.pageY - y
  rot = (rad * (180 / Math.PI) * -1) + 230
  $eye.css {["#{..}transform", "rotate(#{rot}deg)"] for PREFIXES}
