// page 16, number 13

function HugeSucker(){
    var sum = 0;
    for(var i = -300000; i < 300001; i++){
        if(i % 2 === 1){
            sum= sum+i;
        }
    }
    console.log(sum);
}

HugeSucker();
