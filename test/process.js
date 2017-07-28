// get id and delayTime
let id = process.argv[2]
let delayTime = process.argv[3]

// start time
let startTime = process.hrtime(); 
console.log('START ['+id+'] AT      : ' + getFormattedNanoSecond(startTime))

// delay and calculate endTime 
setTimeout(function(){
    let diff = process.hrtime(startTime);
    let endTime = process.hrtime(); 
    // end time
    console.log('END ['+id+'] AT        : ' + getFormattedNanoSecond(endTime))
    console.log('PROCESS ['+id+'] TAKES : ' + getFormattedNanoSecond(diff))
}, delayTime)

function getFormattedNanoSecond(time){
    let nano = time[0] * 1e9 + time[1]
    return nano.toLocaleString()
}
