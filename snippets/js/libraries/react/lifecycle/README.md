## ReactJS Snippets

### [jr.cdmount] componentDidMount

```javascript
componentDidMount: function () {
  // invoked once (client-only), after initial 'render'
  // good for AJAX, setTimeout, setInterval
}
```

### [jr.cdupdate] componentDidUpdate

```javascript
componentDidUpdate: function (prevProps, prevState) {
  // invoked immediately after DOM updates, not for initial 'render'
}
```

### [jr.cwmount] componentWillMount

```javascript
componentWillMount: function () {
  // invoked once, before initial 'render'
}
```

### [jr.cwrprops] componentWillReceiveProps

```javascript
componentWillReceiveProps: function (nextProps) {
  // invoked when component is receiving props, not for initial 'render'
}
```

### [jr.cwunmount] componentWillUnmount

```javascript
componentWillUnmount: function () {
  // invoked immediately before a component is unmounted from the DOM
}
```

### [jr.cwupdate] componentWillUpdate

```javascript
componentWillUpdate: function (nextProps, nextState) {
  // invoked immediately before rendering with new props or state, not for initial 'render'
  // see componentWillReceiveProps if you need to call setState
}
```

### [jr.scupdate] shouldComponentUpdate

```javascript
shouldComponentUpdate: function (nextProps, nextState) {
  // invoked before rendering with new props, not for initial 'render'
}
```
