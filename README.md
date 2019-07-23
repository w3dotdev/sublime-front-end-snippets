# Front-end Project Snippets

[![licence mit](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](http://hemersonvianna.mit-license.org/)
[![GitHub issues](https://img.shields.io/github/issues/org-moon-world/sublime-front-end-snippets.svg)](https://github.com/org-moon-world/sublime-front-end-snippets/issues)
<!-- ![GitHub package.json version](https://img.shields.io/github/package-json/v/org-moon-world/sublime-front-end-snippets.svg) -->
![GitHub Release Date](https://img.shields.io/github/release-date/org-moon-world/sublime-front-end-snippets.svg)
![GitHub top language](https://img.shields.io/github/languages/top/org-moon-world/sublime-front-end-snippets.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/org-moon-world/sublime-front-end-snippets.svg)
![GitHub All Releases](https://img.shields.io/github/downloads/org-moon-world/sublime-front-end-snippets/total.svg)

[![Travis](https://img.shields.io/travis/org-moon-world/sublime-front-end-snippets.svg?style=flat-square)](https://travis-ci.org/org-moon-world/sublime-front-end-snippets)
[![Package Control](https://img.shields.io/packagecontrol/dt/Front-end%20Project%20Snippets.svg?style=flat-square)](https://packagecontrol.io/packages/Front-end%20Project%20Snippets)

![animation](https://cloud.githubusercontent.com/assets/1963897/12625364/a94decc8-c51a-11e5-8546-ca331af65982.gif)

## Translations

* [Portuguese - Brazil](translations/pt_BR)

## Install

If you already have the [Package Control](http://wbond.net/sublime_packages/package_control) installed , just search for `Front-end Project Snippets`. If you have not installed in the Sublime, you can do it [here](http://wbond.net/sublime_packages/package_control/installation).

You can manually download the package and place it within your `Packages` directory. It will work, but it will not be automatically updated.

You can see all installed snippets in `Tools > Snippets...`, in the Sublime Text.

[Tested on windows] When the "."(dot) is used, the autocomplete disappears.. Solve this problem, just put in your user `Preferences >  Settings - User`, the property `word_separators` with value without the "."(dot). You can see an example [here](Preferences.sublime-settings).

## Snippets and prefixes/keys

- [HTML - h.*](snippets/html/)
  - [Microdata - hm.*](snippets/html/schema/microdata)
  - [WAI-ARIA - hw.*](snippets/html/wai-aria)
- [CSS - c.*](snippets/css/) 
- [JavaScript - j.*](snippets/js/vanilla)
  - [EcmaScript 2015 - je.*](snippets/js/es6/)
  - [Libraries](snippets/js/libraries)
    - [jQuery - jq.*](snippets/js/libraries/jquery)
    - [React - jr.*](snippets/js/libraries/react)
  - [Patterns](snippets/js/patterns)
    - [Design Patterns - jdp.*](snippets/js/patterns/design-patterns)
    - [UMD - jumd.*](snippets/js/patterns/umd)
  - [Tests](snippets/js/tests)
    - [Common - t.*](snippets/js/tests/common)
    - [Chai - tc.*](snippets/js/tests/chai)
    - [Jasmine - tj.*](snippets/js/tests/jasmine)
    - [Mocha - tm.*](snippets/js/tests/mocha)
    - [Node - tn.*](snippets/js/tests/node)
    - [QUnit - tq.*](snippets/js/tests/qunit)
    - [Sinon - ts.*](snippets/js/tests/sinon)
- [Regex](snippets/regex/)
- [Schema.org](snippets/schema)
  - [JSON-LD - sj.*](snippets/schema/json-ld)
  - [Microdata - sm.*](snippets/schema/microdata)
  - [RDFa - sr.*](snippets/schema/rdfa)
- [External - e.*](snippets/external/)
- [Comment](snippets/comment/)
  - [HTML - hc.*](snippets/comment/html)
  - [CSS - cc.*](snippets/comment/css)
  - [JavaScript - jc.*](snippets/comment/js)
- [Structure data](snippets/structured-data) (***examples***)
  - [Microdata - z.microdata](snippets/structured-data/microdata)
  - [JSON-LD - z.jsonld](snippets/structured-data/json-ld)
  - [RDFa - z.rdfa](snippets/structured-data/rdfa)

## References

* [@caiogondim](https://github.com/caiogondim) (Caio Gondim)
  [https://github.com/caiogondim/js-patterns-sublime-snippets](https://github.com/caiogondim/js-patterns-sublime-snippets)
* [@zenorocha](https://github.com/zenorocha) (Zeno Rocha)
  [https://github.com/zenorocha/sublime-javascript-snippets](https://github.com/zenorocha/sublime-javascript-snippets)
* [@joshnh](https://github.com/joshnh) (Joshua Hibbert)
  [https://github.com/joshnh/CSS-Snippets](https://github.com/joshnh/CSS-Snippets)
* (Schema.org) [http://schema.org/](http://schema.org/)
* (jQuery) [https://api.jquery.com/](https://api.jquery.com/)
* (jQuery Boilerplate)[https://jqueryboilerplate.com/](https://jqueryboilerplate.com/)
* (JSDuck) [https://github.com/senchalabs/jsduck](https://github.com/senchalabs/jsduck)
* (idiomatic CSS) [https://github.com/necolas/idiomatic-css](https://github.com/necolas/idiomatic-css)
* (JS Design Patterns) [https://addyosmani.com/resources/essentialjsdesignpatterns/book/](https://addyosmani.com/resources/essentialjsdesignpatterns/book/)
* (Node.js Assert) [https://nodejs.org/api/assert.html](https://nodejs.org/api/assert.html)
* (Jasmine) [http://jasmine.github.io/2.0/introduction.html](http://jasmine.github.io/2.0/introduction.html)
* (ReactJS cheatsheet) [http://reactcheatsheet.com/](http://reactcheatsheet.com/)
* (ES6 Features) [https://github.com/lukehoban/es6features#readme](https://github.com/lukehoban/es6features#readme)

## Contributing

- Fork it!
- Create your feature branch: `git checkout -b my-new-feature`
- Commit your changes: `git commit -m 'Add some feature'`
- Push to the branch: `git push origin my-new-feature`
- Submit a pull request

## Log

Check [Releases](https://github.com/org-moon-world/sublime-front-end-snippets/releases) for detailed changelog.

## License

[MIT license](http://hemersonvianna.mit-license.org/) © Hemerson Vianna
