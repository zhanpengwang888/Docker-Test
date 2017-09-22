function initImage(textName, pageNumber) {
    var fixedName = textName.replace(/ /g, "-");
    var url = "/static/zapotexts/img/printed_manuscripts/" + fixedName + "/" + pageNumber + ".jpg";
    $("#pageImage").addClass("faded-image").attr("src", url);
}
