function createTable(num) {
    var html = "{% include 'table.html' with net=" + num + " %}";
    document.getElementById("dynamic-table1").innerText = html;
}

function get_tag(num){
    return createTable(num)
}