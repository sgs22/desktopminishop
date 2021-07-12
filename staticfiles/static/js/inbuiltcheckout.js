function finishSelectFunction() {
    var e = document.getElementById("mySelect");
    var str = e.options[e.selectedIndex].value;

    if (str == 'silver') {
        document.getElementById('silverConfig').style.display = 'block';
        document.getElementById('blackConfig').style.display = 'none';
    }
    else if (str == 'black') {
        document.getElementById('blackConfig').style.display = 'block';
        document.getElementById('silverConfig').style.display = 'none';
    }
    else {
        document.getElementById('silverConfig').style.display = 'none';
        document.getElementById('blackConfig').style.display = 'none';
    }
}

function silverSelectFunction() {
    var e = document.getElementById("silverSelect");
    var str = e.options[e.selectedIndex].value;

    if (str == 'silver-8-256') {
        disabledbtn
        document.getElementById('silver-8-256').style.display = 'inline-block';
        document.getElementById('silver-16-512').style.display = 'none';
        document.getElementById('disabledbtn').style.display = 'none';
    }
    else if (str == 'silver-16-512') {
        document.getElementById('silver-8-256').style.display = 'none';
        document.getElementById('silver-16-512').style.display = 'inline-block';
        document.getElementById('disabledbtn').style.display = 'none';
    }
    else {
        document.getElementById('silver-8-256').style.display = 'none';
        document.getElementById('silver-16-512').style.display = 'none';
        document.getElementById('disabledbtn').style.display = 'inline-block';
    }
}

function blackSelectFunction() {
    var e = document.getElementById("blackSelect");
    var str = e.options[e.selectedIndex].value;

    if (str == 'black-8-256') {
        document.getElementById('black-8-256').style.display = 'inline-block';
        document.getElementById('black-16-512').style.display = 'none';
        document.getElementById('disabledbtn').style.display = 'none';
    }
    else if (str == 'black-16-512') {
        document.getElementById('black-8-256').style.display = 'none';
        document.getElementById('black-16-512').style.display = 'inline-block';
        document.getElementById('disabledbtn').style.display = 'none';
    }
    else {
        document.getElementById('black-8-256').style.display = 'none';
        document.getElementById('black-16-512').style.display = 'none';
        document.getElementById('disabledbtn').style.display = 'inline-block';
    }
}
