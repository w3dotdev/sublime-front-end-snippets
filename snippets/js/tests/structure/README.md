# Tests structure Snippets

## Prefix `ts.*`

### [ts.aftereach] afterEach

```javascript
afterEach(function() {
  ${1}
});
```

### [ts.after] after

```javascript
after(function() {
  ${1}
});
```

### [ts.beforeeach] beforeEach

```javascript
beforeEach(${1:'some description', }function${2: namedFun}() {
  ${3:beforeEach hook}
});
```

### [ts.before] before

```javascript
before(function() {
  ${1}
});
```

### [ts.describe] describe

```javascript
describe("$1", function() {
  $2
});
```

### [ts.it] it

```javascript
it("${1}", function() {
  ${2}
});
```
