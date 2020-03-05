function sum(array, target){
n = array.length;
result = []
for(let i=0;i<n-2; i++) {

  for(let j= i+1;j<n-1;j++){

    for(let k= i+2; k < n;k++){

    if(array[i]+ array[j] + array[k] === target){
      result.push([array[i], array[j], array[k]]);
    }

  }

}
}
return result

}

console.log(sum([1,2,4,5,6,7], 9));

// second largest number

function second_largest(array){
 let firstmax=null;
 let secondmax=null;


 n = array.length;

 for(let i =0; i < n ; i++){
   if(array[i] > firstmax){
     
     let temp = firstmax;
     firstmax=array[i];
     secondmax= temp;
   }
   else if(array[i]> secondmax){
     secondmax = array[i];
   }
 } 
return secondmax;
}

console.log(second_largest([34,55, 48, 53]));


function second_minimum(array){
 let firstmin=Infinity;
 let secondmin=Infinity;

 n = array.length;

 for(let i =0; i < n ; i++){
   if(array[i] < firstmin){
     
     let temp = firstmin;
     firstmin=array[i];
     secondmin= temp;
   }
   else if(array[i] < secondmin){
     secondmin = array[i];
   }
 } 
return secondmin;
}

console.log(second_minimum([34,55, 48, 53]));
