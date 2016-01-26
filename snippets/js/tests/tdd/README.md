# TDD JavaScript Snippets

## Prefix `tt.*`

### [tt.dequal] deepEqual

```javascript
assert.deepEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tt.dsequal] deepStrictEqual

```javascript
assert.deepStrictEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tt.dnthrow] doesNotThrow

```javascript
assert.doesNotThrow(${1:block} ${2:, error} ${3:, message});
```

### [tt.equal] equal

```javascript
assert.equal(${1:actual}, ${2:expected} ${3:, message});
```

### [tt.fail] fail

```javascript
assert.fail(${1:actual}, ${2:expected}, ${3:message}, ${4:operator});
```

### [tt.iferror] ifError

```javascript
assert.ifError(${1:value});
```

### [tt.ndequal] notDeepEqual

```javascript
assert.notDeepEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tt.ndsequal] notDeepStrictEqual

```javascript
assert.notDeepStrictEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tt.nequal] notEqual

```javascript
assert.notEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tt.nsequal] notStrictEqual

```javascript
assert.notStrictEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tt.ok] ok

```javascript
assert.ok(${1:value}${2:, message});
```

### [tt.sequal] strictEqual

```javascript
assert.strictEqual(${1:actual}, ${1:expected} ${2:, message});
```

### [tt.throws] throws

```javascript
assert.throws(${1:block}, ${1:error} ${2:, message});
```

### [tt.a] Assert

```javascript
assert(${1:true}${2:, message});
```
