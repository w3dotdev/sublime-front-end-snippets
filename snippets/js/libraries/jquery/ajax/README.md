## Ajax

### [jq.a] ajax

```javascript
${1:\$}.ajax(${2:{settings}});
```

### [jq.acomplete] ajaxComplete

```javascript
${1:\$(document)}.ajaxComplete(${2:handler});
```

### [jq.aerror] ajaxError

```javascript
${1:\$(document)}.ajaxError(${2:handler});
```

### [jq.gjson] getJSON

```javascript
${1:\$}.getJSON(${2:url}${3:, data}${4:, success});
```

### [jq.gscript] getScript

```javascript
${1:\$}.getScript(${2:url}${3:, success});
```

### [jq.jget] jQuery get

```javascript
${1:\$}.get(${2:url}${3:, data}${4:, success}${5:, dataType});
```

### [jq.load] load

```javascript
${1:\$(document)}.load(${2:url}${3:, data}${4:, complete});
```

### [jq.post] post

```javascript
${1:\$}.post(${2:url}${3:, data}${4:, success}${5:, dataType});
```

### [jq.aprefilter] ajaxPrefilter

```javascript
${1:\$}.ajaxPrefilter(${2:dataTypes,}${3:handler});
```

### [jq.asend] ajaxSend

```javascript
${1:\$(document)}.ajaxSend(${2:handler});
```

### [jq.asetup] ajaxSetup

```javascript
${1:\$}.ajaxSetup(${2:options});
```

### [jq.astart] ajaxStart

```javascript
${1:\$(document)}.ajaxStart(${2:handler});
```

### [jq.astop] ajaxStop

```javascript
${1:\$(document)}.ajaxStop(${2:handler});
```

### [jq.asuccess] ajaxSuccess

```javascript
${1:\$(document)}.ajaxSuccess(${2:handler});
```

### [jq.atransport] ajaxTransport

```javascript
${1:\$}.ajaxTransport(${2:dataType}, ${3:handlerv});
```
