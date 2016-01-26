## Events

### [jq.bind] bind

```javascript
${1:\$(document)}.bind(${2:eventType}${3:,eventData}${4:,handler});
```

### [jq.click] click

```javascript
${1:\$(document)}.click(${2:eventData}${3:,handler});
```

### [jq.cmenu] contextmenu

```javascript
${1:\$(document)}.contextmenu(${2:eventData}${3:,handler});
```

### [jq.ctarget] currentTarget

```javascript
${1:\event}.currentTarget;
```

### [jq.edata] data

```javascript
${1:\event}.data;
```

### [jq.dclick] dblclick

```javascript
${1:\$(document)}.dblclick(${2:eventData}${3:,handler});
```

### [jq.dtarget] delegateTarget

```javascript
${1:\event}.delegateTarget;
```

### [jq.delegate] delegate

```javascript
${1:\$(document)}.delegate(${2:selector}${3:,eventType}${4:,handler});
```

### [jq.hover] hover

```javascript
${1:\event}.hover(${2:handlerIn}${3:, handlerOut});
```

### [jq.idprevented] isDefaultPrevented

```javascript
${1:\event}.isDefaultPrevented();
```

### [jq.iips] isImmediatePropagationStopped

```javascript
${1:\event}.isImmediatePropagationStopped();
```

### [jq.ips] isPropagationStopped

```javascript
${1:\event}.isPropagationStopped();
```

### [jq.kdown] keydown

```javascript
${1:\event}.keydown(${2:eventData}${3:, handler});
```

### [jq.kpress] keypress

```javascript
${1:\event}.keypress(${2:eventData}${3:, handler});
```

### [jq.kup] keyup

```javascript
${1:\event}.keyup(${2:eventData}${3:, handler});
```

### [jq.mkey] metaKey

```javascript
${1:\event}.metaKey;
```

### [jq.mdown] mousedown

```javascript
${1:\$(document)}.mousedown(${2:eventData}${3:, handler});
```

### [jq.menter] mouseenter

```javascript
${1:\$(document)}.mouseenter(${2:eventData}${3:, handler});
```

### [jq.mleave] mouseleave

```javascript
${1:\$(document)}.mouseleave(${2:eventData}${3:, handler});
```

### [jq.mmove] mousemove

```javascript
${1:\$(document)}.mousemove(${2:eventData}${3:, handler});
```

### [jq.mout] mouseout

```javascript
${1:\$(document)}.mouseout(${2:eventData}${3:, handler});
```

### [jq.mover] mouseover

```javascript
${1:\$(document)}.mouseover(${2:eventData}${3:, handler});
```

### [jq.mup] mouseup

```javascript
${1:\$(document)}.mouseup(${2:eventData}${3:, handler});
```

### [jq.ns] namespace

```javascript
${1:\event}.namespace;
```

### [jq.off] off

```javascript
${1:\$(document)}.off(${2:events}${3:, selector}${4:, handler});
```

### [jq.on] on

```javascript
${1:\$(document)}.on(${2:events}${3:, selector}${4:, data}${5:, handler});
```

### [jq.one] one

```javascript
${1:\$(document)}.one(${2:events}${3:, selector}${4:, data}${5:, handler});
```

### [jq.px] pageX

```javascript
${1:\event}.pageX;
```

### [jq.py] pageY

```javascript
${1:\event}.pageY;
```

### [jq.pd] preventDefault

```javascript
${1:\event}.preventDefault();
```

### [jq.ready] ready

```javascript
${1:\$(document)}.ready(${2:handler});
```

### [jq.rtarget] relatedTarget

```javascript
${1:\event}.relatedTarget;
```

### [jq.resize] resize

```javascript
${1:\$(window)}.resize(${2:eventData}${3:, handler});
```

### [jq.result] result

```javascript
${1:\event}.result;
```

### [jq.scroll] scroll

```javascript
${1:\$(window)}.scroll(${2:eventData}${3:, handler});
```

### [jq.sip] stopImmediatePropagation

```javascript
${1:\event}.stopImmediatePropagation();
```

### [jq.sp] stopPropagation

```javascript
${1:\event}.stopPropagation();
```

### [jq.target] target

```javascript
${1:\event}.target;
```

### [jq.tstamp] timeStamp

```javascript
${1:\event}.timeStamp;
```

### [jq.thandler] triggerHandler

```javascript
${1:\$(document)}.triggerHandler(${2:eventType}${3:, extraParameters});
```

### [jq.trigger] trigger

```javascript
${1:\$(document)}.trigger(${2:eventType}${3:, extraParameters});
```

### [jq.type] type

```javascript
${1:\event}.type;
```

### [jq.unbind] unbind

```javascript
${1:\$(document)}.unbind(${2:eventType}${3:, handler});
```

### [jq.undelegate] undelegate

```javascript
${1:\$(document)}.undelegate(${2:selector}${3:, eventType}${4:, handler});
```

### [jq.which] which

```javascript
${1:\event}.which;
```
