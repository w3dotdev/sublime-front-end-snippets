# JavaScript Snippets

## Console

### [j-cd] console.dir

```javascript
console.dir(${1:obj});
```

### [j-ce] console.error

```javascript
console.error(${1:obj});
```

### [j-ci] console.info

```javascript
console.info(${1:obj});
```

### [j-cl] console.log

```javascript
console.log(${1:obj});
```

### [j-cw] console.warn

```javascript
console.warn(${1:obj});
```

## DOM

### [j-ael] addEventListener

```javascript
${1:document}.addEventListener('${2:event}', function(event) {
    ${3}
});
```

### [j-ac] appendChild

```javascript
${1:document}.appendChild(${2:element});
```

### [j-cla] classList.add

```javascript
${1:document}.classList.add('${2:class}');
```

### [j-clr] classList.remove

```javascript
${1:document}.classList.remove('${2:class}');
```

### [j-clt] classList.toggle

```javascript
${1:document}.classList.toggle('${2:class}');
```

### [j-cdf] createDocumentFragment

```javascript
${1:document}.createDocumentFragment(${2:element});
```

### [j-cel] createElement

```javascript
${1:document}.createElement(${2:element});
```

### [j-gattr] getAttribute

```javascript
${1:document}.getAttribute('${2:attr}');
```

### [j-gid] getElementById

```javascript
${1:document}.getElementById('${2:id}');
```

### [j-gclass] getElementsByClassName

```javascript
${1:document}.getElementsByClassName('${2:class}');
```

### [j-gtag] getElementsByTagName

```javascript
${1:document}.getElementsByTagName('${2:tag}');
```

### [j-ih] innerHTML

```javascript
${1:document}.innerHTML = '${2:elem}';
```

### [j-qsa] querySelectorAll

```javascript
${1:document}.querySelectorAll('${2:selector}');
```

### [j-qs] querySelector

```javascript
${1:document}.querySelector('${2:selector}');
```

### [j-rattr] removeAttribute

```javascript
${1:document}.removeAttribute('${2:attr}');
```

### [j-rc] removeChild

```javascript
${1:document}.removeChild(${2:element});
```

### [j-sattr] setAttribute

```javascript
${1:document}.setAttribute('${2:attr}', ${3:value});
```

### [j-tc] textContent

```javascript
${1:document}.textContent = '${2:content}';
```

## Function

### [j-fna] Anonymous Function

```javascript
function(${1:arguments}) {
    ${2}
}
```

### [j-apply] Function apply

```javascript
${1:methodName}.apply(${2:context}, [${3:arguments}])
```

### [j-call] Function call

```javascript
${1:methodName}.call(${2:context}, ${3:arguments})
```

### [j-iife] Immediately-invoked function expression

```javascript
(function(window, document, undefined) {
  ${1}
})(window, document);
```

### [j-prot] Prototype

```javascript
${1:ClassName}.prototype.${2:methodName} = function(${3:arguments}) {
    ${4}
}
```

### [j-fn] Function

```javascript
function ${1:methodName}(${2:arguments}) {
    ${3}
}
```

## JSON

### [j-jp] JSON.parse

```javascript
JSON.parse(${1:obj});
```

### [j-js] JSON.stringify

```javascript
JSON.stringify(${1:obj});
```

## Loop

### [j-fore] forEach

```javascript
${1:myArray}.forEach(function(${2:element}) {
    ${3}
});
```

### [j-fori] for in

```javascript
for (${1:prop} in ${2:obj}) {
  if (${2:obj}.hasOwnProperty(${1:prop})) {
    ${3}
  }
}
```

### [j-for] for

```javascript
for (var i = ${1:0}, len = ${2:10}; i ${3:<=} len; i${4:++} ) {
  ${5}
}
```

## Timer

### [j-si] setInterval

```javascript
setInterval(function() {
  ${2}
}, ${1:delay});
```

### [j-st] setTimeout

```javascript
setTimeout(function() {
    ${2}
}, ${1:delay});
```
