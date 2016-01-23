# HTML Snippets

## Schema

Prefix `hs-*`

### [hs-sne] http://www.schema.org/SiteNavigationElement

```html
<ul itemscope="itemscope" itemtype="http://www.schema.org/SiteNavigationElement">
  <li itemprop="name">
    <a itemprop="url" href="${1:#}">$2</a>
  </li>
</ul>
```