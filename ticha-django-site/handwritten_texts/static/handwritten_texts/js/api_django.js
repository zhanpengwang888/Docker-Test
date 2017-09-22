$(document).ready(function() {
    var currentScript = $('#api_django');
    var tichaID = currentScript.attr('data-ticha-id');
    var pages = currentScript.attr('data-pages');
    var urlList = getURLs(tichaID, pages);
    console.log(urlList);
    $("#openseadragon1").html("")
    var viewer = OpenSeadragon({
        id: "openseadragon1",
        prefixUrl: "http://ticha.haverford.edu/images/openseadragon/",
        tileSources: urlList,
        showNavigator: true,
        navigatorPosition: "ABSOLUTE",
        navigatorTop: "40px",
        navigatorLeft: "4px",
        navigatorHeight: "110px",
        navigatorWidth: "90px",
        sequenceMode: true,
        showReferenceStrip: true,
        referenceStripScroll: 'horizontal',
    });
});

function getURLs(tichaID, pages) {
    var splitPages = pages.split('-');
    var pageList = [];
    if (splitPages.length === 1) {
        pageList = splitPages;
    } else {
        var firstPage = splitPages[0];
        if (firstPage.endsWith('r') || firstPage.endsWith('v')) {
            pageList = pageRangeToListRV(splitPages);
        } else {
            pageList = pageRangeToList(splitPages);
        }
    }
    var prefix = '//ticha.haverford.edu/images/dzi/' + tichaID + '_';
    var urlList = [];
    for (var i = 0; i < pageList.length; i++) {
        urlList.push(prefix + pageList[i] + '.dzi');
    }
    return urlList;
}

/* Split a regular page range, e.g. ['10', '20'], into a list ['10', '11', ..., '20'] */
function pageRangeToList(splitPages) {
    var start = parseInt(splitPages[0]);
    var end = parseInt(splitPages[1]);
    var ret = [];
    for (; start <= end; start++) {
        ret.push(start.toString());
    }
    return ret;
}

/* Split a recto-verso page range, e.g. ['9r', '10v'], into a list ['9r', '9v', '10r', '10v'] */
function pageRangeToListRV(splitPages) {
    // a page '9r' is represented by 9.0, and '9v' by 9.5
    var start = parseInt(splitPages[0]) + (splitPages[0].endsWith('v') ? 0.5 : 0.0);
    var end = parseInt(splitPages[1]) + (splitPages[1].endsWith('v') ? 0.5 : 0.0);
    var ret = [];
    for (; start <= end; start += 0.5) {
        if (start % 1 === 0) {
            ret.push(start + 'r');
        } else {
            ret.push(Math.floor(start) + 'v');
        }
    }
    return ret;
}
