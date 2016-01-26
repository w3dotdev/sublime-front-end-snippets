## Callbacks

### [jq.cbadd] add

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.add(${4:callbacks});
```

### [jq.cbdisable] disable

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.disable();
```

### [jq.cbdisabled] disabled

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.disabled();
```

### [jq.cbempty] empty

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.empty();
```

### [jq.cbfirewith] fireWith

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.fireWith(${4:context}${5:, args});
```

### [jq.cbfire] fire

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.fire(${4:arguments});
```

### [jq.cbfired] fired

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.fired();
```

### [jq.cbhas] has

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.has(${4:callback});
```

### [jq.cblock] lock

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.lock();
```

### [jq.cblocked] locked

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.locked();
```

### [jq.cbremove] remove

```javascript
${1:var callbacks = \$.Callbacks();}${2}${3:callbacks}.remove(${4:callbacks});
```

### [jq.cb] callbacks

```javascript
${1:\$}.Callbacks(${2:flags});
```
