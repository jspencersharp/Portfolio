function minusOne(x){
    if (typeof (x == "number")){
        console.log(x-1);
        return(x-1);
        
    }
    else if (typeof (x == "array")){
       
        x.length = x.length-1;
         console.log(x);
        return x;
    }
    else{
        return undefined;
    }
}


minusOne(132)