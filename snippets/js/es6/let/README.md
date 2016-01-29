## ECMA Script 2015 Snippets

### [je.leti] ES6 For Loop Iterator using Let

```javascript
let ${1:v} = {
  [Symbol.iterator]() {
    ${2:let pre = ${3:0}, cur = ${4:1};}
    return {
      next() {
        ${5:[pre, cur] = [cur, pre + cur];}
        ${6:return ${7:\{ done: ${8:false}, value: ${9:cur}\};}}
      }
    };
  }
};$10
```

### [je.let] ES6 Let

```javascript
let ${1:${2:x} = ${3:'something'};$4}
```
