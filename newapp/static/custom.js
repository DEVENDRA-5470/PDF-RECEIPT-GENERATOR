
 function fun1(){
        var get=Number(document.getElementById('get').value)
        console.log(get)
        var set=Number(document.getElementById('set').value)
        console.log(set)
        var go=(document.getElementById('go').value=get-set)
        
}


function fun3(){
    // let date1=(document.getElementById('date2').value)
    // let nextd=document.getElementById('date3').value=date1;
    // console.log(nextd.month)
var input = document.getElementById( 'date2' ).value;
var d = new Date( input );

if ( d.valueOf() )
 { 
    year = d.getFullYear();
    month = d.getMonth();
    day = d.getDate();
    
    let nextd=document.getElementById('date3').value=day+30+"-"+month +"-"+d.getFullYear();
    
}


    
}