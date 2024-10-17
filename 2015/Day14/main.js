let DATA = `Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.`.split("\n")

let TEST = `Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.`.split("\n")

class Reindeer {

    constructor(name, speed, stamina, restTime) {
        this.name = name
        this.speed = speed
        this.stamina = stamina
        this.restTime = restTime
        this.traveling = true
        this.distance = 0
        this.resting = 0
        this.secondsTraveled = 0
        this.totalSecondsTraveled = 0
        this.secondsRested = 0
        this.points = 0
    }

    travel(second) {
        if(this.secondsTraveled == this.stamina) {
            this.traveling = false
            if(this.resting == 0) {
                this.resting = this.restTime
            }
        }
        if(this.traveling) { 
            this.distance += this.speed
            this.secondsTraveled += 1
            this.totalSecondsTraveled += 1
        }
        else if(this.resting > 0) {
            this.resting--;
            this.secondsRested++;
            if(this.resting == 0) {
                this.secondsTraveled = 0
                this.traveling = true
            }
        }
    }

    get traveled() {
        return this.distance
    }

}

function parse(data) {
    let reindeer = []
    for(let i = 0; i < data.length; i++) {
        split = data[i].split(" ")
        reindeer.push(new Reindeer(split[0], Number(split[3]), Number(split[6]), Number(split[13])))
    }
    return reindeer
}

function getLeader(data) {
    let max = 0
    let winner = null
    for(let r in data) {
        if(data[r].distance > max) {
            max = data[r].distance
            winner = data[r]
        }
    }
    for(let r in data) {
        if(data[r].distance == max) {
            data[r].points += 1
        }
    }
    return winner
}

function getPointsWinner(data) {
    let max = 0
    let winner = null
    for(let r in data) {
        if(data[r].points > max) {
            max = data[r].points
            winner = data[r]
        }
    }
    return winner
}

function part_one(data, seconds) {
    for(let second = 1; second <= seconds; second++) {
        for(let r in data) {
            data[r].travel(second)
        }
    }
    return getLeader(data).distance
}

function part_two(data, seconds) {
    for(let second = 1; second <= seconds; second++) {
        for(let r in data) {
            data[r].travel(second)
        }
        getLeader(data)
    }
    return getPointsWinner(data).points
}

let data = parse(DATA)
console.log(part_one(data, 2503))
data = parse(DATA)
console.log(part_two(data, 2503))