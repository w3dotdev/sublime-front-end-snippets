# Chai JavaScript Snippets

## Prefix `tc.*`

### [tc.a.e] equal

```javascript
assert.equal(${1:actual}, ${1:expected} ${2:, message});
```

### [tc.a.lo] lengthOf

```javascript
assert.lengthOf(${1:actual}, ${1:expected} ${2:, message});
```

### [tc.a.to] typeOf

```javascript
assert.typeOf(${1:actual}, ${1:expected} ${2:, message});
```

### [tc.e.tba] to.be.a

```javascript
expect(${1}).to.be.a(${2});
```

### [tc.e.te] to.equal

```javascript
expect(${1}).to.equal(${2});
```

### [tc.e.thl] to.have.length

```javascript
expect(${1}).to.have.length(${2});
```

### [tc.e.thp] to.have.property

```javascript
expect(${1}).to.have.property(${2}).with.length(${3});
```

### [tc.s.ba] be.a

```javascript
${1}.should.be.a(${2});
```

### [tc.s.e] equal

```javascript
${1}.should.equal(${2});
```

### [tc.s.hl] have.length

```javascript
${1}.should.have.length(${2});
```

### [tc.s.hp] have.property

```javascript
${1}.should.have.property(${2}).with.length(${3});
```
