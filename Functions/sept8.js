function NFLTeam(name, color, city){
    this.name = name;
    this.color = color;
    this.city = city;
    this.players = [];
}

function players(name, position, jersey_num){
    this.name = name;
    this.position = position;
    this.jersey_num = jersey_num;
}


seahawks = new NFLTeam("Seahawks", "Purple", "Seattle")
seahawks.players.push(new players("bob", "QB", 42))

