## Manipulation

### [jq.after] after

```javascript
${1:\$(this)}.after(${2:content}${3:,content});
```

### [jq.appendto] appendTo

```javascript
${1:\$(this)}.appendTo(${2:content}${3:,content});
```

### [jq.append] append

```javascript
${1:\$(this)}.append(${2:content}${3:,content});
```

### [jq.before] before

```javascript
${1:\$(this)}.before(${2:content}${3:,content});
```

### [jq.clone] clone

```javascript
${1:\$(this)}.clone(${2:withDataAndEvents}${3:,deepWithDataAndEvents});
```

### [jq.detach] detach

```javascript
${1:\$(this)}.detach(${2:selector});
```

### [jq.empty] empty

```javascript
${1:\$(this)}.empty();
```

### [jq.iafter] insertAfter

```javascript
${1:\$(this)}.insertAfter(${2:target});
```

### [jq.ibefore] insertBefore

```javascript
${1:\$(this)}.insertBefore(${2:target});
```

### [jq.prependto] prependTo

```javascript
${1:\$(this)}.prependTo(${2:target});
```

### [jq.prepend] prepend

```javascript
${1:\$(this)}.prepend(${2:content}${3:,content});
```

### [jq.remove] remove

```javascript
${1:\$(this)}.remove(${2:selector});
```

### [jq.replaceall] replaceAll

```javascript
${1:\$(this)}.replaceAll(${2:target});
```

### [jq.replacewith] replaceWith

```javascript
${1:\$(this)}.replaceWith(${2:newContent});
```

### [jq.text] text

```javascript
${1:\$(this)}.text();
```

### [jq.unwrap] unwrap

```javascript
${1:\$(this)}.unwrap();
```

### [jq.wall] wrapAll

```javascript
${1:\$(this)}.wrapAll(${2:wrappingElement});
```

### [jq.winner] wrapInner

```javascript
${1:\$(this)}.wrapInner(${2:wrappingElement});
```

### [jq.wrap] wrap

```javascript
${1:\$(this)}.wrap(${2:wrappingElement});
```
