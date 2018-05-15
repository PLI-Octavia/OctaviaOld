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

export gEBI = -> document.get-element-by-id it
hide = -> it.style.visibility = 'hidden'
set-tag-attr = (el, k, v) -> switch
| k in <[content text]>
  el.inner-HTML = v
| k is \class
  el.class-list.add v
| k is \classes
  for v
    el.class-list.add ..
| _
  el[k] = v
# L :: TagName -> Attrs -> DOMElement
# L :: Attrs+{tag: TagName} -> defaultTag: TagName -> DOMElement
export L = (tag, attrs) ->
  if typeof! tag is 'Object'
    if tag.tag
      # TODO LiveScript 1.6:
      #{tag, ...attrs} = tag
      # XXX temp fix:
      attrs = tag
      tag = tag.tag
    else
      # use attrs as defaulted-to tag
      [tag, attrs] = [attrs, tag]
  document.create-element tag
    for k, v of attrs when v?
      set-tag-attr .., k, v

