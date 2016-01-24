## Deferred

### [jqalways] always

```javascript
${1:\$.get("")}.always(${2:alwaysCallbacks}${3:,alwaysCallbacks});
```

### [jqdone] done

```javascript
${1:\$.get("")}.done(${2:doneCallbacks}${3:,doneCallbacks});
```

### [jqfail] fail

```javascript
${1:\$.get("")}.fail(${2:failCallbacks}${3:,failCallbacks});
```

### [jqnotifywith] notifyWith

```javascript
${1:\$.then()}.notifyWith(${2:context}${3:, args});
```

### [jqnotify] notify

```javascript
${1:\$.then()}.notify(${2:args});
```

### [jqprogress] progress

```javascript
${1:\$.then()}.progress(${2:progressCallbacks}${3:, progressCallbacks});
```

### [jqdpromise] deferred promise

```javascript
${1:\$.then()}.promise(${2:target});
```

### [jqrejectwith] rejectWith

```javascript
${1:\$.then()}.rejectWith(${2:context}${3:, args});
```

### [jqreject] reject

```javascript
${1:\$.then()}.reject(${2:args});
```

### [jqresolvewith] resolveWith

```javascript
${1:\$.then()}.resolveWith(${2:context}${3:, args});
```

### [jqstate] state

```javascript
${1:\$.resolve()}.state();
```

### [jqthen] then

```javascript
${1:\$.get()}.then(${2:doneFilter}${3:, failFilter}${4:, progressFilter});
```

### [jqd] deferred

```javascript
${1:\$}.Deferred(${2:beforeStart});
```

### [jqpromise] promise

```javascript
${1:\$(document)}.promise(${2:type}${3:, target});
```

### [jqresolve] resolve

```javascript
${1:\$.then()}.resolve(${2:args});
```
