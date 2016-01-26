# Tests Common Snippets

## Prefix `t.*`

### [t.aftereach] afterEach

```javascript
afterEach(function() {
  ${1}
});
```

### [t.after] after

```javascript
after(function() {
  ${1}
});
```

### [t.beforeeach] beforeEach

```javascript
beforeEach(${1:'some description', }function${2: namedFun}() {
  ${3:beforeEach hook}
});
```

### [t.before] before

```javascript
before(function() {
  ${1}
});
```

### [t.describe] describe

```javascript
describe("$1", function() {
  $2
});
```

### [t.it] it

```javascript
it("${1}", function() {
  ${2}
});
```
