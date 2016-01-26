# Node.js JavaScript Snippets

## Prefix `tn.*`

### [tn.dequal] deepEqual

```javascript
assert.deepEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tn.dsequal] deepStrictEqual

```javascript
assert.deepStrictEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tn.dnthrow] doesNotThrow

```javascript
assert.doesNotThrow(${1:block} ${2:, error} ${3:, message});
```

### [tn.equal] equal

```javascript
assert.equal(${1:actual}, ${2:expected} ${3:, message});
```

### [tn.fail] fail

```javascript
assert.fail(${1:actual}, ${2:expected}, ${3:message}, ${4:operator});
```

### [tn.iferror] ifError

```javascript
assert.ifError(${1:value});
```

### [tn.ndequal] notDeepEqual

```javascript
assert.notDeepEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tn.ndsequal] notDeepStrictEqual

```javascript
assert.notDeepStrictEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tn.nequal] notEqual

```javascript
assert.notEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tn.nsequal] notStrictEqual

```javascript
assert.notStrictEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tn.ok] ok

```javascript
assert.ok(${1:value}${2:, message});
```

### [tn.sequal] strictEqual

```javascript
assert.strictEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tn.throws] throws

```javascript
assert.throws(${1:block}, ${1:error} ${2:, message});
```

### [tn.a] Assert

```javascript
assert(${1:true}${2:, message});
```
