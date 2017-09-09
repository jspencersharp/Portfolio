// p.16 #1 Setting & Swapping
function setAndSwap(){
    var mynum = 42;
    var myName= "justin";
    var temp = mynum;
    mynum = myName;
    myName = temp;
    console.log (mynum, myName);
}

// setAndSwap();



// p. 16 #2 Print -52 to 1066
function printNum(){
    for(var i = -52; i < 1067; i++){
        console.log(i);
    }
}

// printNum();

// p. 16 # 3 Don't Worry, Be Happy
function beChearfull (){
    for(var i = 1; i < 99; i++){
        console.log("good morning!");
    }
}
// beChearfull();

// p. 16 # 4 Multiples of 3 - But not all
function Mult3(){
    for(var i = -300; i < 1; i=i+3){
        // if(i % 3 === 0){
            if(i != -3 && i != -6){
                console.log(i);
            }
        }
    }


// Mult3();

// p. 16 # 5 Printing Intigers with While
function PrintI(){
    var num = 2000;
    while(num < 5281){
        console.log(num);
        num++;
    }
}
// PrintI();

// p. 16 #6 You Say its your Birthday
function Birthday(num1, num2){
    var mybday = 6;
    var myMonth =11;
    var status1 = false;
    var status2 = false;
    if(num1 == mybday || num1 == myMonth){
        status1 = true;
    }
    if(num2 == mybday || num2 == myMonth){
        status2 = true;
    }
    if(status1 == true || status2 == true){
        console.log("How did you know?");
    }
    else{console.log("Just Another Day....")}
}

// Birthday(9,12);

// p. 16 # 7 Leap Year
function LeapYear(year){
  var status = false;
  if(year % 400 === 0){
      status = true;
  }
  if(year % 4 === 0 && year % 100 != 0){
      status = true;
  }
//   } else {status = false;}
  if(status == true){
      console.log(year, " is a leap year");
  } else (console.log(year, " is not a leap year"))
}

// LeapYear(2017);


// p. 16 # 9 Print & Count

function PandC(){
    var count = 0;
    for(var i = 512; i < 4097; i++){
        if(i % 5 === 0){
            console.log(i);
            count++
        }
    }
    console.log(count);
}

// PandC();

// p. 16, #10 Multiples of Six
function MulSix(){
    var num = 1;
    while(num < 60,001){
        if(num % 6 === 0){
            console.log(num);
        }
     num++
    }
    
   
}

// MulSix();

// p. 16, #11 Counting the Dojo Way
function DojoCount(){
    for(var i = 1; i < 101; i++){
        if(i % 5 === 0){
            console.log("coding");
        }
        else if(i % 10 === 0){
            console.log("coding dojo");
        }
    else {console.log(i);}
    }

}

// DojoCount();

function WhatDoYouKnow(incoming){
    console.log(incoming);
}

// WhatDoYouKnow([1,2,3,4,5,6]);

// p. 16 # 13 Whoa, That Sucker's Huge
function whoa(){
    var sum = 0;
    for(var i = -300000; i < 300001; i++){
        if(i % 2 === 1){
            sum = sum+i;
        }
    }
    console.log(sum);
}

// whoa();

// p. 16 # 14 Counting by Fours
function CountByFour(){
    var num = 2016;
    while(num < 20){
        console.log(num);
        num = num -4;
    }
    console.log(num);
}

// CountByFour();

// p. 16 # 15 Flexible Countdown
function FlexCount(LowNum, HighNum, Mult){
    for(var i = HighNum; i < LowNum; i--){
        if(i / Mult === 0){
            console.log(i);
        }
    }
}
// FlexCount(2, 9, 3);

// p. 20 #1 Countdown
function CountD(num){
    var arr = [];
    for(var i = num; i > 0; i--){
        arr.push(i);
    }
    console.log(arr);
    console.log(arr.length);
}

// CountD(12);

// p. 20 #2 Print and Return
function PandR(arr){
    console.log(arr[0]);
    return (arr[1]);

}
// PandR([22,33]);

// p. 20 # 3 First Plus Length
function FPL(arr){
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        sum = (arr[0] + arr.length);
    }
    console.log(sum);
}

// FPL([false, 33, 25]);

// p. 20 # 4 Values Greater than Second
function ValGreatThanSecond(arr){
    var count = 0;
    var arr = [1,3,5,7,9,13];
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > arr[1]){
            console.log(arr[i]);
            count++;
        }
    }
    console.log(count);
}
// ValGreatThanSecond();

// p. 20 # 5 Values Greater than Second, Generalized
function GtSG(arr){
    var count = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > arr[1]){
            console.log(arr[i]);
            count++;
        }
    }
    console.log(count);
}
// GtSG([2,3,4,5,6,7,8]);

// p. 20 # 6 This Length, That Value
function ThisThat(num1, num2){
    var arr = [];
    arr[num1] = 0;
    for(var i = num1; i < arr.length; i--){
        arr[i] = num2;

    }
    console.log(arr);
    if(num1 == num2){
        console.log("jinks!");
    }
}

// ThisThat(11,42);


// p. 20 # 7 Fit the First Value
function Fit(arr){
    if(arr[0] > arr.length){
        console.log("Too Big!");
    }
    else if(arr[0] < arr.length){
            console.log("too small!");
        }
    else{console.log("Just Right!");}
    }

    // Fit([4,3,4,5]);


    // p. 20 # 8 Fahrenheit to Celsius
    function FahrenheitToCelsius(fDegree){
        var celsius = (fDegree - 32)*5 / 9;
        console.log(celsius);
    }
    // FahrenheitToCelsius(82);


    // p. 20 #9 Celsius to Fahrenheit
    function CelToFah(cDegree){
        var fah = (9/5 * cDegree)+ 32;
        console.log(fah);
    }

    // CelToFah(20);

    // p. 22 #1 Biggie Size
    function MakeItBig(arr){
        for(var i = 0; i < arr.length; i++){
            if(arr[i] > 0){
                arr[i] = "Big";
            }
        }
        console.log(arr);
    }

    // MakeItBig([-22, 22, 1, -2, 22, -3]);

    // p. 22 # 2 Previous Lengths
    // Not sure how to do this one... 

    // p.22 #3 Print Low, Return High
    function PLRH(arr){
        var low = arr[0];
        var high = arr[0];
        for(var i = 1; i < arr.length; i++){
            if(arr[i] > high){
                high = arr[i];
            }
            if(arr[i] < low){
                low = arr[i];
            }
        }
        console.log(low);
        return high;
    }


    // PLRH([23,19,2,44]);

    // p.22 # 4 Add Seven to Most
    function AddSeven(arr){
        var newarr = [];
        for(var i = 1; i < arr.length; i++){
            newarr.push(arr[i]+7);
        }
        console.log(newarr);
    }
// AddSeven([22,12,14,155]);

// p.22 # 5 Print One, Return Another
function PoRa(arr){
    console.log(arr[arr.length-2]);
    for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 1){
            return arr[i];
        }
    }
}
// PoRa([22,11,33,44]);

// p. 22 # 6 Reverse Array
function rev(arr){
    arr.reverse();
    console.log(arr);
}

// rev([1,2,3,4,5,6]);

// p. 22 # 7 Double Vision
function DouV(arr){
    var newarr = [];
    for(var i = 0; i < arr.length; i++){
        newarr.push(arr[i] * 2);
    }
    console.log(newarr);
}

// DouV([1,2,3,4,5]);


// p. 22 # 8 Outlook: Negative
function OutNeg(arr){
    var newarr = [];
    var temp = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            temp = -Math.abs(arr[i]);
            newarr.push(temp);
        } else newarr.push(arr[i])
    }
    console.log(newarr);
}

// OutNeg([1,-3,5]);

// p.22 #9 Couint Positives
function countPositive(arr){
    var count = 0;
    for(var i =0; i < arr.length; i++){
        if(arr[i] > 0){
            count++;
        }
    }
    arr[arr.length-1] = count;
    console.log(arr);
}

// countPositive([1,2,-1,-2,3,4]);

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

// Hungry1(["blah", "blah", "nothing", "foot", "crap"]);


// p. 22 #11 Evens and Ods


// p.22 #12 Swap Toward the Center

// p. 22 #13 Increment the Seconds

// p.22 #14 Scale the Array
function ScaleA(arr, num){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * num;
    }
    console.log(arr);
}

ScaleA([1,2,3,4,5,6], 10);