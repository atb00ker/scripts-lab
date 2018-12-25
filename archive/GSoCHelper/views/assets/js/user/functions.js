makeTable();
function makeTable() {
    var orgTableContainer = document.getElementById("orgTable");
    var html = "";
    for (var x in organizations) {
        html+="<tr><td>" + parseInt(parseInt(x)+1) + "</td><td><a href='" + organizations[x]['link'] + "'>" + organizations[x]['name'] + "</a></td><td>" + organizations[x]['tech'] +"</tr>";
    }
    orgTableContainer.innerHTML+=html;
}

$(document).ready(function() {
    var table = $("#orgTable");
    table.bootstrapTable({
        search: true,
        pagination: true,
        classes: 'table table-striped table-hover',
        showRefresh: true,
        showColumns: true,
        columns : [{
           field: 'Number',
           title: 'Number',
           sortable: true
        },
        {
           field: 'Name',
           title: 'Name',
           sortable: true
        },
        {
           field: 'Technology',
           title: 'Technology',
           sortable: true
       }]
    });
});
