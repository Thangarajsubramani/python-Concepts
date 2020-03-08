function topWords(array){

counts = {}

for(const value  of  array){
if(counts.hasOwnProperty(value)){
counts[value] = counts[value] + 1;
}
else{
  counts[value] = 1;
}
}

console.log(counts);

counts = Object.entries(counts);


for(const [key, value] of counts){
  console.log(key, value);
}





return counts.sort(function(a, b) { 
    return a[1] < b[1] ? 1 : -1;
});

}

topWords(['yes','win', 'apple', 'apple', 'yes', 'no']);
