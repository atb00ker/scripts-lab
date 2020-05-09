$(document).ready(function () {
    $('.sidenav').sidenav();
});

function addFocus(ele) {
    var li = document.getElementsByTagName('li');
    for (i = 0; i < li.length; i++) {
        li[i].classList.remove('icon-side-active')
    }
    ele.classList.add('icon-side-active');
};
(function () {
    var li = document.getElementsByTagName('li');
    li[2].classList.add('icon-side-active');

    var articleObj = document.getElementById('article-objects');
    var articleList = []
    articleList[0] = { "amount": 500, "name": "Blog / Article" }
    articleList[1] = { "amount": 1000, "name": "Newsletter / E-mailer" }
    articleList[2] = { "amount": 2000, "name": "Whitepaper" }
    articleList[3] = { "amount": 1000, "name": "e-book" }
    articleList[4] = { "amount": 1000, "name": "Report / Guide" }
    articleList[5] = { "amount": 500, "name": "Product Description" }
    articleList[6] = { "amount": 1000, "name": "Website Content" }
    articleList[7] = { "amount": 1000, "name": "Video Script" }
    articleList[9] = { "amount": 2000, "name": "Company Profile / Brochure" }
    articleList[9] = { "amount": 2000, "name": "Press Release" }

    for (art in articleList) {
        html = '<div class="col s12 m6 l4"><div class="content-card card"><div class="card-content"><div class="row"><div class="col s3"><div class="content-image-container"><img class="content-image" src="https://kurzgesagt.org/wp-content/themes/kurzgesagt/library/images/logo.gif"></div></div><div class="col s9"><span class="blog-title">' + articleList[art].name + '</span></div><div class="col s9"><span class="price">from ₹' + articleList[art].amount + '</span></div><div class="col s12"><div class="blog-content">Typically 450-400 words, an e-book is perfect for your target audidence ranging from prospective customers to users.</div></div><div class="col s12"><div class="blog-action"><a href="#">Order</a></div></div></div></div></div></div>';
        articleObj.innerHTML += html;
    }


})();



