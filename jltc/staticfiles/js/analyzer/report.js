$(function () {
    $('#test-report-tabs li:last-child a').tab('show')
})
$("#aggregate-table").tablesorter();
$("#aggregate-table").trigger('tsUpdate');