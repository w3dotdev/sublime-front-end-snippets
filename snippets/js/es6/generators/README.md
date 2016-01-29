## ECMA Script 2015 Snippets

### [je.generators] ES6 Generators

```javascript
var ${1:generator} = {
  [Symbol:iterator]: function*() {
    ${2:var ${3:pre} = ${4:0}, ${5:cur} = ${6:1};}
    for(;;) {
      ${7:var ${8:temp} = ${9:pre};
      ${9:pre} = ${10:cur};
      ${10:cur} += ${8:temp};
      yield ${10:cur};}
    }
  }
};
```
