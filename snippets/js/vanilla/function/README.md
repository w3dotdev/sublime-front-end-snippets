## JavaScript Function Snippets

### [j.afn] Anonymous Function

```javascript
function(${1:arguments}) {
    ${2}
}
```

### [j.apply] Function apply

```javascript
${1:methodName}.apply(${2:context}, [${3:arguments}])
```

### [j.call] Function call

```javascript
${1:methodName}.call(${2:context}, ${3:arguments})
```

### [j.iife] Immediately-invoked function expression

```javascript
(function(window, document, undefined) {
  ${1}
})(window, document);
```

### [j.prot] Prototype

```javascript
${1:ClassName}.prototype.${2:methodName} = function(${3:arguments}) {
    ${4}
}
```

### [j.fn] Function

```javascript
function ${1:methodName}(${2:arguments}) {
    ${3}
}
```
