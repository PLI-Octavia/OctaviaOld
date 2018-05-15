{map} = require 'prelude-ls'

class BaseField
  (@key, @field, value, @handler) ->
    @make-tag value
    @setup-events!
  make-tag: -> @el = L 'input' value: it ? '', class: @field.class
  setup-events: !->
    @el.add-event-listener 'keyup' ~>
      @handler @key, @el.value
  render: -> @el

class TextField extends BaseField
  make-tag: -> @el = L 'textarea' text: it ? '', class: @field.class

class NestedRender
  make-tag: -> @el = L @field.tag ? 'div'
  render: ->
    if @field.legend
      # if we need to display a legend/fieldset...
      L 'fieldset'
        if typeof! that is 'String'
          # if anything else, just wrap in a fieldset with no legend
          ..append-child L 'legend' text: @field.legend
        ..append-child @el
    else
      @el

class NestedForm extends NestedRender
  (@key, @field, o = {}, @handler) ->
    @make-tag!
    nested-handler = (key, value) !~>
      # update current level's key
      o[key] = value
      # bubble up to the parent's handler
      @handler @key, o
    render-form-to @el, @field.config, o, nested-handler

class ListNested extends NestedRender
  (@key, @field, o, @handler) ->
    unless o
      @handler @key, o = []
    @make-tag!
    @draw o
  draw: (xs) ->
    @el.inner-HTML = ''
    for let x, i in xs
      # handler for this element
      el-handler = (key, value) ~>
        x[key] = value
        @handler @key, xs

      # "remove" button for this element
      rem-handler = ~>
        xs.splice i, 1 # remove the current element
        @handler @key, xs
        @draw xs # redraw list

      # create the wrapper
      L (@field.item ? 'div')
        # append the remove button
        ..append-child @make-remover rem-handler
        # append the subform
        render-form-to .., @field.config, x, el-handler

        # add it to the container
        @el.append-child ..
    @el.append-child @make-add-button(xs)

  # generates the "add" button
  make-add-button: (xs) ->
    L 'span' text: @field.add-text
      ..add-event-listener 'click' ~>
        xs.push {}
        @draw xs

  # generates the "remove" button
  make-remover: ->
    L 'span' text: @field.remove-text
      ..add-event-listener 'click' it


FIELD-TYPES =
  input: BaseField
  text: TextField
  nested: NestedForm
  "list-nested": ListNested
field-for = (key, {type}:field, value, handler) ->
  # dispatch on the correct field type
  if FIELD-TYPES[type ? \input]
    new that(key, field, value, handler)render!
  else
    throw new Error "No such field type: #type"

export render-form-to = (el, {fields}:config, o, handler) !->
  for key, field of fields
    # create an element with the correct configuration
    L (config.layout ? \div)
      if field.label
        # create a label if requested
        ..append-child L \label text: field.label
      # append the field
      ..append-child field-for(key, field, o[key], handler)
  |> map (el.append-child _)
