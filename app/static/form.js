// Generated by LiveScript 1.5.0
var map, BaseField, TextField, NestedRender, NestedForm, ListNested, FIELDTYPES, fieldFor, renderFormTo, toString$ = {}.toString, out$ = typeof exports != 'undefined' && exports || this, slice$ = [].slice;
map = require('prelude-ls').map;
BaseField = (function(){
  BaseField.displayName = 'BaseField';
  var prototype = BaseField.prototype, constructor = BaseField;
  function BaseField(key, field, value, handler){
    this.key = key;
    this.field = field;
    this.handler = handler;
    this.makeTag(value);
    this.setupEvents();
  }
  BaseField.prototype.makeTag = function(it){
    return this.el = L('input', {
      value: it != null ? it : '',
      'class': this.field['class']
    });
  };
  BaseField.prototype.setupEvents = function(){
    var this$ = this;
    this.el.addEventListener('keyup', function(){
      return this$.handler(this$.key, this$.el.value);
    });
  };
  BaseField.prototype.render = function(){
    return this.el;
  };
  return BaseField;
}());
TextField = (function(superclass){
  var prototype = extend$((import$(TextField, superclass).displayName = 'TextField', TextField), superclass).prototype, constructor = TextField;
  TextField.prototype.makeTag = function(it){
    return this.el = L('textarea', {
      text: it != null ? it : '',
      'class': this.field['class']
    });
  };
  function TextField(){
    TextField.superclass.apply(this, arguments);
  }
  return TextField;
}(BaseField));
NestedRender = (function(){
  NestedRender.displayName = 'NestedRender';
  var prototype = NestedRender.prototype, constructor = NestedRender;
  NestedRender.prototype.makeTag = function(){
    var ref$;
    return this.el = L((ref$ = this.field.tag) != null ? ref$ : 'div');
  };
  NestedRender.prototype.render = function(){
    var that, x$;
    if (that = this.field.legend) {
      x$ = L('fieldset');
      if (toString$.call(that).slice(8, -1) === 'String') {
        x$.appendChild(L('legend', {
          text: this.field.legend
        }));
      }
      x$.appendChild(this.el);
      return x$;
    } else {
      return this.el;
    }
  };
  function NestedRender(){}
  return NestedRender;
}());
NestedForm = (function(superclass){
  var prototype = extend$((import$(NestedForm, superclass).displayName = 'NestedForm', NestedForm), superclass).prototype, constructor = NestedForm;
  function NestedForm(key, field, o, handler){
    var nestedHandler, this$ = this;
    this.key = key;
    this.field = field;
    o == null && (o = {});
    this.handler = handler;
    this.makeTag();
    nestedHandler = function(key, value){
      o[key] = value;
      this$.handler(this$.key, o);
    };
    renderFormTo(this.el, this.field.config, o, nestedHandler);
  }
  return NestedForm;
}(NestedRender));
ListNested = (function(superclass){
  var prototype = extend$((import$(ListNested, superclass).displayName = 'ListNested', ListNested), superclass).prototype, constructor = ListNested;
  function ListNested(key, field, o, handler){
    this.key = key;
    this.field = field;
    this.handler = handler;
    if (!o) {
      this.handler(this.key, o = []);
    }
    this.makeTag();
    this.draw(o);
  }
  ListNested.prototype.draw = function(xs){
    var i$, len$;
    this.el.innerHTML = '';
    for (i$ = 0, len$ = xs.length; i$ < len$; ++i$) {
      (fn$.call(this, i$, xs[i$]));
    }
    return this.el.appendChild(this.makeAddButton(xs));
    function fn$(i, x){
      var elHandler, remHandler, x$, ref$, this$ = this;
      elHandler = function(key, value){
        x[key] = value;
        return this$.handler(this$.key, xs);
      };
      remHandler = function(){
        xs.splice(i, 1);
        this$.handler(this$.key, xs);
        return this$.draw(xs);
      };
      x$ = L((ref$ = this.field.item) != null ? ref$ : 'div');
      x$.appendChild(this.makeRemover(remHandler));
      renderFormTo(x$, this.field.config, x, elHandler);
      this.el.appendChild(x$);
    }
  };
  ListNested.prototype.makeAddButton = function(xs){
    var x$, this$ = this;
    x$ = L('span', {
      text: this.field.addText
    });
    x$.addEventListener('click', function(){
      xs.push({});
      return this$.draw(xs);
    });
    return x$;
  };
  ListNested.prototype.makeRemover = function(it){
    var x$;
    x$ = L('span', {
      text: this.field.removeText
    });
    x$.addEventListener('click', it);
    return x$;
  };
  return ListNested;
}(NestedRender));
FIELDTYPES = {
  input: BaseField,
  text: TextField,
  nested: NestedForm,
  "list-nested": ListNested
};
fieldFor = function(key, field, value, handler){
  var type, that;
  type = field.type;
  if (that = FIELDTYPES[type != null ? type : 'input']) {
    return new that(key, field, value, handler).render();
  } else {
    throw new Error("No such field type: " + type);
  }
};
out$.renderFormTo = renderFormTo = function(el, config, o, handler){
  var fields, key, field;
  fields = config.fields;
  map(partialize$.apply(el, [el.appendChild, [void 8], [0]]))(
  (function(){
    var ref$, x$, ref1$, results$ = [];
    for (key in ref$ = fields) {
      field = ref$[key];
      x$ = L((ref1$ = config.layout) != null ? ref1$ : 'div');
      if (field.label) {
        x$.appendChild(L('label', {
          text: field.label
        }));
      }
      x$.appendChild(fieldFor(key, field, o[key], handler));
      results$.push(x$);
    }
    return results$;
  }()));
};
function extend$(sub, sup){
  function fun(){} fun.prototype = (sub.superclass = sup).prototype;
  (sub.prototype = new fun).constructor = sub;
  if (typeof sup.extended == 'function') sup.extended(sub);
  return sub;
}
function import$(obj, src){
  var own = {}.hasOwnProperty;
  for (var key in src) if (own.call(src, key)) obj[key] = src[key];
  return obj;
}
function partialize$(f, args, where){
  var context = this;
  return function(){
    var params = slice$.call(arguments), i,
        len = params.length, wlen = where.length,
        ta = args ? args.concat() : [], tw = where ? where.concat() : [];
    for(i = 0; i < len; ++i) { ta[tw[0]] = params[i]; tw.shift(); }
    return len < wlen && len ?
      partialize$.apply(context, [f, ta, tw]) : f.apply(context, ta);
  };
}