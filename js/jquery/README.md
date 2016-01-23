# JQuery Snippets

Prefix `jq-*`

## Dimensions

### [jq-cd] height

```javascript
${1:\$(document)}.height();
```

### [jq-cd] innerHeight

```javascript
${1:\$(document)}.innerHeight();
```

### [jq-cd] innerWidth

```javascript
${1:\$(document)}.innerWidth();
```

### [jq-cd] outerHeight

```javascript
${1:\$(document)}.outerHeight(${2:includeMargin});
```

### [jq-cd] outerWidth

```javascript
${1:\$(document)}.outerWidth(${2:includeMargin});
```

### [jq-cd] width

```javascript
${1:\$(document)}.width();
```

## Effects

### [jq-cd] animate

```javascript
${1:\$("div")}.animate(${2:properties}${3:,duration}${4:,easing}${5:,complete});
```

### [jq-cd] clearQueue

```javascript
${1:\$("div")}.clearQueue(${2:queueName});
```

### [jq-cd] delay

```javascript
${1:\$("div")}.delay(${2:duration}${3:,queueName});
```

### [jq-cd] dequeue

```javascript
${1:\$("div")}.dequeue(${2:queueName});
```

### [jq-cd] fadeIn

```javascript
${1:\$("div")}.fadeIn(${2:duration}${3:,easing}${4:,complete});
```

### [jq-cd] fadeOut

```javascript
${1:\$("div")}.fadeOut(${2:duration}${3:,easing}${4:,complete});
```

### [jq-cd] fadeToggle

```javascript
${1:\$("div")}.fadeToggle(${2:duration}${3:,easing}${4:,complete});
```

### [jq-cd] fadeTo

```javascript
${1:\$("div")}.fadeTo(${2:duration}, ${3:opacity}${4:,easing}${5:,complete});
```

### [jq-cd] finish

```javascript
${1:\$("div")}.finish(${2:queue});
```

### [jq-cd] hide

```javascript
${1:\$("div")}.hide(${2:duration}${3:,easing}${4:,complete});
```

### [jq-cd] queue

```javascript
${1:\$("div")}.queue(${2:queueName});
```

### [jq-cd] show

```javascript
${1:\$("div")}.show(${2:duration}${3:,easing}${4:,complete});
```

### [jq-cd] slideDown

```javascript
${1:\$("div")}.slideDown(${2:duration}${3:,easing}${4:,complete});
```

### [jq-cd] slideToggle

```javascript
${1:\$("div")}.slideToggle(${2:duration}${3:,easing}${4:,complete});
```

### [jq-cd] slideUp

```javascript
${1:\$("div")}.slideUp(${2:duration}${3:,easing}${4:,complete});
```

### [jq-cd] stop

```javascript
${1:\$("div")}.stop(${2:queue}${3:,clearQueue}${4:,jumpToEnd});
```

### [jq-cd] toggle

```javascript
${1:\$("div")}.toggle(${2:duration}${3:,easing}${4:,complete});
```

## Events

### [jq-cd] animate

```javascript

```

## Forms

### [jq-cd] blur

```javascript
${1:\$(document)}.blur(${2:eventData}${3:,handler});
```

### [jq-cd] change

```javascript
${1:\$(document)}.change(${2:eventData}${3:,handler});
```

### [jq-cd] focusin

```javascript
${1:\$(document)}.focusin(${2:eventData}${3:,handler});
```

### [jq-cd] focusout

```javascript
${1:\$(document)}.focusout(${2:eventData}${3:,handler});
```

### [jq-cd] focus

```javascript
${1:\$(document)}.focus(${2:eventData}${3:,handler});
```

### [jq-cd] param

```javascript
${1:\$}.param(${2:obj}${3:,traditional});
```

### [jq-cd] select

```javascript
${1:\$(document)}.select(${2:eventData}${3:,handler});
```

### [jq-cd] serializeArray

```javascript
${1:\$(this)}.serializeArray();
```

### [jq-cd] serialize

```javascript
${1:\$(this)}.serialize();
```

### [jq-cd] submit

```javascript
${1:\$(document)}.submit(${2:eventData}${3:,handler});
```

### [jq-cd] val

```javascript
${1:\$(this)}.val();
```

## Internals

### [jq-cd] error

```javascript
${1:\$}.error(${2:message});
```

### [jq-cd] pushStack

```javascript
${1:\$([])}.pushStack(${2:elements}${3:,name}${4:,arguments});
```

## Manipulation

### [jq-cd] animate

```javascript

```

## Miscellaneous

### [jq-cd] animate

```javascript

```

## Offset

### [jq-cd] offsetParent

```javascript
${1:\$(this)}.offsetParent();
```

### [jq-cd] position

```javascript
${1:\$(this)}.position();
```

### [jq-cd] scrollLeft

```javascript
${1:\$(this)}.scrollLeft();
```

### [jq-cd] scrollTop

```javascript
${1:\$(this)}.scrollTop();
```

### [jq-cd] offset

```javascript
${1:\$(this)}.offset();
```

## Properties

### [jq-cd] fx.interval

```javascript
${1:\$}.fx.interval = ${2:500};
```

### [jq-cd] fx.off

```javascript
${1:\$}.fx.off = ${2:true};
```

### [jq-cd] jquery

```javascript
${1:\$.fn}.jquery;
```

### [jq-cd] length

```javascript
${1:\$([])}.length;
```

## Selectors

### [jq-cd] animate

```javascript

```

## Traversing

### [jq-cd] animate

```javascript

```

## Utilities

### [jq-cd] animate

```javascript

```
