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

```

### [jdp.flyweight] Flyweight

```javascript

```

### [jdp.mediator] Mediator

```javascript

```

### [jdp.mixin] Mixin

```javascript

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
