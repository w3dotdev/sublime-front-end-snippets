# Universal Module Definition - JavaScript Snippets

## Prefix `jumd.*`

### [jumd.awg] AMD Web Global

```javascript
${1:// Uses AMD or browser globals to create a module. This example creates a
// global even when AMD is used. This is useful if you have some scripts
// that are loaded by an AMD loader, but they still want access to globals.
// If you do not need to export a global for the AMD case, see amdWeb.js.

// If you want something that will also work in Node, and still export a
// global in the AMD case, see returnExportsGlobal.js
// If you want to support other stricter CommonJS environments,
// or if you need to create a circular dependency, see commonJsStrictGlobal.js

// Defines a module "amdWebGlobal" that depends another module called "b".
// Note that the name of the module is implied by the file name. It is best
// if the file name and the exported global have matching names.

// If the 'b' module also uses this type of boilerplate, then
// in the browser, it will create a global .b that is used below.
}

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        ${2:// AMD. Register as an anonymous module.
        }
        define(['b'], function (b) {
            ${3:// Also create a global in case some scripts
            // that are loaded still are looking for
            // a global even when an AMD loader is in use.
            }
            return (root.amdWebGlobal = factory(b));
        });
    } else {
        ${4:// Browser globals
        }
        root.amdWebGlobal = factory(root.b);
    }
}(this, function (b) {
    ${5://use b in some fashion.

    // Just return a value to define the module export.
    // This example returns an object, but the module
    // can return a function as the exported value.
    }
    return {};
}));${6}
```

### [jumd.aw] AMD Web

```javascript
${1:// Uses AMD or browser globals to create a module.

// If you want something that will also work in Node, see returnExports.js
// If you want to support other stricter CommonJS environments,
// or if you need to create a circular dependency, see commonJsStrict.js

// Defines a module "amdWeb" that depends on another module called "b".
// Note that the name of the module is implied by the file name. It is best
// if the file name and the exported global have matching names.

// If the 'b' module also uses this type of boilerplate, then
// in the browser, it will create a global .b that is used below.

// If you do not want to support the browser global path, then you
// can remove the `root` use and the passing of `this` as the first arg to
// the top function.
}

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    ${2:// AMD. Register as an anonymous module.
    }
    define(['b'], factory);
  } else {
    ${3:// Browser globals
    }
    root.amdWeb = factory(root.b);
  }
}(this, function (b) {
  ${4://use b in some fashion.

  // Just return a value to define the module export.
  // This example returns an object, but the module
  // can return a function as the exported value.
  }
  return {};
}));${5}
```

### [jumd.ca] CommonJS Adapter

```javascript
${1:// Defines a module that works in CommonJS and AMD.

// This version can be used as common boilerplate for a library module
// that you only want to expose to CommonJS and AMD loaders. It will not work
// well for defining browser globals.

// If you only want to target Node and AMD or a CommonJS environment that
// supports assignment to module.exports and you are not defining a module
// that has a circular dependency, see nodeAdapter.js

// Help Node out by setting up define.
}
if (typeof exports === 'object' && typeof exports.nodeName !== 'string' && typeof define !== 'function') {
  var define = function (factory) {
    factory(require, exports, module);
  };
}

define(function (require, exports, module) {
  var b = require('b');

  ${2:// Only attach properties to the exports object to define
  // the module's properties.
  }
  exports.action = function () {};
});${3}
```

### [jumd.csg] CommonJS Strict Global

```javascript
${1:// Uses CommonJS, AMD or browser globals to create a module. This example
// creates a global even when AMD is used. This is useful if you have some
// scripts that are loaded by an AMD loader, but they still want access to
// globals. If you do not need to export a global for the AMD case, see
// commonjsStrict.js.

// If you just want to support Node, or other CommonJS-like environments that
// support module.exports, and you are not creating a module that has a
// circular dependency, then see returnExportsGlobal.js instead. It will allow
// you to export a function as the module value.

// Defines a module "commonJsStrictGlobal" that depends another module called
// "b". Note that the name of the module is implied by the file name. It is
// best if the file name and the exported global have matching names.

// If the 'b' module also uses this type of boilerplate, then
// in the browser, it will create a global .b that is used below.
}

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        ${2:// AMD. Register as an anonymous module.
        }
        define(['exports', 'b'], function (exports, b) {
            factory((root.commonJsStrictGlobal = exports), b);
        });
    } else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {
        ${3:// CommonJS
        }
        factory(exports, require('b'));
    } else {
        ${4:// Browser globals
        }
        factory((root.commonJsStrictGlobal = {}), root.b);
    }
}(this, function (exports, b) {
    ${5://use b in some fashion.

    // attach properties to the exports object to define
    // the exported module properties.
    }
    exports.action = function () {};
}));${6}
```

### [jumd.cs] CommonJS Strict

```javascript
${1:// Uses CommonJS, AMD or browser globals to create a module.

// If you just want to support Node, or other CommonJS-like environments that
// support module.exports, and you are not creating a module that has a
// circular dependency, then see returnExports.js instead. It will allow
// you to export a function as the module value.

// Defines a module "commonJsStrict" that depends another module called "b".
// Note that the name of the module is implied by the file name. It is best
// if the file name and the exported global have matching names.

// If the 'b' module also uses this type of boilerplate, then
// in the browser, it will create a global .b that is used below.

// If you do not want to support the browser global path, then you
// can remove the `root` use and the passing `this` as the first arg to
// the top function.
}

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    ${2:// AMD. Register as an anonymous module.
    }
    define(['exports', 'b'], factory);
  } else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {
    ${3:// CommonJS
    }
    factory(exports, require('b'));
  } else {
    ${4:// Browser globals
    }
    factory((root.commonJsStrict = {}), root.b);
  }
}(this, function (exports, b) {
  ${5://use b in some fashion.

  // attach properties to the exports object to define
  // the exported module properties.
  }
  exports.action = function () {};
}));${6}
```

### [jumd.jp] jQuery plugin

```javascript
${1:// Uses CommonJS, AMD or browser globals to create a jQuery plugin.
}

(function (factory) {
  if (typeof define === 'function' && define.amd) {
    ${2:// AMD. Register as an anonymous module.
    }
    define(['jquery'], factory);
  } else if (typeof module === 'object' && module.exports) {
      ${3:// Node/CommonJS
      }
      module.exports = function( root, jQuery ) {
        if ( jQuery === undefined ) {
          ${4:// require('jQuery') returns a factory that requires window to
          // build a jQuery instance, we normalize how we use modules
          // that require this pattern but the window provided is a noop
          // if it's defined (how jquery works)
          }
          if ( typeof window !== 'undefined' ) {
            jQuery = require('jquery');
          }
          else {
            jQuery = require('jquery')(root);
          }
        }
        factory(jQuery);
        return jQuery;
      };
  } else {
    ${5:// Browser globals
    }
    factory(jQuery);
  }
}(function ($) {
  $.fn.jqueryPlugin = function () { return true; };
}));${6}
```

### [jumd.na] Node Adapter

```javascript
${1:// Defines a module that works in Node and AMD.

// This version can be used as common boilerplate for a library module
// that you only want to expose to Node and AMD loaders. It will not work
// well for defining browser globals.

// If you need a version of this file that works CommonJS-like environments
// that do not support module.exports or if you want to define a module
// with a circular dependency, see commonjsAdapter.js
}

(function(define) {

  define(function (require, exports, module) {
    var b = require('b');

    return function () {};
  });

}( ${2:// Help Node out by setting up define.
}
  typeof module === 'object' && module.exports && typeof define !== 'function' ?
  function (factory) { module.exports = factory(require, exports, module); } :
  define
));${3}
```

### [jumd.reg] Return Exports Global

```javascript
${1:// Uses Node, AMD or browser globals to create a module. This example creates
// a global even when AMD is used. This is useful if you have some scripts
// that are loaded by an AMD loader, but they still want access to globals.
// If you do not need to export a global for the AMD case,
// see returnExports.js.

// If you want something that will work in other stricter CommonJS environments,
// or if you need to create a circular dependency, see commonJsStrictGlobal.js

// Defines a module "returnExportsGlobal" that depends another module called
// "b". Note that the name of the module is implied by the file name. It is
// best if the file name and the exported global have matching names.

// If the 'b' module also uses this type of boilerplate, then
// in the browser, it will create a global .b that is used below.
}

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    ${2:// AMD. Register as an anonymous module.
    }
    define(['b'], function (b) {
      return (root.returnExportsGlobal = factory(b));
    });
  } else if (typeof module === 'object' && module.exports) {
    ${3:// Node. Does not work with strict CommonJS, but
    // only CommonJS-like enviroments that support module.exports,
    // like Node.
    }
    module.exports = factory(require('b'));
  } else {
    ${4:// Browser globals
    }
    root.returnExportsGlobal = factory(root.b);
  }
}(this, function (b) {
  ${5://use b in some fashion.

  // Just return a value to define the module export.
  // This example returns an object, but the module
  // can return a function as the exported value.
  }
  return {};
}));${6}
```

### [jumd.re] Return Exports

```javascript
${1:// Uses Node, AMD or browser globals to create a module.

// If you want something that will work in other stricter CommonJS environments,
// or if you need to create a circular dependency, see commonJsStrict.js

// Defines a module "returnExports" that depends another module called "b".
// Note that the name of the module is implied by the file name. It is best
// if the file name and the exported global have matching names.

// If the 'b' module also uses this type of boilerplate, then
// in the browser, it will create a global .b that is used below.

// If you do not want to support the browser global path, then you
// can remove the `root` use and the passing `this` as the first arg to
// the top function.
}

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    ${2:// AMD. Register as an anonymous module.
    }
    define(['b'], factory);
  } else if (typeof module === 'object' && module.exports) {
    ${3:// Node. Does not work with strict CommonJS, but
    // only CommonJS-like environments that support module.exports,
    // like Node.
    }
    module.exports = factory(require('b'));
  } else {
    ${4:// Browser globals (root is window)
    }
    root.returnExports = factory(root.b);
  }
}(this, function (b) {
  ${5://use b in some fashion.

  // Just return a value to define the module export.
  // This example returns an object, but the module
  // can return a function as the exported value.
  }
  return {};
}));


${6:// if the module has no dependencies, the above pattern can be simplified to
}
(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    ${7:// AMD. Register as an anonymous module.
    }
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    ${8:// Node. Does not work with strict CommonJS, but
    // only CommonJS-like environments that support module.exports,
    // like Node.
    }
    module.exports = factory();
  } else {
    ${9:// Browser globals (root is window)
    }
    root.returnExports = factory();
  }
}(this, function () {
  ${10:// Just return a value to define the module export.
  // This example returns an object, but the module
  // can return a function as the exported value.
  }
  return {};
}));${11}
```
