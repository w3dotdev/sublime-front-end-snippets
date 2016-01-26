## Deferred

### [jq.always] always

```javascript
${1:\$.get("")}.always(${2:alwaysCallbacks}${3:,alwaysCallbacks});
```

### [jq.done] done

```javascript
${1:\$.get("")}.done(${2:doneCallbacks}${3:,doneCallbacks});
```

### [jq.fail] fail

```javascript
${1:\$.get("")}.fail(${2:failCallbacks}${3:,failCallbacks});
```

### [jq.notifywith] notifyWith

```javascript
${1:\$.then()}.notifyWith(${2:context}${3:, args});
```

### [jq.notify] notify

```javascript
${1:\$.then()}.notify(${2:args});
```

### [jq.progress] progress

```javascript
${1:\$.then()}.progress(${2:progressCallbacks}${3:, progressCallbacks});
```

### [jq.dpromise] deferred promise

```javascript
${1:\$.then()}.promise(${2:target});
```

### [jq.rejectwith] rejectWith

```javascript
${1:\$.then()}.rejectWith(${2:context}${3:, args});
```

### [jq.reject] reject

```javascript
${1:\$.then()}.reject(${2:args});
```

### [jq.resolvewith] resolveWith

```javascript
${1:\$.then()}.resolveWith(${2:context}${3:, args});
```

### [jq.state] state

```javascript
${1:\$.resolve()}.state();
```

### [jq.then] then

```javascript
${1:\$.get()}.then(${2:doneFilter}${3:, failFilter}${4:, progressFilter});
```

### [jq.d] deferred

```javascript
${1:\$}.Deferred(${2:beforeStart});
```

### [jq.promise] promise

```javascript
${1:\$(document)}.promise(${2:type}${3:, target});
```

### [jq.resolve] resolve

```javascript
${1:\$.then()}.resolve(${2:args});
```
