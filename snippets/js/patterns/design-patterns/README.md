# JavaScript Design Patterns Snippets

## Prefix `jdp.*`

### [jdp.command] Command

```javascript

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

```

### [jdp.facade] Facade

```javascript

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
