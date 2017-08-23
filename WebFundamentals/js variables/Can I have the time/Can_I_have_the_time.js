function Tell_time(Hour, Minute, period){

    if(period == "am" && Minute > 30){
        Hour = Hour++;
        // if(Hour > 12){
        //     Hour = Hour-12;
        // }
        console.log("It is almost", Hour, "in the morning");
    }
   else if(period == "pm" && Minute > 30){
       Hour = Hour++;
        console.log("It is almost ", Hour, "in the evening");    
    }
    else if(period == "am" && Minute < 30){
        console.log("It is just past ", Hour, " in the morning");
    }
    else {
        console.log("It is just past ", Hour, " in the evening");
    }
}

Tell_time(6, 22, "am");
Tell_time(8, 44, "pm");