let tbody = document.getElementsByTagName('tbody')[0].children

let i = 0
let arr = []

for (let item of tbody) {
    if (!item.children[1].children[0].title.includes('FII') &&
        !item.children[1].children[0].title.includes('Corp') &&
        !item.children[1].children[0].title.includes('US') &&
        !item.children[1].children[0].title.includes('Inc')){
        arr.push(item.children[1].children[0].href);
        i++;
    }
}

console.log(arr);

var download = document.getElementById('download');
download.setAttribute('href', 'data:text/txt;charset=utf-8,' + encodeURIComponent(arr));
download.setAttribute('download', 'filename.txt');