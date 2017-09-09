// p.22 #10 Always Hungry
function Hungry1(arr){
    var checks = false;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] == "food"){
            console.log("yummy!");
            status = true;
        }
      
        }
      
    if(checks != true){
            console.log("I'm Hungry");
}
}

Hungry1(["blah", "blah", "nothing", "foot", "crap"]);