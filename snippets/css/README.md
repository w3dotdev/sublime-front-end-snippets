# CSS Snippets

Prefix `c-*`

## Font

### [c-ff] @font-face

```css
@font-face {
  font-family: "$1";
  src:url("$2.eot");
  src:url("$2.eot?#iefix") format('embedded-opentype'),
      url("$2.woff2") format('woff2'),
      url("$2.woff") format('woff'),
      url("$2.ttf") format('truetype'),
      url("$2.svg#$1") format('svg');
  font-weight: ${3:400};
  font-style: normal;
  font-variant: normal;
  -webkit-font-smoothing: antialiased;
}

@media screen and (-webkit-min-device-pixel-ratio:0){
  @font-face {
    font-family: "$1";
    src: url("$2.svg#$1") format('svg');
    font-weight: ${3:400};
  }
}
```

## Media Querie

### [c-mq] @media

```css
@media ${1:all} and (${2:min-width}: ${3:768px}) {
  ${4}
}
```

## Keyframes

### [c-k] @keyframes

```css
@-webkit-keyframes ${1:[animation-name]} {
  0%   { ${2} }
  100% { ${3} }
}
@-moz-keyframes ${1} {
  0%   { ${2} }
  100% { ${3} }
}
@-o-keyframes ${1} {
  0%   { ${2} }
  100% { ${3} }
}
@keyframes ${1} {
  0%   { ${2} }
  100% { ${3} }
}
```
