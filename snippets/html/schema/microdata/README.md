# HTML Snippets

## Microdata

Prefix `hm.*`

### [hm.sitenav] http://www.schema.org/SiteNavigationElement

```html
<ul itemscope="itemscope" itemtype="http://www.schema.org/SiteNavigationElement">
  <li itemprop="name">
    <a itemprop="url" href="${1:#}">$2</a>
  </li>
</ul>
```
