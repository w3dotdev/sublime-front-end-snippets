# ReactJS Snippets

## key: `jr.z.testutils`

### findAllInRenderedTree

```javascript
var CompositeComponent = React.createClass({
  render () {
    return <div><div /></div>;
  }
});

var componentTree = TestUtils.renderIntoDocument(
  <CompositeComponent />
);

var allDivs = TestUtils.findAllInRenderedTree(
  componentTree,
  (c) => c.tagName === 'DIV'
)

expect(allDivs).toBeAn('array');
expect(allDivs.length).toBe(2);
```

### findRenderedComponentWithType

```javascript
var MyCompositeComponent = React.createClass({
  render () { return <TargetComponent /> }
});

var TargetComponent = React.createClass({
  render () { return <div /> }
});

var componentTree = TestUtils.renderIntoDocument(
  <MyCompositeComponent />
);

var onlyTargetComponent = TestUtils.findRenderedComponentWithType(
  componentTree,
  TargetComponent
);

expect(onlyTargetComponent).toBeAn('object');
expect(onlyTargetComponent).toNotBeAn('array');
expect(TestUtils.isCompositeComponentWithType(
  onlyTargetComponent,
  TargetComponent
)).toBe(true);
```

### findRenderedDOMComponentWithClass

```javascript
var MyCompositeComponent = React.createClass({
  render () {
    return <MyNestedComponent />;
  }
});

var MyNestedComponent = React.createClass({
  render () {
    return <div className="nested"/>;
  }
});

var componentTree = TestUtils.renderIntoDocument(<MyCompositeComponent />);

var singleComponentWithMatchedClass = TestUtils.findRenderedDOMComponentWithClass(
  componentTree,
  'nested'
);

expect(singleComponentWithMatchedClass).toBeAn('object');
expect(singleComponentWithMatchedClass).toNotBeAn('array');
expect(singleComponentWithMatchedClass.className).toBe('nested');
```

### findRenderedDOMComponentWithTag

```javascript
var MyCompositeComponent = React.createClass({
  render () {
    return <MyNestedComponent />;
  }
});

var MyNestedComponent = React.createClass({
  render () {
    return <div />;
  }
});

var componentTree = TestUtils.renderIntoDocument(<MyCompositeComponent />);

var onlyDiv = TestUtils.findRenderedDOMComponentWithTag(
  componentTree,
  'div'
);

expect(onlyDiv).toBeAn('object');
expect(onlyDiv).toNotBeAn('array');
expect(onlyDiv.tagName).toBe('DIV');
```

### isCompositeComponentWithType

```javascript
var CompositeComponent = React.createClass({
  render () {
    return <div />;
  }
});

var subject = TestUtils.renderIntoDocument(
  <CompositeComponent />
);

expect(
  TestUtils.isCompositeComponentWithType(
    subject,
    CompositeComponent
  )
).toBe(true);
```

### isCompositeComponent

```javascript
var subject = TestUtils.renderIntoDocument(
  <CompositeComponent />
);

expect(
  TestUtils.isCompositeComponent(subject)
).toBe(true);
```

### isDOMComponent

```javascript
var subject = TestUtils.renderIntoDocument(<div />);

expect(
  TestUtils.isDOMComponent(subject)
).toBe(true);
```

### isElementOfType

```javascript
var MyComponent = React.createClass({
  render () {
    return <div />;
  }
});

expect(
  TestUtils.isElementOfType(<MyComponent />, MyComponent)
).toBe(true);
```

### isElement

```javascript
expect(TestUtils.isElement(<div />)).toBe(true);
```

### mockComponent

```javascript
mockComponent
```

### renderIntoDocument

```javascript
var componentTree = TestUtils.renderIntoDocument(<div><span /></div>);

console.log('You mounted a component tree with a ' + componentTree.tagName + ' at the root!');
```

### scryRenderedComponentsWithType

```javascript
var MyCompositeComponent = React.createClass({
  render () {
    return (
      <div>
        <Target />
        <br />
        <Target />
      </div>
    )
  }
});

var Target = React.createClass({
  render () {
    return <div />;
  }
});

var componentTree = TestUtils.renderIntoDocument(
  <MyCompositeComponent />
);

var allTargetComponents = TestUtils.scryRenderedComponentsWithType(
  componentTree,
  Target
);

expect(allTargetComponents).toBeAn('array');
expect(allTargetComponents.length).toBe(2);
```

### scryRenderedDOMComponentsWithClass

```javascript
var CompositeComponent = React.createClass({
  render () {
    return (
      <div className="target">
        <div className="not-target">
          <div className="target" />
        </div>
      </div>
    );
  }
});

var componentTree = TestUtils.renderIntoDocument(
  <CompositeComponent />
);

var allDOMComponentsWithMatchingClass = TestUtils.scryRenderedDOMComponentsWithClass(
  componentTree,
  'target'
);

expect(allDOMComponentsWithMatchingClass).toBeAn('array');
expect(allDOMComponentsWithMatchingClass.length).toBe(2);
```

### scryRenderedDOMComponentsWithTag

```javascript
var CompositeComponent = React.createClass({
  render () {
    return <div><div /></div>;
  }
});

var componentTree = TestUtils.renderIntoDocument(
  <CompositeComponent />
);

var allDivs = TestUtils.scryRenderedDOMComponentsWithTag(
  componentTree,
  'DIV'
);

expect(allDivs).toBeAn('array');
expect(allDivs.length).toBe(2);
```

### Shallow rendering (basics)

```javascript
// 1. create a renderer
var renderer = TestUtils.createRenderer();

// 2. render component into renderer
renderer.render(<MyComponent />);

// 3. capture renderer output
var subject = renderer.getRenderOutput();

// 4. make assertions
expect(subject.type).toBe('div');
```

### Shallow rendering (child-count)

```javascript
var renderer = TestUtils.createRenderer();

renderer.render(
  <MyList items={[1, 2, 3]} />
);

var subject = renderer.getRenderOutput();

var childCount = React.Children.count(subject.props.children);

expect(childCount).toBe(3); // => true
```

### Shallow rendering (child-equality)

```javascript
var renderer = TestUtils.createRenderer();

renderer.render(
  <MyComponent>
    <div>Thing 1</div>
    <div>Thing 2</div>
  </MyComponent>
);

var subject = renderer.getRenderOutput();

expect(subject.props.children).toEqual([
  <div>Thing 1</div>,
  <div>Thing 2</div>
]); // => true
```

### Shallow rendering (events)

```javascript
var renderer = TestUtils.createRenderer();

var spy = expect.createSpy();

renderer.render(<MyComponent onClick={spy} />);

var subject = renderer.getRenderOutput();

expect(spy.call.length).toEqual(1); // => true
```

### Shallow rendering (props)

```javascript
var renderer = TestUtils.createRenderer();

renderer.render(<MyComponent className="my-component" />);

var subject = renderer.getRenderOutput();

expect(subject.props.className).toBe('my-component'); // => true
```

### Shallow rendering (state changes)

```javascript
var renderer = TestUtils.createRenderer();

renderer.render(<ClickCounter />);

// test initial rendering
var result = renderer.getRenderOutput();

expect(result.props.children).toEqual(0);


// test post-click rendering
result.props.onClick();

var clickedResult = renderer.getRenderOutput();

expect(clickedResult.props.children).toEqual(1);
```

### Shallow rendering (type)

```javascript
var renderer = TestUtils.createRenderer();

renderer.render(<MyComponent />);

var subject = renderer.getRenderOutput();

expect(subject.type).toBe('div');  // => true
```

### Simulate (basic)

```javascript
var subject = TestUtils.renderIntoDocument(
  <div onClick={handleClick} />
);

TestUtils.Simulate.click(subject);
```

### Simulate (with data)

```javascript
function handleChange (event) {
  console.log('A change was simulated with key: ' + event.key);
}

var subject = TestUtils.renderIntoDocument(
  <input type="text" onChange={handleChange} />
);

TestUtils.Simulate.change(subject, { key: "Enter" });
```
