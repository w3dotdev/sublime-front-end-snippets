## ReactJS Snippets

### [jr.chcount] children.count

```javascript
React.Children.count(this.props.children);
```

### [jr.chfeach] children.forEach

```javascript
React.Children.forEach(this.props.children, (child, i) => {
  ${1:console.log(child + ' at index: ' + i);}
})
```

### [jr.chmap] children.map

```javascript
React.Children.map(this.props.children, (child, i) => {
  ${1}
  return child;
});
```

### [jr.clelement] cloneElement

```javascript
React.cloneElement(${1:element}, ${2:props}, ${3:...children});
```

### [jr.component] component

```javascript
class ${1:MyComponent} extends React.Component {
  render () {
    return ${2};
  }
}
```

### [jr.cclass] createClass

```javascript
var ${1:MyComponent} = React.createClass({
  render: function () {
    return ${2};
  }
});
```

### [jr.celement] createElement

```javascript
React.createElement(${1:MyComponent}, ${2:props}, ${3:...children});
```

### [jr.cfactory] createFactory

```javascript
React.createFactory(${1:MyComponentClass});
```

### [jr.ivelement] isValidElement

```javascript
React.isValidElement(${1:MyComponent});
```
