var iPad = navigator.userAgent.match(/iPad/i) != null;
var DIM = {	'contentMarginWidth' : 0,
		'contentMarginHeight' : 0,
		'contentBorderWidth' : 0,
		'contentBorderHeight' : 0,
		'headerHeight': 34
          };

window.onload = function() {
    var innerHTML = '';

    // header
    innerHTML +=
'<a href="../toc.html" id="pageHeader">' + notebook['name'] + '</a>' +
//'<p> page['name'] </p>' +
'<div id="pageNumber">' +
'<a href="' + (page['number'] > 1 ? '../' + (page['number'] - 1) + '/index.html' : '#') + '"><img id="prevPageButton" src="' + staticUrl + '/images/PreviousPageButton.png" /></a>' +
'(' + page['number'] + '/' + notebook['pageCount'] + ')' +
'<a href="' + (page['number'] < notebook['pageCount'] ? '../' + (page['number'] + 1) + '/index.html' : '#') + '"><img id="nextPageButton" src="' + staticUrl + '/images/NextPageButton.png" /></a>' +
'</div>';

    // content
    var top = DIM['headerHeight'] + 2 * DIM['contentMarginHeight'];
    innerHTML +=
'<div id="content" style="width:' + (page['width'] + DIM['contentMarginWidth']) + 'px;height=' + (page['height'] + top) + 'px;top:' + top + 'px;">' +
'<div id="pageBackground" style="width:' + page['width'] + 'px;height:' + page['height'] + 'px;">';

    if( page['withPdfBackground'] && iPad ) {
        innerHTML += '<iframe src="background.pdf" width="' + page['width'] + '" height="' + page['height'] + '" frameborder="0" marginwidth="0" marginheight="0"></iframe>';
    }

    innerHTML +=
'</div>' +
'<object id="svg"  data="page.svg" type="image/svg+xml" width="' + page['width'] + '" height="' + page['height'] + '"></object>';

    // border for page content
    var imgPre = staticUrl + '/images/GrayCarbon_ContentBorder';
    var x1 = w1 = DIM['contentBorderWidth'];
    var x2 = page['width'] - DIM['contentBorderWidth'];
    var w2 = page['width'] - 2 * DIM['contentBorderWidth'];
    var y1 = h1 = DIM['contentBorderHeight'];
    var y2 = page['height'] - DIM['contentBorderHeight'];
    var h2 = page['height'] - 2 * DIM['contentBorderHeight'];
    innerHTML +=
'<div id="pageBorder" style="width:' + page['width'] + 'px;height=' + page['height'] + 'px;">' +
'<img src="' + imgPre + 'TopLeft.png" width="' + w1 + '" height="' + h1 + '" class="pageBorder" style="top:0px;left:0px;" />' +
'<img src="' + imgPre + 'Top.png" width="' + w2 + '" height="' + h1 + '" class="pageBorder" style="top:0px;left:' + x1 + 'px;" />' +
'<img src="' + imgPre + 'TopRight.png" width="' + w1 + '" height="' + h1 + '" class="pageBorder" style="top:0px;left:' + x2 + 'px;" />' +
'<img src="' + imgPre + 'Right.png" width="' + w1 + '" height="' + h2 + '" class="pageBorder" style="top:' + y1 + 'px;left:' + x2 + 'px;" />' +
'<img src="' + imgPre + 'BottomRight.png" width="' + w1 + '" height="' + h1 + '" class="pageBorder" style="top:' + y2 + 'px;left:' + x2 + 'px;" />' +
'<img src="' + imgPre + 'Bottom.png" width="' + w2 + '" height="' + h1 + '" class="pageBorder" style="top:' + y2 + 'px;left:' + x1 + 'px;" />' +
'<img src="' + imgPre + 'BottomLeft.png" width="' + w1 + '" height="' + h1 + '" class="pageBorder" style="top:' + y2 + 'px;left:0px;" />' +
'<img src="' + imgPre + 'Left.png" width="' + w1 + '" height="' + h2 + '" class="pageBorder" style="top:' + y1 + 'px;left:0px;" />' +
'</div>' +
'</div>';

    document.getElementById('wrapper').innerHTML = innerHTML;

}
