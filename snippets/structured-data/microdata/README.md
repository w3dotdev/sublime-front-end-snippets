# Schema (microdata)

key: `zmicrodata`

### Organization

```html
<div itemscope itemtype="http://schema.org/Organization">
  <span itemprop="name">Google.org (GOOG)</span>
Contact Details:
  <div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
    Main address:
      <span itemprop="streetAddress">38 avenue de l'Opera</span>
      <span itemprop="postalCode">F-75002</span>
      <span itemprop="addressLocality">Paris, France</span>
    ,
  </div>
    Tel:<span itemprop="telephone">( 33 1) 42 68 53 00 </span>,
    Fax:<span itemprop="faxNumber">( 33 1) 42 68 53 01 </span>,
    E-mail: <span itemprop="email">secretariat(at)google.org</span>
Members:
- National Scientific Members in 100 countries and territories: Country1, Country2, ...
- Scientific Union Members, 30 organizations listed in this Yearbook:
List of Alumni:
 <span itemprop="alumni" itemscope itemtype="http://schema.org/Person">
   <span itemprop="name">Jack Dan</span>
 </span>,
 <span itemprop="alumni" itemscope itemtype="http://schema.org/Person">
   <span itemprop="name">John Smith</span>
 </span>,
History:
</div>
```

### Article

```html
<div itemscope itemtype="http://schema.org/Article">
  <span itemprop="name">How to Tie a Reef Knot</span>
  by <span itemprop="author">John Doe</span>
  This article has been tweeted 1203 times and contains 78 user comments.
  <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
    <div itemprop="interactionService" itemscope itemid="http://www.twitter.com" itemtype="http://schema.org/Website">
      <meta itemprop="name" content="Twitter" />
    </div>
    <meta itemprop="interactionType" content="http://schema.org/ShareAction"/>
    <meta itemprop="userInteractionCount" content="1203" />
  </div>
  <div itemprop="interactionStatistic" itemscope itemtype="http://schema.org/InteractionCounter">
    <meta itemprop="interactionType" content="http://schema.org/CommentAction"/>
    <meta itemprop="userInteractionCount" content="78" />
  </div>
</div>
```

### Book

```html
<!-- Uses both the "Book" and "Product" item types to support Offer relationships -->
<div itemscope itemtype="http://schema.org/Book" itemid="#record">
 <link itemprop="additionalType" href="http://schema.org/Product"/>
 <h3 itemprop="name">Le concerto</h3>
 <table summary="Bibliographic Details">
   <tr>
     <th>Main Author: </th>
     <td itemprop="author">Ferchault, Guy</td>
   </tr>
 </table>
</div>
<table summary="Holdings details from Anytown City Library">
 <!-- Example of a copy available for loan -->
 <tr itemscope itemtype="http://schema.org/Offer">
   <th>Copy </th>
   <td>Available
     <link itemprop="availability" href="http://schema.org/InStock">
     <div>Barcode: <span itemprop="serialNumber">CONC91000937</span></div>
     <div>Call number: <span itemprop="sku">780 R2</span></div>
     <div>Library: <span itemprop="offeredBy" itemtype="http://schema.org/Library" itemid="http://library.anytown.gov.uk" >Anytown City Library</span></div>
     <link itemprop="businessFunction" href="http://purl.org/goodrelations/v1#LeaseOut">
     <link itemprop="itemOffered" href="#record">
   </td>
 </tr>
<table>
```

### Game

```html
<section itemscope itemtype="http://schema.org/Game">
    <section itemprop="offers" itemscope itemtype="http://schema.org/Offer">
        <span>Approx. Retail:</span>
        <span itemprop="priceCurrency">$</span><span itemprop="price">17.99</span>
        <a href="/monopoly-2/en_US/shop/where-to-buy.cfm?brand_guid=DAD28866-1C43-11DD-BD0B-0800200C9A66&prodName=Monopoly%20Game" itemprop="availableAtOrFrom">Where To Buy</a>
    </section>
    <span itemprop="audience" itemscope itemtype="http://schema.org/PeopleAudience">
      Ages: <span itemprop="suggestedMinAge">8</span> YEARS & UP
    </span>
      <h4>Game  Description:</h4>
    <p itemprop="description">Own it all as a high-flying trader in the fast-paced world of real estate. Tour the city for the hottest properties: sites, stations and utilities are all up for grabs. Invest in houses and hotels, then watch the rent come pouring in! Make deals with other players and look out for bargains at auction. There are many ways to get what you want. For really speedy dealers, use the speed die for a quick and intense game of Monopoly. So get on Go and trade your way to success!<br/><br/>Includes <span itemprop="gameItem">gameboard</span>, <span itemprop="gameItem">8 tokens</span>, <span itemprop="gameItem">28 Title Deed cards</span>, <span itemprop="gameItem">16 Chance cards</span>, <span itemprop="gameItem">16 Community Chest cards</span>, <span itemprop="gameItem">money pack</span>,<span itemprop="gameItem"> 32 houses</span>, <span itemprop="gameItem">12 hotels</span>, 2 dice and instructions<br/><br/>•Features a speed die for a faster, more intense game<br/>•Includes the new token that was voted No. 1: the cat<br/><br/>For <div itemprop="numberOfPlayers" itemscope itemtype="http://schema.org/QuantitativeValue">
<span itemprop="minValue">3</span> to <span itemprop="maxValue">5</span>  players </div>.<br/><br/>Ages 8 and up.<br/><br/>Monopoly and all related characters are trademarks of <span itemprop="copyrightHolder">Hasbro</span>. <P></p>
</section>
```

### Webpage

```html
<body itemscope itemtype="http://schema.org/WebPage">
...
<div itemprop="breadcrumb">
  <a href="category/books.html">Books</a> >
  <a href="category/books-literature.html">Literature & Fiction</a> >
  <a href="category/books-classics">Classics</a>
</div>
<div itemprop="mainEntity" itemscope itemtype="http://schema.org/Book">
<img itemprop="image" src="catcher-in-the-rye-book-cover.jpg"
     alt="cover art: red horse, city in background"/>
<span itemprop="name">The Catcher in the Rye</span> -
 <link itemprop="bookFormat" href="http://schema.org/Paperback">Mass Market Paperback
by <a itemprop="author" href="/author/jd_salinger.html">J.D. Salinger</a>
<div itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating">
  <span itemprop="ratingValue">4</span> stars -
  <span itemprop="reviewCount">3077</span> reviews
</div>
<div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
  Price: <span itemprop="price" content="6.99">$6.99</span>
  <meta itemprop="priceCurrency" content="USD" />
  <link itemprop="availability" href="http://schema.org/InStock">In Stock
</div>
Product details
<span itemprop="numberOfPages">224</span> pages
Publisher: <span itemprop="publisher">Little, Brown, and Company</span> -
 <meta itemprop="datePublished" content="1991-05-01">May 1, 1991
Language: <span itemprop="inLanguage">English</span>
ISBN-10: <span itemprop="isbn">0316769487</span>
Reviews:
<div itemprop="review" itemscope itemtype="http://schema.org/Review">
  <span itemprop="reviewRating">5</span> stars -
  <b>"<span itemprop="name">A masterpiece of literature</span>"</b>
  by <span itemprop="author">John Doe</span>,
  Written on <meta itemprop="datePublished" content="2006-05-04">May 4, 2006
  <span itemprop="reviewBody">I really enjoyed this book. It captures the essential
  challenge people face as they try make sense of their lives and grow to adulthood.</span>
</div>
<div itemprop="review" itemscope itemtype="http://schema.org/Review">
  <span itemprop="reviewRating">4</span> stars -
  <b>"<span itemprop="name">A good read.</span>" </b>
  by <span itemprop="author">Bob Smith</span>,
  Written on <meta itemprop="datePublished" content="2006-06-15">June 15, 2006
  <span itemprop="reviewBody">Catcher in the Rye is a fun book. It's a good book to read.</span>
</div>
</div>
...
</body>
```
