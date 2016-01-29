## ECMA Script 2015 Snippets

### [je.simport] ES6 Dynamic Module Import

```javascript
System.import(${1:'my-module'})${2:.then(function(${3:m}) \{
  $3
\})};
```

### [je.efunction] ES6 Module Export Function

```javascript
export function ${2:name}(${3:args}) {
  $4
}
```

### [je.evariable] ES6 Module Export Variable

```javascript
export var ${1:myvar} = ${2:value};
```

### [je.import] ES6 Module Import

```javascript
import ${1:*} ${2:as ${3:mod}} from ${4:"lib/package"};
```

### [je.loader] ES6 Loader Class

```javascript
var ${1:loader} = new Loader({
  ${2:global: fixup(window)}
});
```

### [je.sget] ES6 System Get Module

```javascript
System.get(${1:'module'});
```

### [je.sset] ES6 System Set Module

```javascript
System.set(${1:'jquery'}, ${2:Module(${3:\{\$: \$\}})});
```
