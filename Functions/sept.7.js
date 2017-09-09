// pokemon

var bulbasaur = {name: "Bulbasaur", type: "Grass & Poison", attack: "49"}

var ivysaur = {name: "Ivysaur", type: "grass/poison", attack: "62"}

function Pokemon(name, type, attack){
    this.name = name;
    this.type = type;
    this.attack =attack;
}

var t1 = new Pokemon("Bulbasaur", "Grass & Poison", 49)
var t2 = new Pokemon("Ivysaur", "Grass & Poison", 62)

