# QUnit JavaScript Snippets

## Prefix `tq.*`

### [tq.async] async

```javascript
assert.async(${1:acceptCallCount});
```

### [tq.dequal] deepEqual

```javascript
assert.deepEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tq.equal] equal

```javascript
assert.equal(${1:actual}, ${2:expected} ${3:, message});
```

### [tq.ndequal] notDeepEqual

```javascript
assert.notDeepEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tq.nequal] notEqual

```javascript
assert.notEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tq.nok] notOk

```javascript
assert.notOk(${1:state} ${2:, message});
```

### [tq.npequal] notPropEqual

```javascript
assert.notPropEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tq.nsequal] notStrictEqual

```javascript
assert.notStrictEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tq.ok] ok

```javascript
assert.ok(${1:state} ${2:, message});
```

### [tq.pequal] propEqual

```javascript
assert.propEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tq.sequal] strictEqual

```javascript
assert.strictEqual(${1:actual}, ${2:expected} ${3:, message});
```

### [tq.throws] throws

```javascript
assert.throws(${1:block}${2:, expected}${3:, message});
```

### [tq.begin] QUnit.begin

```javascript
QUnit.begin(${1:callback})
```

### [tq.config] QUnit.config

```javascript
QUnit.config.${1:urlConfig}
```

### [tq.done] QUnit.done

```javascript
QUnit.done(${1:callback});
```

### [tq.dparse] QUnit.dump.parse

```javascript
QUnit.dump.parse(${1:data});
```

### [tq.expect] Expect

```javascript
QUnit.expect(${1:amount});
```

### [tq.extend] QUnit.extend

```javascript
QUnit.extend(${1:target}, ${2:mixin});
```

### [tq.log] QUnit.log

```javascript
QUnit.log(${1:callback});
```

### [tq.mdone] QUnit.moduleDone

```javascript
QUnit.moduleDone(${1:callback});
```

### [tq.mstart] QUnit.moduleStart

```javascript
QUnit.moduleStart(${1:callback});
```

### [tq.module] QUnit.module

```javascript
QUnit.module(${1:name}${2:, hooks}${3:, nested});
```

### [tq.only] QUnit.only

```javascript
QUnit.only(${1:name}, ${2:callback});
```

### [tq.push] push

```javascript
${1:this}.push(${2:result}, ${3:actual},  ${4:expected}, ${5:message});
```

### [tq.skip] QUnit.skip

```javascript
QUnit.skip(${1:name});
```

### [tq.stack] QUnit.stack

```javascript
QUnit.stack(${1:offset});
```

### [tq.tdone] QUnit.testDone

```javascript
QUnit.testDone(${1:callback});
```

### [tq.tstart] QUnit.testStart

```javascript
QUnit.testStart(${1:callback});
```

### [tq.test] Test

```javascript
QUnit.test(${1:name}, ${2:callback});
```
