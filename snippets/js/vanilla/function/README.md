## JavaScript Function Snippets

### [jafn] Anonymous Function

```javascript
function(${1:arguments}) {
    ${2}
}
```

### [japply] Function apply

```javascript
${1:methodName}.apply(${2:context}, [${3:arguments}])
```

### [jcall] Function call

```javascript
${1:methodName}.call(${2:context}, ${3:arguments})
```

### [jiife] Immediately-invoked function expression

```javascript
(function(window, document, undefined) {
  ${1}
})(window, document);
```

### [jprot] Prototype

```javascript
${1:ClassName}.prototype.${2:methodName} = function(${3:arguments}) {
    ${4}
}
```

### [jfn] Function

```javascript
function ${1:methodName}(${2:arguments}) {
    ${3}
}
```
