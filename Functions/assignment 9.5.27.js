function myFunction(x, y){
    if(x == typeof "function"){
        x(y);
    }
    else {
        return ("not a function");
    }
}


myFunction("My name is ... what?", "My name is... who")