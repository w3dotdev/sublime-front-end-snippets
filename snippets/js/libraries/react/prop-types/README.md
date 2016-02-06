## ReactJS Snippets

### [jr.ptany] PropTypes.any

```javascript
{
  requiredAny: React.PropTypes.any.isRequired
}
```

### [jr.ptarrayof] PropTypes.arrayOf

```javascript
{
  optionalArrayOf: React.PropTypes.arrayOf(React.PropTypes.string),
  requiredArrayOf: React.PropTypes.arrayOf(React.PropTypes.string).isRequired
}
```

### [jr.ptarray] PropTypes.array

```javascript
{
  optionalArray: React.PropTypes.array,
  requiredArray: React.PropTypes.array.isRequired
}
```

### [jr.ptbool] PropTypes.bool

```javascript
{
  optionalBoolean: React.PropTypes.bool,
  requiredBoolean: React.PropTypes.bool.isRequired
}
```

### [jr.ptelement] PropTypes.element

```javascript
{
  optionalElement: React.PropTypes.element,
  requiredElement: React.PropTypes.element.isRequired
}
```

### [jr.ptfunc] PropTypes.func

```javascript
{
  optionalFunction: React.PropTypes.func,
  requiredFunction: React.PropTypes.func.isRequired
}
```

### [jr.ptiof] PropTypes.instanceOf

```javascript
{
  optionalClass: React.PropTypes.instanceOf(MyClass),
  requiredClass: React.PropTypes.instanceOf(MyClass).isRequired
}
```

### [jr.ptnode] PropTypes.node

```javascript
{
  optionalNode: React.PropTypes.node,
  requiredNode: React.PropTypes.node.isRequired
};
```

### [jr.ptnumber] PropTypes.number

```javascript
{
  optionalNumber: React.PropTypes.number,
  requiredNumber: React.PropTypes.number.isRequired
}
```

### [jr.ptobjectof] PropTypes.objectOf

```javascript
{
  optionalObjectOf: React.PropTypes.objectOf(React.PropTypes.string),
  requiredObjectOf: React.PropTypes.objectOf(React.PropTypes.string).isRequired
}
```

### [jr.ptobject] PropTypes.object

```javascript
{
  optionalObject: React.PropTypes.object,
  requiredObject: React.PropTypes.object.isRequired
}
```

### [jr.ptootype] PropTypes.oneOfType

```javascript
{
  optionalUnion: React.PropTypes.oneOfType([
    React.PropTypes.bool,
    React.PropTypes.string
  ]),

  requiredUnion: React.PropTypes.oneOfType([
    React.PropTypes.bool,
    React.PropTypes.string
  ]).isRequired,
}
```

### [jr.ptoneof] PropTypes.oneOf

```javascript
{
  optionalEnum: React.PropTypes.oneOf(['Thing 1', 'Thing 2']),
  optionalEnum: React.PropTypes.oneOf(['Thing 1', 'Thing 2']).isRequired
}
```

### [jr.ptshape] PropTypes.shape

```javascript
{
  optionalObjectWithShape: React.PropTypes.shape({
    age: React.PropTypes.number,
    name: React.PropTypes.string
  }),

  requiredObjectWithShape: React.PropTypes.shape({
    age: React.PropTypes.number,
    name: React.PropTypes.string
  }).isRequired,

  requiredObjectWithRequiredShape: React.PropTypes.shape({
    age: React.PropTypes.number.isRequired,
    name: React.PropTypes.string.isRequired
  }).isRequired,
}
```

### [jr.ptstring] PropTypes.string

```javascript
{
  optionalString: React.PropTypes.string,
  requiredString: React.PropTypes.string.isRequired
}
```
