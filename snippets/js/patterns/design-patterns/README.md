# JavaScript Design Patterns Snippets

## Prefix `jdp.*`

### [jdp.command] Command

```javascript
(function(){
 
  var ${1:carManager} = {
 
    ${2:requestInfo}: function( ${2:model}, ${3:id} ){
      return ${4:"The information for " + ${2:model} + " with ID " + ${3:id} + " is foobar"};
    },
 
    ${5:buyVehicle}: function( ${5:model}, ${6:id} ){
      return ${7:"You have successfully purchased Item " + ${6:id} + ", a " + ${5:model}};
    },
 
    ${8:arrangeViewing}: function( ${9:model}, ${10:id} ){
      return ${11:"You have successfully booked a viewing of " + ${9:model} + " ( " + ${10:id} + " ) "};
    }
 
  };

  ${1:carManager}.${12:execute} = function ( ${13:name} ) {
    return ${1:carManager}[${13:name}] && ${1:carManager}[${13:name}].apply( ${1:carManager}, [].slice.call(arguments, 1) );
  };
  
  ${1:carManager}.${12:execute}( "${14:buyVehicle}", "${15:Ford Escort}", "${16:453543}" );

})();
```

### [jdp.constructor] Contructor

```javascript
var ${1:ConstructorName} = (function() {
  'use strict';
  function ${1:ConstructorName}(${2:args}) {
    // enforces new
    if (!(this instanceof ${1:ConstructorName})) {
      return new ${1:ConstructorName}(${2:args});
    }
    ${3:// constructor body
    }
  }
  ${4:${1:ConstructorName}.prototype.${5:methodName} = function(${6:args}) \{
    ${7:// method body
    }
  \}};
  return ${1:ConstructorName};
}());
```

### [jdp.decorator] Decorator

```javascript
function ${1:vehicle}( ${2:vehicleType} ){
  this.${2:vehicleType} = ${2:vehicleType} || '${3:car}',
    this.${4:model} = '${5:default}',
    this.${6:license} = '${7:00000-000}'
}

var ${8:testInstance} = new ${1:vehicle}('${3:car}');
var ${9:truck} = new ${1:vehicle}('truck');

${9:truck}.${10:setModel} = function( ${11:modelName} ){
    this.${4:model} = ${11:modelName};
}
${9:truck}.${12:setColor} = function( ${13:color} ){
    this.${13:color} = ${13:color};
}

${9:truck}.${10:setModel}('${14:CAT}');
${9:truck}.${12:setColor}('${15:blue}');

var ${16:secondInstance} = new ${1:vehicle}('${3:car}');
```

### [jdp.facade] Facade

```javascript
var ${1:MyModule} = ( function( window, undefined ) {

  function ${1:MyModule}() {

    function ${2:someMethod}() {
      ${3:alert( 'some method' );}
    }

    function ${4:someOtherMethod}() {
      ${5:alert( 'some other method' );}
    }

    return {
      ${2:someMethod} : function() {
        ${2:someMethod}();
      }
    };
  }

} )( window );
```

### [jdp.factory] Factory

```javascript
function ${1:Animal}(${2:name}) {
  ${9}
}

function ${3:Rabbit}(${2:name}) {
  var ${4:rabbit} = ${1:Animal}(${2:name})

  var ${5:parentRun} = ${4:rabbit}.${6:run}

  ${4:rabbit}.${7:jump} = function() {
    ${10:alert(${2:name} + " jumped!");}
  }

  ${4:rabbit}.${6:run} = function() {
    ${5:parentRun}.call(this)
    ${11:alert("fast");}
  }

  return ${4:rabbit}
}

${4:rabbit} = ${3:Rabbit}("${8:rab}");
```

### [jdp.flyweight] Flyweight

```javascript
${0:'use strict';}

var ${1:Flyweight} = function (${2:intrinisicState}) {
  this.${2:intrinisicState} = ${2:intrinisicState};
};

${1:Flyweight}.prototype.operation = function (${4:extrinsicState}) {
  ${3:// Perform some action using intrinsic and extrinsic state}
  return this.${2:intrinisicState} * ${4:extrinsicState};
};

module.exports = ${1:Flyweight};
```

### [jdp.mediator] Mediator

```javascript
var mediator = (function(){
  var subscribe = function(channel, fn){
    if(!mediator.channels[channel]) mediator.channels[channel] = [];
    mediator.channels[channel].push({ context : this, callback : fn });
    return this;
  };
  var publish = function(channel){
    if(!mediator.channels[channel]) return false;
    var args = Array.prototype.slice.call(arguments, 1);
    for(var i = 0, l = mediator.channels[channel].length; i < l; i++){
         var subscription = mediator.channels[channel][i];
         subscription.callback.apply(subscription.context.args);
    };
    return this;
  };
  return {
    channels : {},
    publish : publish,
    subscribe : subscribe,
    installTo : function(obj){
         obj.subscribe = subscribe;
         obj.publish = publish;
    }
  };
}());${1}
```

### [jdp.mixin] Mixin

```javascript
var ${1:Circle} = function() {};
${1:Circle}.prototype = {
  ${2:area}: function() {
    ${3:return Math.PI * this.radius * this.radius};
  },
  ${4:grow}: function() {
    ${5:this.radius++;}
  },
  ${6:shrink}: function() {
    ${7:this.radius--;}
  }
};${8}
```

### [jdp.module] Module

```javascript
var ${1:moduleName} = (function() {
  'use strict';
  var ${1:moduleName} = {
    init: {
      $2
    }
  };
  return ${1:moduleName};
}());
```

### [jdp.observer] Observer

```javascript
var ${1:Publisher} = {
  ${2:subscribers}: {
    ${6:any}: []
  },

  ${3:subscribe}: function(fn, type) {

    type = type || "${6:any}";
    if (typeof this.${2:subscribers}[type] === "undefined") {
      this.${2:subscribers}[type] = [];
    }

    this.${2:subscribers}[type].push(fn);
  },

  ${4:unsubscribe}: function(fn, type) {
    if (typeof this.${2:subscribers}[type] !== undefined) {
      this.${2:subscribers}[type].pull(fn);
    }
  },

  ${5:publish}: function(type, obj) {
    var ${2:subscribers} = this.${2:subscribers}[type];

    for (var i = 0, max = ${2:subscribers}.length; i < max; i++) {
      ${2:subscribers}[i](obj);
    }
  }
};


${7://var paper = Object.create(${1:Publisher});
//var joe = {
//  shout : function(obj){
//    console.log("oh i got issue" + obj);
//  }
//};

//paper.${3:subscribe}(joe.shout, "new issue");
//paper.${5:publish}("new issue", 27);}
```

### [jdp.prototype] Prototype

```javascript
function ${1:Car}() {
  // constructor...
}
${2:${1:Car}.prototype.${3:drive} = function () \{
  ${4: // body...
  }
\};}
return ${1:Car};
${0}
```

### [jdp.rmodule] Revealing Module

```javascript
var ${1:revealingModuleName} = (function() {
  'use strict';
  function ${2:methodName}() {
    ${3}
  }
  return {
    ${2:methodName}:${2:methodName}
  };
}());
```

### [jdp.singleton] Singleton

```javascript
var ${1:name} = (function() {
  'use strict';
  var instance;
  ${1:name} = function(${2:args}) {
    if (instance) {
      return instance;
    }
    instance = this;
    ${3:// your code goes here
    }
  };
  return ${1:name};
```
