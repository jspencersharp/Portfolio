function randomChance(quarters){
    while(quarters > 0){
        var win = Math.floor(Math.random()*100);
        if(win > 1){
            var amountWon = Math.random()*50+50;
            return amountWon + quarters;
        }
    }
    return 0;
}

function playSlotsBonus(quarters, goal){
    while(quarters > 0){
        var win=Math.floor(Math.random()*100);
        if(win > 99){
            var amountWon = Math.floor(Math.random()*50+50);
            if(amountWon + quarters > goal){
                return amountWon + quarters;
            }
        else{
            quarters =+ amountWon;
            console.log("won:", quarters);
        }
        }
    }
    console.log("loosed");
    return 0;
}

playSlotsBonus(100,200);