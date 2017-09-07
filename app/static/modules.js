// Generated by LiveScript 1.5.0
(function(){
  var octavia, map, hide, el, out$ = typeof exports != 'undefined' && exports || this, join$ = [].join;
  out$.octavia = octavia = {
    modules: {},
    aliases: {},
    require: function(it){
      var that, ref$;
      while (that = this.aliases[it]) {
        it = that;
      }
      return typeof (ref$ = this.modules)[it] == 'function' ? ref$[it]() : void 8;
    },
    register: function(module, arg$){
      this.modules[module] = arg$;
    },
    alias: function(old, arg$){
      this.aliases[old] = arg$;
    }
  };
  map = require('prelude-ls').map;
  hide = function(it){
    return it.style.visibility = 'hidden';
  };
  el = function(tag){
    return document.createElement(tag);
  };
  octavia.register('login-form', function(){
    var shapes, selectedShapes, passwordField, passwordContainer, passwordShapes, unselectedShape, renderPassword, shapeSelector, i$, len$;
    shapes = ['square', 'circle', 'triangle'];
    selectedShapes = [];
    passwordField = document.querySelector('#input-password'), passwordContainer = passwordField.parentNode;
    passwordShapes = document.querySelector('.password-shapes');
    unselectedShape = function(idx){
      return function(){
        selectedShapes.splice(idx, 1);
        return renderPassword();
      };
    };
    renderPassword = function(){
      var i$, ref$, len$, results$ = [];
      passwordShapes.innerHTML = '';
      passwordField.value = join$.call(selectedShapes, ' ');
      for (i$ = 0, len$ = (ref$ = selectedShapes).length; i$ < len$; ++i$) {
        results$.push((fn$.call(this, i$, ref$[i$])));
      }
      return results$;
      function fn$(idx, passwordShape){
        var x$;
        x$ = el('span');
        x$.className = "shape shape-" + passwordShape;
        x$.onclick = unselectedShape(idx);
        passwordShapes.appendChild(x$);
        return x$;
      }
    };
    hide(passwordField);
    shapeSelector = document.querySelector('.shape-selector');
    for (i$ = 0, len$ = shapes.length; i$ < len$; ++i$) {
      (fn$.call(this, shapes[i$]));
    }
    function fn$(shape){
      var x$, shapeEl;
      console.log(shape);
      x$ = shapeEl = el('span');
      x$.className = "shape shape-" + shape;
      shapeEl.onclick = function(){
        selectedShapes.push(shape);
        renderPassword();
      };
      shapeSelector.appendChild(shapeEl);
    }
  });
  octavia.alias('student_login', 'login-form');
  octavia.alias('student_create', 'login-form');
}).call(this);
