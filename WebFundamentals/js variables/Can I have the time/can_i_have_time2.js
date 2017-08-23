function canIhaveTime(){
    var HOUR = 8;
    var MINUTE = 10;
    var period = "am";

    var str = "It's ";

    if(MINUTE > 30){
        str+= "almost" +(hour +1);
    }
        else {
            str=+"just after" + HOUR;
        }

    if(period = "pm"){
        str+=" in the evening."
    } else {str += "in the morning."}

    console.log(str);
    }


canIhaveTime();