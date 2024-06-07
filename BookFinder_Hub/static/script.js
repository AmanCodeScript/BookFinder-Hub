/** 
    jsondata = {
        'sites': [
            {
                'site': string,
                'items': number,
                'name': list,
                'price': list,
                'desc': list,
                'link': list,
            },
        ],
    }    
*/

for(let key in jsondata) {
    var n = "";

    for(let i  in jsondata[key]) {
        var s = jsondata[key][i];
        if(s != null) {
            n = s.site;
            for(let j = 0; j < s.items; ++j) {
                document.getElementById('price').innerHTML = "<p>"+ s.price[j]+"</p>";   
            }
        }
    }

    document.getElementById('site').innerHTML = `<p>${s.price[j]}</p>`;
}