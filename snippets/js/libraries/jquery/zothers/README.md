## Others

### [jq.b] jQuery Boilerplate

```javascript
/**
 * Plugin: ${1}
 * Description: ${2}
 * Author: ${3}
 * License: ${4}
 */
${5:// the semi-colon before function invocation is a safety net against concatenated
// scripts and/or other plugins which may not be closed properly.}
;(function ( \$, window, document, undefined ) {

  "use strict";

  ${6:// undefined is used here as the undefined global variable in ECMAScript 3 is
  // mutable (ie. it can be changed by someone else). undefined isn't really being
  // passed in so we can ensure the value of it is truly undefined. In ES5, undefined
  // can no longer be modified.

  // window and document are passed through as local variable rather than global
  // as this (slightly) quickens the resolution process and can be more efficiently
  // minified (especially when both are regularly referenced in your plugin).

  // Create the defaults once}
  var pluginName = "${13:defaultPluginName}",
    defaults = {
    propertyName: "value"
  };

  ${7:// The actual plugin constructor}
  function Plugin ( element, options ) {
    this.element = element;
    ${8:// jQuery has an extend method which merges the contents of two or
    // more objects, storing the result in the first object. The first object
    // is generally empty as we don't want to alter the default options for
    // future instances of the plugin}
    this.settings = \$.extend( {}, defaults, options );
    this._defaults = defaults;
    this._name = pluginName;
    this.init();
  }

  ${9:// Avoid Plugin.prototype conflicts}
  \$.extend(Plugin.prototype, {
    init: function () {
      ${10:// Place initialization logic here
      // You already have access to the DOM element and
      // the options via the instance, e.g. this.element
      // and this.settings
      // you can add more functions like the one below and
      // call them like the example bellow}
      ${15:this.yourOtherFunction("jQuery Boilerplate");}
    },
    ${14:yourOtherFunction: function (text) \{
      ${11:// some logic}
      \$(this.element).text(text);
    \}}
  });

  ${12:// A really lightweight plugin wrapper around the constructor,
  // preventing against multiple instantiations}
  \$.fn[ pluginName ] = function ( options ) {
    return this.each(function() {
      if ( !\$.data( this, "plugin_" + pluginName ) ) {
        \$.data( this, "plugin_" + pluginName, new Plugin( this, options ) );
      }
    });
  };

})( jQuery, window, document );
```
